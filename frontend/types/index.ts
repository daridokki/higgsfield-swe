// Type definitions for the application

export interface MusicAnalysis {
  tempo: number
  energy: number
  mood: string
  duration: number
  total_beats?: number
}

export interface VideoUrl {
  url: string
  type: 'scene' | 'special'
}

export interface VideoResult {
  music_analysis: MusicAnalysis
  video_urls: VideoUrl[]
}


// This is the same as VideoResult but with a different name for clarity
export type GenerationResult = VideoResult
