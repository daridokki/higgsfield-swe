'use client'

import { useCallback, useState } from 'react'
import { Upload } from 'lucide-react'


interface UploadSectionProps {
  onFileUpload: (file: File) => void
}

export default function UploadSection({ onFileUpload }: UploadSectionProps) {
  const [isDragging, setIsDragging] = useState(false)

  const handleFileSelect = useCallback((file: File) => {
    if (file && file.type.startsWith('audio/')) {
      onFileUpload(file)
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
    <div 
      className={`dropzone ${isDragging ? 'active' : ''}`}
      onDrop={onDrop}
      onDragOver={onDragOver}
      onDragLeave={onDragLeave}
    >
      <div className="flex flex-col items-center justify-center space-y-4">
        <div className="bg-indigo-900/50 p-6 rounded-full">
          <Upload className="w-12 h-12 text-indigo-400" />
        </div>
        <h2 className="text-2xl font-semibold">Drop your audio file here</h2>
        <p className="text-gray-400">Or click to browse your files</p>
        
        <input 
          type="file" 
          id="audio-upload"
          accept="audio/*"
          className="hidden"
          onChange={onFileInputChange}
        />
        
        <button 
          onClick={() => document.getElementById('audio-upload')?.click()}
          className="mt-4 px-6 py-3 bg-gradient-to-r from-indigo-600 to-purple-600 rounded-full font-medium hover:opacity-90 transition-all pulse"
        >
          Select File
        </button>
      </div>
    </div>
  )
}