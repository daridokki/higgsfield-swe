// API service for communicating with the backend
import { config } from './config'

const API_BASE_URL = config.apiUrl

// Debug logging
console.log('API_BASE_URL:', API_BASE_URL)
console.log('NEXT_PUBLIC_API_URL:', process.env.NEXT_PUBLIC_API_URL)

// Import types from the main types file
import { VideoResult, MusicAnalysis, GenerationResult } from '../types'

export interface ApiResponse<T> {
  status: 'success' | 'error'
  message: string
  data?: T
  error?: string
}

class ApiService {
  private async request<T>(
    endpoint: string, 
    options: RequestInit = {}
  ): Promise<ApiResponse<T>> {
    try {
      const response = await fetch(`${API_BASE_URL}${endpoint}`, {
        headers: {
          'Content-Type': 'application/json',
          ...options.headers,
        },
        ...options,
      })

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`)
      }

      const data = await response.json()
      return {
        status: 'success',
        message: data.message || 'Request successful',
        data: data
      }
    } catch (error) {
      return {
        status: 'error',
        message: 'Request failed',
        error: error instanceof Error ? error.message : 'Unknown error'
      }
    }
  }

  async checkHealth(): Promise<ApiResponse<any>> {
    try {
      const response = await fetch(`${API_BASE_URL}/health`, {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
        },
        mode: 'cors',
      })

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`)
      }

      const data = await response.json()
      return {
        status: 'success',
        message: data.message || 'Health check successful',
        data: data
      }
    } catch (error) {
      return {
        status: 'error',
        message: 'Health check failed',
        error: error instanceof Error ? error.message : 'Unknown error'
      }
    }
  }


  async analyzeMusic(file: File): Promise<ApiResponse<{ analysis: MusicAnalysis }>> {
    const formData = new FormData()
    formData.append('file', file)
    
    try {
      console.log('Sending request to:', `${API_BASE_URL}/analyze-music`)
      const response = await fetch(`${API_BASE_URL}/analyze-music`, {
        method: 'POST',
        body: formData,
      })

      console.log('Response status:', response.status)
      
      if (!response.ok) {
        const errorText = await response.text()
        console.error('API Error:', errorText)
        throw new Error(`HTTP error! status: ${response.status} - ${errorText}`)
      }

      const data = await response.json()
      console.log('Analysis response:', data)
      return {
        status: 'success',
        message: data.message || 'Analysis completed',
        data: { analysis: data.analysis }
      }
    } catch (error) {
      console.error('Analysis error:', error)
      return {
        status: 'error',
        message: 'Analysis failed',
        error: error instanceof Error ? error.message : 'Unknown error'
      }
    }
  }

  async generateVideo(file: File): Promise<ApiResponse<VideoResult>> {
    const formData = new FormData()
    formData.append('file', file)
    
    try {
      console.log('Sending video generation request to:', `${API_BASE_URL}/generate-video`)
      const response = await fetch(`${API_BASE_URL}/generate-video`, {
        method: 'POST',
        body: formData,
      })

      console.log('Video generation response status:', response.status)
      
      if (!response.ok) {
        const errorText = await response.text()
        console.error('Video generation API Error:', errorText)
        throw new Error(`HTTP error! status: ${response.status} - ${errorText}`)
      }

      const data = await response.json()
      console.log('Video generation response:', data)
      return {
        status: 'success',
        message: data.message || 'Video generation completed',
        data: data.result
      }
    } catch (error) {
      console.error('Video generation error:', error)
      return {
        status: 'error',
        message: 'Video generation failed',
        error: error instanceof Error ? error.message : 'Unknown error'
      }
    }
  }
}

export const apiService = new ApiService()

// Re-export types for convenience
export type { GenerationResult, VideoResult, MusicAnalysis }
