import Link from 'next/link'

export default function Home() {
  return (
    <main className="flex flex-col items-center justify-center min-h-screen p-4 space-y-6">
      <h1 className="text-4xl font-bold">Welcome to IRMA</h1>
      <p className="max-w-xl text-center">
        IRMA is a collaborative platform designed for industrial teams to track performance, resolve problems, and improve operational efficiency. With intelligent ticketing, real-time KPIs, and AI-guided analysis, IRMA brings digital transformation to the shop floor.
      </p>
      <div className="flex space-x-4">
        <Link href="/login" className="px-4 py-2 bg-blue-500 text-white rounded">Login</Link>
        <Link href="/signup" className="px-4 py-2 bg-green-600 text-white rounded">Sign Up</Link>
      </div>
    </main>
  )
}
