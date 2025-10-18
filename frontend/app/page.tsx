'use client'

import { useState } from 'react'
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
      // First analyze the music
      const analysisResponse = await apiService.analyzeMusic(file)
      console.log('Music analysis:', analysisResponse.analysis)
      
      // Then generate the video
      const videoResponse = await apiService.generateVideo(file)
      console.log('Video generation result:', videoResponse.result)
      
      setGenerationResult(videoResponse.result)
      setCurrentState('result')
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
    <div className="container mx-auto px-4 py-12">
      <header className="text-center mb-16">
        <h1 className="text-4xl md:text-6xl font-bold mb-4 bg-clip-text text-transparent bg-gradient-to-r from-purple-400 via-pink-500 to-blue-500">
          SonicCanvas
        </h1>
        <p className="text-xl text-gray-300 max-w-2xl mx-auto">
          Upload your audio and watch it transform into a mesmerizing visual experience ✨
        </p>
      </header>

      <main className="max-w-4xl mx-auto">
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
          <div className="bg-red-900/20 border border-red-500/50 rounded-lg p-4 text-center">
            <p className="text-red-400">Error: {error}</p>
            <button 
              onClick={handleNewUpload}
              className="mt-2 px-4 py-2 bg-red-600 rounded-lg hover:bg-red-700 transition"
            >
              Try Again
            </button>
          </div>
        )}
      </main>
    </div>
  )
}