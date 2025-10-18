import './globals.css'
import { ReactNode } from 'react'

export const metadata = {
  title: 'SonicCanvas | Audio to Visual Magic',
  description: 'Upload your audio and watch it transform into a mesmerizing visual experience',
}

export default function RootLayout({ children }: { children: ReactNode }) {
  return (
    <html lang="en">
      <body className="min-h-screen text-white bg-gradient-to-br from-[#1a1a2e] to-[#16213e]">
        {children}
      </body>
    </html>
  )
}