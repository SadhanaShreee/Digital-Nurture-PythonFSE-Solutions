import axios from 'axios'
const apiClient = axios.create({
  baseURL: 'https://jsonplaceholder.typicode.com',
  timeout: 5000,
  headers: {
    'Content-Type': 'application/json'
  }
})


apiClient.interceptors.request.use((config) => {
  config.headers.Authorization = 'Bearer mock-token-12345'
  return config
})

/* response interceptor — runs on EVERY response.

   (a) On success: return response.data directly, not the whole
       Axios response object.

   (b) On failure: catch whatever Axios throws, and re-throw a
       clean, STANDARDISED Error */
apiClient.interceptors.response.use(
  (response) => response.data,
  (error) => {
    const statusCode = error.response ? error.response.status : null
    const message = error.response
      ? `Request failed with status ${statusCode}`
      : 'Network error — please check your connection'

    const standardisedError = new Error(message)
    standardisedError.statusCode = statusCode

    return Promise.reject(standardisedError)
  }
)

export default apiClient