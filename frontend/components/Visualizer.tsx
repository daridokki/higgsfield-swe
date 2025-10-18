'use client'

import { useEffect, useRef } from 'react'

interface VisualizerProps {
  isPlaying: boolean
}

export default function Visualizer({ isPlaying }: VisualizerProps) {
  const canvasRef = useRef<HTMLCanvasElement>(null)
  const animationRef = useRef<number>()

  useEffect(() => {
    const canvas = canvasRef.current
    if (!canvas) return

    const ctx = canvas.getContext('2d')
    if (!ctx) return

    // Set canvas size
    canvas.width = canvas.offsetWidth
    canvas.height = canvas.offsetHeight

    const drawVisualizer = () => {
      if (!ctx || !canvas) return

      // Clear canvas
      ctx.fillStyle = 'rgba(0, 0, 0, 0.1)'
      ctx.fillRect(0, 0, canvas.width, canvas.height)

      if (isPlaying) {
        // Create gradient
        const gradient = ctx.createLinearGradient(0, 0, canvas.width, 0)
        gradient.addColorStop(0, '#7f5af0')
        gradient.addColorStop(1, '#2cb67d')

        // Draw animated bars
        const barCount = 50
        const barWidth = canvas.width / barCount

        for (let i = 0; i < barCount; i++) {
          const height = Math.random() * canvas.height * 0.8
          const x = i * barWidth
          const y = (canvas.height - height) / 2

          ctx.fillStyle = gradient
          ctx.fillRect(x, y, barWidth - 2, height)
        }
      }

      animationRef.current = requestAnimationFrame(drawVisualizer)
    }

    drawVisualizer()

    return () => {
      if (animationRef.current) {
        cancelAnimationFrame(animationRef.current)
      }
    }
  }, [isPlaying])

  return (
    <div className="visualizer rounded-xl overflow-hidden mb-8 h-64">
      <canvas 
        ref={canvasRef} 
        className="w-full h-full"
      />
    </div>
  )
}