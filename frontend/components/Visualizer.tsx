'use client'

import { useEffect, useRef } from 'react'

interface VisualizerProps {
  isPlaying: boolean
}

export default function Visualizer({ isPlaying }: VisualizerProps) {
  const canvasRef = useRef<HTMLCanvasElement>(null)
  const animationRef = useRef<number | undefined>(undefined)

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
      ctx.fillStyle = '#111111'
      ctx.fillRect(0, 0, canvas.width, canvas.height)

      if (isPlaying) {
        // Create gradient with higgsfield.ai accent color
        const gradient = ctx.createLinearGradient(0, 0, canvas.width, 0)
        gradient.addColorStop(0, 'rgb(209, 254, 23)')
        gradient.addColorStop(0.5, 'rgba(209, 254, 23, 0.8)')
        gradient.addColorStop(1, 'rgba(209, 254, 23, 0.6)')

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
    <div className="visualizer h-80">
      <canvas 
        ref={canvasRef} 
        className="w-full h-full"
      />
    </div>
  )
}