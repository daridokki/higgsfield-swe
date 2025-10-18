'use client'

import { useState } from 'react'
import UploadSection from '../components/UploadSection'
import ProcessingSection from '../components/ProcessingSection'
import ResultSection from '../components/ResultSection'

type AppState = 'upload' | 'processing' | 'result'

export default function Home() {
  const [currentState, setCurrentState] = useState<AppState>('upload')
  const [audioFile, setAudioFile] = useState<File | null>(null)
  const [resultVideoUrl, setResultVideoUrl] = useState<string>('')

  const handleFileUpload = (file: File) => {
    setAudioFile(file)
    setCurrentState('processing')
    
    // Simulate processing and generation
    setTimeout(() => {
      setResultVideoUrl('https://example.com/generated-video.mp4')
      setCurrentState('result')
    }, 3000)
  }

  const handleNewUpload = () => {
    setAudioFile(null)
    setResultVideoUrl('')
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
            onCancel={() => setCurrentState('upload')}
          />
        )}
        
        {currentState === 'result' && resultVideoUrl && (
          <ResultSection 
            videoUrl={resultVideoUrl}
            onNewUpload={handleNewUpload}
          />
        )}
      </main>
    </div>
  )
}