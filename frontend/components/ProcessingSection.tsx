'use client'

import { useState, useRef, useEffect } from 'react'
import { Play, X, Wand } from 'lucide-react'
import Visualizer from './Visualizer'

interface ProcessingSectionProps {
  audioFile: File
  isProcessing: boolean
  onCancel: () => void
}

export default function ProcessingSection({ audioFile, isProcessing, onCancel }: ProcessingSectionProps) {
  const [isPlaying, setIsPlaying] = useState(false)
  const [currentTime, setCurrentTime] = useState(0)
  const [duration, setDuration] = useState(0)
  const audioRef = useRef<HTMLAudioElement | null>(null)

  useEffect(() => {
    // Create audio element for playback
    const audioUrl = URL.createObjectURL(audioFile)
    audioRef.current = new Audio(audioUrl)
    
    audioRef.current.addEventListener('loadedmetadata', () => {
      setDuration(audioRef.current?.duration || 0)
    })
    
    audioRef.current.addEventListener('timeupdate', () => {
      setCurrentTime(audioRef.current?.currentTime || 0)
    })
    
    audioRef.current.addEventListener('ended', () => {
      setIsPlaying(false)
      setCurrentTime(0)
    })

    return () => {
      if (audioRef.current) {
        URL.revokeObjectURL(audioUrl)
      }
    }
  }, [audioFile])

  const togglePlayback = () => {
    if (!audioRef.current) return

    if (isPlaying) {
      audioRef.current.pause()
    } else {
      audioRef.current.play()
    }
    setIsPlaying(!isPlaying)
  }

  const formatTime = (seconds: number) => {
    const mins = Math.floor(seconds / 60)
    const secs = Math.floor(seconds % 60)
    return `${mins}:${secs.toString().padStart(2, '0')}`
  }

  const progress = duration > 0 ? (currentTime / duration) * 100 : 0

  return (
    <div className="max-w-4xl mx-auto">
      <Visualizer isPlaying={isPlaying} />
      
      <div className="card mt-8">
        <div className="flex items-center justify-between mb-6">
          <div>
            <h3 className="text-xl font-semibold text-text-primary">{audioFile.name}</h3>
            <p className="text-text-secondary">
              {formatTime(duration)} • {(audioFile.size / (1024 * 1024)).toFixed(2)} MB
            </p>
          </div>
          <button 
            onClick={onCancel}
            className="btn-secondary text-red-400 hover:text-red-300 hover:border-red-400 flex items-center gap-2"
          >
            <X size={18} />
            Cancel
          </button>
        </div>

        <div className="waveform mb-6">
          <div 
            className="waveform-progress" 
            style={{ width: `${progress}%` }}
          />
        </div>

        <div className="flex items-center justify-between">
          <div className="flex items-center space-x-6">
            <button 
              onClick={togglePlayback}
              className="w-14 h-14 bg-accent rounded-full flex items-center justify-center hover:bg-accent-hover transition group"
            >
              <Play 
                size={24} 
                className={`text-background ${isPlaying ? 'hidden' : 'block'}`} 
              />
              <div className={`text-background ${isPlaying ? 'block' : 'hidden'} flex space-x-1`}>
                <div className="w-1 h-6 bg-background animate-pulse"></div>
                <div className="w-1 h-6 bg-background animate-pulse" style={{animationDelay: '0.2s'}}></div>
                <div className="w-1 h-6 bg-background animate-pulse" style={{animationDelay: '0.4s'}}></div>
              </div>
            </button>
            <span className="text-text-primary font-medium">{formatTime(currentTime)}</span>
          </div>
          <span className="text-text-secondary">{formatTime(duration)}</span>
        </div>
      </div>

      <div className="mt-12 text-center">
        {isProcessing ? (
          <div className="flex flex-col items-center space-y-6">
            <div className="relative">
              <div className="w-16 h-16 border-4 border-border rounded-full animate-spin border-t-accent"></div>
              <div className="absolute inset-0 flex items-center justify-center">
                <Wand className="w-6 h-6 text-accent animate-pulse" />
              </div>
            </div>
            <div className="space-y-2">
              <h4 className="text-xl font-semibold text-text-primary">Generating your visual experience</h4>
              <p className="text-text-secondary">This may take a few moments...</p>
            </div>
            <div className="flex space-x-2">
              <div className="w-2 h-2 bg-accent rounded-full animate-bounce"></div>
              <div className="w-2 h-2 bg-accent rounded-full animate-bounce" style={{animationDelay: '0.1s'}}></div>
              <div className="w-2 h-2 bg-accent rounded-full animate-bounce" style={{animationDelay: '0.2s'}}></div>
            </div>
          </div>
        ) : (
          <button className="btn-primary text-lg px-8 py-4 flex items-center mx-auto space-x-3">
            <Wand size={20} />
            <span>Generate Visual Experience</span>
          </button>
        )}
      </div>
    </div>
  )
}