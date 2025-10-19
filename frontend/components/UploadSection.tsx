'use client'

import React, { useCallback, useState } from 'react'
import { Upload } from 'lucide-react'

interface UploadSectionProps {
  onFileUpload: (file: File) => void
}

export default function UploadSection({ onFileUpload }: UploadSectionProps) {
  const [isDragging, setIsDragging] = useState(false)

  const validateFile = (file: File): { valid: boolean; error?: string } => {
    // Check file type
    const allowedTypes = ['audio/mpeg', 'audio/wav', 'audio/mp4', 'audio/ogg', 'audio/x-m4a']
    if (!allowedTypes.includes(file.type) && !file.name.match(/\.(mp3|wav|m4a|ogg)$/i)) {
      return { valid: false, error: 'Please upload an audio file (MP3, WAV, M4A, or OGG)' }
    }
    
    // Check file size (50MB limit)
    const maxSize = 50 * 1024 * 1024 // 50MB
    if (file.size > maxSize) {
      return { valid: false, error: 'File too large. Maximum size is 50MB' }
    }
    
    // Check minimum size (1KB)
    if (file.size < 1024) {
      return { valid: false, error: 'File too small. Please upload a valid audio file' }
    }
    
    return { valid: true }
  }

  const handleFileSelect = useCallback((file: File) => {
    const validation = validateFile(file)
    if (validation.valid) {
      onFileUpload(file)
    } else {
      alert(validation.error)
    }
  }, [onFileUpload])

  const onDrop = useCallback((e: React.DragEvent) => {
    e.preventDefault()
    setIsDragging(false)
    const files = e.dataTransfer.files
    if (files.length > 0) {
      handleFileSelect(files[0])
    }
  }, [handleFileSelect])

  const onDragOver = useCallback((e: React.DragEvent) => {
    e.preventDefault()
    setIsDragging(true)
  }, [])

  const onDragLeave = useCallback((e: React.DragEvent) => {
    e.preventDefault()
    setIsDragging(false)
  }, [])

  const onFileInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const files = e.target.files
    if (files && files.length > 0) {
      handleFileSelect(files[0])
    }
  }

  return (
    <div className="flex flex-col items-center justify-center">
      <div 
        className={`dropzone ${isDragging ? 'active' : ''} w-full max-w-2xl`}
        onDrop={onDrop}
        onDragOver={onDragOver}
        onDragLeave={onDragLeave}
      >
        <div className="flex flex-col items-center justify-center space-y-6">
          <div className="p-8 rounded-full bg-surface border border-border">
            <Upload size={64} style={{ color: 'var(--accent)' }} />
          </div>
          <div className="text-center space-y-3">
            <h2 className="text-2xl font-semibold text-text-primary">
              Drop your audio file here
            </h2>
            <p className="text-text-secondary">
              Supports MP3, WAV, M4A, and OGG formats
            </p>
          </div>
          
          <input 
            type="file" 
            id="audio-upload"
            accept="audio/*"
            className="hidden"
            onChange={onFileInputChange}
          />
          
          <div className="space-y-4">
            <button 
              onClick={() => document.getElementById('audio-upload')?.click()}
              className="btn-primary text-lg px-8 py-4"
            >
              Select File
            </button>
            
          </div>
        </div>
      </div>
      
      <div className="mt-12 grid grid-cols-1 md:grid-cols-3 gap-6 max-w-4xl w-full">
        <div className="card text-center">
          <div className="w-12 h-12 bg-accent/10 rounded-lg flex items-center justify-center mx-auto mb-4">
            <Upload size={24} style={{ color: 'var(--accent)' }} />
          </div>
          <h3 className="font-semibold mb-2">Upload</h3>
          <p className="text-text-secondary text-sm">
            Drag and drop or select your audio file
          </p>
        </div>
        
        <div className="card text-center">
          <div className="w-12 h-12 bg-accent/10 rounded-lg flex items-center justify-center mx-auto mb-4">
            <svg className="w-6 h-6 text-accent" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" />
            </svg>
          </div>
          <h3 className="font-semibold mb-2">Analyze</h3>
          <p className="text-text-secondary text-sm">
            AI analyzes tempo, mood, and energy
          </p>
        </div>
        
        <div className="card text-center">
          <div className="w-12 h-12 bg-accent/10 rounded-lg flex items-center justify-center mx-auto mb-4">
            <svg className="w-6 h-6 text-accent" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M15 10l4.553-2.276A1 1 0 0121 8.618v6.764a1 1 0 01-1.447.894L15 14M5 18h8a2 2 0 002-2V8a2 2 0 00-2-2H5a2 2 0 00-2 2v8a2 2 0 002 2z" />
            </svg>
          </div>
          <h3 className="font-semibold mb-2">Generate</h3>
          <p className="text-text-secondary text-sm">
            Create stunning visual experiences
          </p>
        </div>
      </div>
    </div>
  )
}