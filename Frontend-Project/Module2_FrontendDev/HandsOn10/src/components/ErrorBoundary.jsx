import { Component } from 'react'

class ErrorBoundary extends Component {
  constructor(props) {
    super(props)
    this.state = { hasError: false, errorMessage: '' }
  }

  static getDerivedStateFromError(error) {
    return { hasError: true, errorMessage: error.message }
  }

  
  componentDidCatch(error, errorInfo) {
    console.error('ErrorBoundary caught an error:', error, errorInfo)
  }

  render() {
    if (this.state.hasError) {
      return (
        <div className="error-fallback">
          <h2>Something went wrong.</h2>
          <p>{this.state.errorMessage}</p>
          <button onClick={() => window.location.reload()}>Reload page</button>
        </div>
      )
    }
    return this.props.children
  }
}

export default ErrorBoundary