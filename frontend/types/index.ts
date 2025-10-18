export interface MusicAnalysis {
    tempo: number;
    energy: number;
    mood: string;
    beats: number[];
    structure: {
      sections: Array<{
        start: number;
        end: number;
        intensity: number;
      }>;
      intensity_changes: number[];
    };
    key_features: {
      spectral_centroid: number;
      zero_crossing_rate: number;
      spectral_rolloff: number;
    };
  }
  
  export interface GeneratedScene {
    imageUrl: string;
    videoUrl: string;
    prompt: string;
    duration: number;
    transition: string;
  }
  
  export interface VideoGenerationState {
    currentStep: 'upload' | 'analyzing' | 'generating' | 'complete';
    musicFile: File | null;
    analysis: MusicAnalysis | null;
    progress: {
      currentScene: number;
      totalScenes: number;
      status: string;
    };
    result: {
      videoUrl: string;
      scenes: GeneratedScene[];
    } | null;
  }