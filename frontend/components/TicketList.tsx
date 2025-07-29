'use client'
import useSWR from 'swr'

const fetcher = (url: string) => fetch(url).then(res => res.json())

export default function TicketList() {
  const { data, error } = useSWR('/api/tickets', fetcher)

  if (error) return <div>Failed to load</div>
  if (!data) return <div>Loading...</div>

  return (
    <ul>
      {data.map((ticket: any) => (
        <li key={ticket.id}>{ticket.title} - {ticket.status}</li>
      ))}
    </ul>
  )
}
