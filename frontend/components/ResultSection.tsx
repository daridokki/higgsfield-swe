'use client'

import React, { useState } from 'react'
import { Download, Plus, Music, Zap } from 'lucide-react'
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

  const { music_analysis, video_urls } = generationResult

  // DEBUG: Log the received data
  console.log('ResultSection received:', generationResult)
  console.log('Video URLs:', video_urls)
  console.log('Number of videos:', video_urls?.length || 0)

  return (
    <div className="max-w-6xl mx-auto">
      {/* Music Analysis Results */}
      <div className="card mb-8">
        <h3 className="text-2xl font-semibold mb-6 flex items-center gap-3">
          <Music className="w-6 h-6 text-accent" />
          Music Analysis
        </h3>
        <div className="grid grid-cols-2 md:grid-cols-4 gap-6">
          <div className="text-center p-4 bg-surface rounded-lg border border-border">
            <div className="text-3xl font-bold text-accent mb-2">{Math.round(music_analysis.tempo)}</div>
            <div className="text-sm text-text-secondary">BPM</div>
          </div>
          <div className="text-center p-4 bg-surface rounded-lg border border-border">
            <div className="text-3xl font-bold text-accent mb-2">{Math.round(music_analysis.energy * 100)}%</div>
            <div className="text-sm text-text-secondary">Energy</div>
          </div>
          <div className="text-center p-4 bg-surface rounded-lg border border-border">
            <div className="text-3xl font-bold text-accent mb-2 capitalize">{music_analysis.mood}</div>
            <div className="text-sm text-text-secondary">Mood</div>
          </div>
          <div className="text-center p-4 bg-surface rounded-lg border border-border">
            <div className="text-3xl font-bold text-accent mb-2">{Math.round(music_analysis.duration)}s</div>
            <div className="text-sm text-text-secondary">Duration</div>
          </div>
        </div>
      </div>


      {/* Generated Videos */}
      <div className="space-y-8">
        <h3 className="text-2xl font-semibold flex items-center gap-3">
          <Zap className="w-6 h-6 text-accent" />
          Generated Videos ({video_urls.length})
        </h3>
        
        <div className="grid grid-cols-1 gap-8">
          {video_urls.map((video, index) => (
            <div 
              key={index}
              className="visualizer h-96 relative group"
              onMouseEnter={() => setShowDownloadOverlay(true)}
              onMouseLeave={() => setShowDownloadOverlay(false)}
            >
              <video 
                src={video.url} 
                controls 
                className="w-full h-full object-cover"
              />
              <div 
                className={`absolute inset-0 flex items-center justify-center transition-opacity duration-300 bg-black/60 ${
                  showDownloadOverlay ? 'opacity-100' : 'opacity-0'
                }`}
              >
                <button 
                  onClick={() => handleDownload(video.url, index)}
                  className="btn-primary text-lg px-6 py-3 flex items-center space-x-3"
                >
                  <Download size={20} />
                  <span>Download Video {index + 1}</span>
                </button>
              </div>
              <div className="absolute top-4 left-4 bg-background/90 px-4 py-2 rounded-lg text-sm font-medium border border-border">
                {video.type === 'special' ? '✨ Special Moment' : `🎬 Scene ${index + 1}`}
              </div>
            </div>
          ))}
        </div>
      </div>
      
      <div className="mt-12 text-center">
        <button 
          onClick={onNewUpload}
          className="btn-secondary text-lg px-8 py-4 flex items-center space-x-3 mx-auto"
        >
          <Plus size={20} />
          <span>Create Another</span>
        </button>
      </div>
    </div>
  )
}