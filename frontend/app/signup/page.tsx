"use client"

import { useState } from 'react'
import Link from 'next/link'

export default function SignUpPage() {
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const [confirm, setConfirm] = useState('')

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault()
    if (password !== confirm) {
      alert('Passwords do not match')
      return
    }
    // TODO: integrate sign-up logic
    alert(`Sign up with ${email}`)
  }

  const handleGoogle = () => {
    // TODO: integrate Google sign-up
    alert('Google Sign-Up')
  }

  return (
    <main className="flex flex-col items-center justify-center min-h-screen p-4 space-y-4">
      <h1 className="text-2xl font-bold">Sign Up</h1>
      <button onClick={handleGoogle} className="px-4 py-2 bg-red-500 text-white rounded w-60">Sign up with Google</button>
      <form onSubmit={handleSubmit} className="flex flex-col space-y-2 w-60">
        <input className="border p-2 rounded" type="email" value={email} onChange={e => setEmail(e.target.value)} placeholder="Email" required />
        <input className="border p-2 rounded" type="password" value={password} onChange={e => setPassword(e.target.value)} placeholder="Password" required />
        <input className="border p-2 rounded" type="password" value={confirm} onChange={e => setConfirm(e.target.value)} placeholder="Confirm Password" required />
        <button type="submit" className="px-4 py-2 bg-green-600 text-white rounded">Create Account</button>
      </form>
      <p>Already have an account? <Link href="/login" className="text-blue-600">Login</Link></p>
    </main>
  )
}
