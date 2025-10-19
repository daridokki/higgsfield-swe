// Configuration for the frontend application
export const config = {
  // Backend API URL - can be overridden by environment variables
  apiUrl: process.env.NEXT_PUBLIC_API_URL || 'https://higgsfield-visionofsound.up.railway.app',
  
  // File upload settings
  maxFileSize: 50 * 1024 * 1024, // 50MB
  allowedAudioTypes: ['audio/mpeg', 'audio/wav', 'audio/mp4', 'audio/ogg'],
  
  // UI settings
  defaultTimeout: 30000, // 30 seconds
  pollingInterval: 1000, // 1 second
}
