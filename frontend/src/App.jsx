import { useEffect, useState } from 'react'
import './App.css'

function App() {
  const [count, setCount] = useState(0)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState('')

  const API_BASE = 'http://127.0.0.1:5000/api/counter'

  const fetchCount = async () => {
    try {
      setError('')
      const response = await fetch(API_BASE)
      if (!response.ok) {
        throw new Error('Failed to load counter')
      }
      const data = await response.json()
      setCount(data.count)
    } catch (err) {
      setError('Could not connect to Flask backend')
      console.error(err)
    } finally {
      setLoading(false)
    }
  }

  const updateCounter = async (endpoint) => {
    try {
      setError('')
      const response = await fetch(`${API_BASE}/${endpoint}`, {
        method: 'POST',
      })

      if (!response.ok) {
        throw new Error(`Failed to ${endpoint} counter`)
      }

      const data = await response.json()
      setCount(data.count)
    } catch (err) {
      setError('Could not update counter')
      console.error(err)
    }
  }

  useEffect(() => {
    fetchCount()
  }, [])

  return (
    <div className="page">
      <div className="container">
        <h1 className="title">Counter App</h1>

        {loading ? (
          <div className="count">...</div>
        ) : (
          <div className="count">{count}</div>
        )}

        {error && <p className="error">{error}</p>}

        <div className="buttons">
          <button
            className="decrement"
            onClick={() => updateCounter('decrement')}
          >
            -
          </button>

          <button
            className="reset"
            onClick={() => updateCounter('reset')}
          >
            Reset
          </button>

          <button
            className="increment"
            onClick={() => updateCounter('increment')}
          >
            +
          </button>
        </div>
      </div>
    </div>
  )
}

export default App