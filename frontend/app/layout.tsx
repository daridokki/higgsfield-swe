import './globals.css'
import React from 'react'
import { ReactNode } from 'react'
import { Metadata } from 'next'

export const metadata: Metadata = {
  title: 'Higgsfield: Vision of Sound | Audio to Visual Magic',
  description: 'Upload your audio and watch it transform into a mesmerizing visual experience powered by Higgsfield AI',
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