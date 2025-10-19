'use client'

import React, { useState } from 'react'
// Component imports - TypeScript refresh
import UploadSection from '../components/UploadSection'
import ProcessingSection from '../components/ProcessingSection'
import ResultSection from '../components/ResultSection'
import { apiService, GenerationResult } from '../lib/api'

type AppState = 'upload' | 'processing' | 'result'

export default function Home() {
  const [currentState, setCurrentState] = useState<AppState>('upload')
  const [audioFile, setAudioFile] = useState<File | null>(null)
  const [generationResult, setGenerationResult] = useState<GenerationResult | null>(null)
  const [error, setError] = useState<string | null>(null)
  const [isProcessing, setIsProcessing] = useState(false)

  const handleFileUpload = async (file: File) => {
    setAudioFile(file)
    setCurrentState('processing')
    setIsProcessing(true)
    setError(null)
    
    try {
      // Temporarily skip health check to test direct API calls
      console.log('Skipping health check for now...')
      // const healthResponse = await apiService.checkHealth()
      // console.log('Health check response:', healthResponse)
      
      // if (healthResponse.status === 'error') {
      //   throw new Error(`Backend server is not running: ${healthResponse.error}`)
      // }
      // First analyze the music
      const analysisResponse = await apiService.analyzeMusic(file)
      console.log('Music analysis:', analysisResponse.data?.analysis)
      
      // Then generate the video
      const videoResponse = await apiService.generateVideo(file)
      console.log('Full video response:', videoResponse)
      console.log('Video generation result:', videoResponse.data)
      
      if (videoResponse.status === 'success' && videoResponse.data) {
        console.log('Setting generation result:', videoResponse.data)
        console.log('Video URLs:', videoResponse.data.video_urls)
        console.log('Number of videos:', videoResponse.data.video_urls?.length || 0)
        setGenerationResult(videoResponse.data)
        setCurrentState('result')
      } else {
        console.error('Video generation failed:', videoResponse)
        throw new Error(videoResponse.error || 'No video data received')
      }
    } catch (err) {
      console.error('Error during processing:', err)
      setError(err instanceof Error ? err.message : 'An error occurred during processing')
      setCurrentState('upload')
    } finally {
      setIsProcessing(false)
    }
  }

  const handleNewUpload = () => {
    setAudioFile(null)
    setGenerationResult(null)
    setError(null)
    setCurrentState('upload')
  }

  return (
    <div className="min-h-screen bg-background">
      <div className="container mx-auto px-6 py-16">
        <header className="text-center mb-20">
          <h1 className="text-5xl md:text-7xl font-bold mb-6 gradient-text">
            Higgsfield: Vision of Sound
          </h1>
          <p className="text-lg text-text-secondary max-w-xl mx-auto leading-relaxed">
            Transform your audio into stunning visual experiences with AI-powered generation
          </p>
        </header>

        <main className="max-w-5xl mx-auto">
          {currentState === 'upload' && (
            <UploadSection onFileUpload={handleFileUpload} />
          )}
          
          {currentState === 'processing' && audioFile && (
            <ProcessingSection 
              audioFile={audioFile}
              isProcessing={isProcessing}
              onCancel={() => setCurrentState('upload')}
            />
          )}
          
          {currentState === 'result' && generationResult && (
            <ResultSection 
              generationResult={generationResult}
              onNewUpload={handleNewUpload}
            />
          )}
          
          {error && (
            <div className="card border-red-500/20 bg-red-950/10 text-center">
              <p className="text-red-400 mb-4">Error: {error}</p>
              <button 
                onClick={handleNewUpload}
                className="btn-secondary"
              >
                Try Again
              </button>
            </div>
          )}
        </main>
      </div>
    </div>
  )
}