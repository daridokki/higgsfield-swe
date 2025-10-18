'use client'

import { useState } from 'react'
import { Download, Plus, Music, Zap, DollarSign } from 'lucide-react'
import { GenerationResult } from '../lib/api'

interface ResultSectionProps {
  generationResult: GenerationResult
  onNewUpload: () => void
}

export default function ResultSection({ generationResult, onNewUpload }: ResultSectionProps) {
  const [showDownloadOverlay, setShowDownloadOverlay] = useState(false)

  const handleDownload = (videoUrl: string, index: number) => {
    // Create temporary link for download
    const link = document.createElement('a')
    link.href = videoUrl
    link.download = `sonic-canvas-video-${index + 1}.mp4`
    link.click()
  }

  const { music_analysis, video_urls, budget_used, budget_remaining } = generationResult

  return (
    <div className="mt-12">
      {/* Music Analysis Results */}
      <div className="bg-gray-800/50 rounded-xl p-6 mb-8">
        <h3 className="text-xl font-semibold mb-4 flex items-center gap-2">
          <Music className="w-5 h-5 text-purple-400" />
          Music Analysis
        </h3>
        <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
          <div className="text-center">
            <div className="text-2xl font-bold text-purple-400">{music_analysis.tempo}</div>
            <div className="text-sm text-gray-400">BPM</div>
          </div>
          <div className="text-center">
            <div className="text-2xl font-bold text-green-400">{(music_analysis.energy * 100).toFixed(0)}%</div>
            <div className="text-sm text-gray-400">Energy</div>
          </div>
          <div className="text-center">
            <div className="text-2xl font-bold text-blue-400 capitalize">{music_analysis.mood}</div>
            <div className="text-sm text-gray-400">Mood</div>
          </div>
          <div className="text-center">
            <div className="text-2xl font-bold text-yellow-400">{music_analysis.duration}s</div>
            <div className="text-sm text-gray-400">Duration</div>
          </div>
        </div>
      </div>

      {/* Budget Status */}
      <div className="bg-gray-800/50 rounded-xl p-6 mb-8">
        <h3 className="text-xl font-semibold mb-4 flex items-center gap-2">
          <DollarSign className="w-5 h-5 text-green-400" />
          Budget Status
        </h3>
        <div className="flex justify-between items-center">
          <div>
            <div className="text-sm text-gray-400">Used: ${budget_used.toFixed(2)}</div>
            <div className="text-sm text-gray-400">Remaining: ${budget_remaining.toFixed(2)}</div>
          </div>
          <div className="w-32 bg-gray-700 rounded-full h-2">
            <div 
              className="bg-green-500 h-2 rounded-full transition-all duration-300"
              style={{ width: `${(budget_used / (budget_used + budget_remaining)) * 100}%` }}
            ></div>
          </div>
        </div>
      </div>

      {/* Generated Videos */}
      <div className="space-y-6">
        <h3 className="text-xl font-semibold flex items-center gap-2">
          <Zap className="w-5 h-5 text-yellow-400" />
          Generated Videos ({video_urls.length})
        </h3>
        
        {video_urls.map((video, index) => (
          <div 
            key={index}
            className="visualizer rounded-xl overflow-hidden h-96 relative"
            onMouseEnter={() => setShowDownloadOverlay(true)}
            onMouseLeave={() => setShowDownloadOverlay(false)}
          >
            <video 
              src={video.url} 
              controls 
              className="w-full h-full object-cover"
            />
            <div 
              className={`absolute inset-0 flex items-center justify-center transition-opacity duration-300 bg-black/50 ${
                showDownloadOverlay ? 'opacity-100' : 'opacity-0'
              }`}
            >
              <button 
                onClick={() => handleDownload(video.url, index)}
                className="px-6 py-3 bg-white text-black rounded-full font-medium hover:bg-gray-200 transition flex items-center space-x-2"
              >
                <Download size={20} />
                <span>Download Video {index + 1}</span>
              </button>
            </div>
            <div className="absolute top-4 left-4 bg-black/70 px-3 py-1 rounded-full text-sm">
              {video.type === 'special' ? '✨ Special Moment' : `🎬 Scene ${index + 1}`}
            </div>
          </div>
        ))}
      </div>
      
      <div className="mt-8 text-center">
        <button 
          onClick={onNewUpload}
          className="px-6 py-2 border border-gray-600 rounded-full font-medium hover:bg-gray-800/50 transition flex items-center space-x-2 mx-auto"
        >
          <Plus size={20} />
          <span>Create Another</span>
        </button>
      </div>
    </div>
  )
}