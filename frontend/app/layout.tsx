import './globals.css'
import { ReactNode } from 'react'
import { Metadata } from 'next'

export const metadata: Metadata = {
  title: 'SonicCanvas | Audio to Visual Magic',
  description: 'Upload your audio and watch it transform into a mesmerizing visual experience',
}

export default function RootLayout({ children }: { children: ReactNode }) {
  return (
    <html lang="en">
      <body className="min-h-screen text-text-primary bg-background font-sans">
        {children}
      </body>
    </html>
  )
}