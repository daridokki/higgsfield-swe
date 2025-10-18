'use client'

import { useState } from 'react'
import { Download, Plus } from 'lucide-react'
interface ResultSectionProps {
  videoUrl: string
  onNewUpload: () => void
}

export default function ResultSection({ videoUrl, onNewUpload }: ResultSectionProps) {
  const [showDownloadOverlay, setShowDownloadOverlay] = useState(false)

  const handleDownload = () => {
    // Create temporary link for download
    const link = document.createElement('a')
    link.href = videoUrl
    link.download = 'sonic-canvas-video.mp4'
    link.click()
  }

  return (
    <div className="mt-12 text-center">
      <div 
        className="visualizer rounded-xl overflow-hidden mb-8 h-96 relative"
        onMouseEnter={() => setShowDownloadOverlay(true)}
        onMouseLeave={() => setShowDownloadOverlay(false)}
      >
        <video 
          src={videoUrl} 
          controls 
          className="w-full h-full object-cover"
        />
        <div 
          className={`absolute inset-0 flex items-center justify-center transition-opacity duration-300 bg-black/50 ${
            showDownloadOverlay ? 'opacity-100' : 'opacity-0'
          }`}
        >
          <button 
            onClick={handleDownload}
            className="px-6 py-3 bg-white text-black rounded-full font-medium hover:bg-gray-200 transition flex items-center space-x-2"
          >
            <Download size={20} />
            <span>Download Video</span>
          </button>
        </div>
      </div>
      
      <button 
        onClick={onNewUpload}
        className="px-6 py-2 border border-gray-600 rounded-full font-medium hover:bg-gray-800/50 transition flex items-center space-x-2 mx-auto"
      >
        <Plus size={20} />
        <span>Create Another</span>
      </button>
    </div>
  )
}