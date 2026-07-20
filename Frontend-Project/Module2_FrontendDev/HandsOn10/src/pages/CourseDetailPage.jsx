import { useParams } from 'react-router-dom'
import { useSelector } from 'react-redux'
import { selectCourses } from '../redux/selectors'

function CourseDetailPage() {
  const { courseId } = useParams()
  const courses = useSelector(selectCourses)

  const course = courseId ? courses.find((c) => c.id === Number(courseId)) : null

  if (!course) {
    return <p>Course not found.</p>
  }

  return (
    <main>
      <h2>{course.name}</h2>
      <p>Code: {course.code}</p>
      <p>Credits: {course.credits}</p>
      <p>Grade: {course.grade}</p>
    </main>
  )
}

export default CourseDetailPage