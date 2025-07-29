"use client"

import { useState } from 'react'
import Link from 'next/link'

export default function LoginPage() {
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault()
    // TODO: integrate email/password login
    alert(`Login with ${email}`)
  }

  const handleGoogle = () => {
    // TODO: integrate Google sign-in
    alert('Google Sign-In')
  }

  return (
    <main className="flex flex-col items-center justify-center min-h-screen p-4 space-y-4">
      <h1 className="text-2xl font-bold">Login</h1>
      <button onClick={handleGoogle} className="px-4 py-2 bg-red-500 text-white rounded w-60">Sign in with Google</button>
      <form onSubmit={handleSubmit} className="flex flex-col space-y-2 w-60">
        <input className="border p-2 rounded" type="email" value={email} onChange={e => setEmail(e.target.value)} placeholder="Email" required />
        <input className="border p-2 rounded" type="password" value={password} onChange={e => setPassword(e.target.value)} placeholder="Password" required />
        <button type="submit" className="px-4 py-2 bg-blue-500 text-white rounded">Login</button>
      </form>
      <p>Don't have an account? <Link href="/signup" className="text-blue-600">Sign up</Link></p>
    </main>
  )
}
