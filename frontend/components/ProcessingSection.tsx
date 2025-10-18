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
    <div>
      <Visualizer isPlaying={isPlaying} />
      
      <div className="flex items-center justify-between mb-4">
        <div>
          <h3 className="text-lg font-medium">{audioFile.name}</h3>
          <p className="text-sm text-gray-400">
            {formatTime(duration)} • {(audioFile.size / (1024 * 1024)).toFixed(2)} MB
          </p>
        </div>
        <button 
          onClick={onCancel}
          className="text-red-400 hover:text-red-300 transition flex items-center gap-2"
        >
          <X size={20} />
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
        <div className="flex space-x-4">
          <button 
            onClick={togglePlayback}
            className="w-12 h-12 bg-indigo-600 rounded-full flex items-center justify-center hover:bg-indigo-700 transition"
          >
            <Play 
              size={20} 
              className={isPlaying ? 'hidden' : 'block'} 
            />
            <div className={isPlaying ? 'block' : 'hidden'}>
              <div className="w-2 h-4 bg-white mx-0.5 inline-block animate-pulse"></div>
              <div className="w-2 h-4 bg-white mx-0.5 inline-block animate-pulse" style={{animationDelay: '0.2s'}}></div>
              <div className="w-2 h-4 bg-white mx-0.5 inline-block animate-pulse" style={{animationDelay: '0.4s'}}></div>
            </div>
          </button>
          <span className="flex items-center">{formatTime(currentTime)}</span>
        </div>
        <span className="text-gray-400">{formatTime(duration)}</span>
      </div>

      <div className="mt-8 text-center">
        {isProcessing ? (
          <div className="flex flex-col items-center space-y-4">
            <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-purple-600"></div>
            <p className="text-gray-400">Generating your visual experience...</p>
            <div className="flex space-x-2">
              <div className="w-2 h-2 bg-purple-600 rounded-full animate-bounce"></div>
              <div className="w-2 h-2 bg-purple-600 rounded-full animate-bounce" style={{animationDelay: '0.1s'}}></div>
              <div className="w-2 h-2 bg-purple-600 rounded-full animate-bounce" style={{animationDelay: '0.2s'}}></div>
            </div>
          </div>
        ) : (
          <button className="px-8 py-3 bg-gradient-to-r from-purple-600 to-pink-600 rounded-full font-medium hover:opacity-90 transition-all flex items-center mx-auto space-x-2">
            <Wand size={20} />
            <span>Generate Visual Experience</span>
          </button>
        )}
      </div>
    </div>
  )
}