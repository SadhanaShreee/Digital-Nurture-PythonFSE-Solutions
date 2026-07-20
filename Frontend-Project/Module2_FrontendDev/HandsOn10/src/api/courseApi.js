import apiClient from './apiClient'

export async function getAllCourses() {
  const posts = await apiClient.get('/posts?_limit=5')
  return posts.map((post, index) => ({
    id: post.id,
    name: post.title,
    code: `CS10${index + 1}`,
    credits: 3 + (index % 2),
    grade: 'A'
  }))
}

export async function getCourseById(id) {
  const post = await apiClient.get(`/posts/${id}`)
  return {
    id: post.id,
    name: post.title,
    code: `CS10${post.id}`,
    credits: 3 + (post.id % 2),
    grade: 'A'
  }
}

export async function enrollStudent(studentId, courseId) {
  return apiClient.post('/posts', { studentId, courseId })
}