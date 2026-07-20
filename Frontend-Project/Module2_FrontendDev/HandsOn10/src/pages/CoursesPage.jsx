import { useEffect, useState } from 'react'
import { useDispatch, useSelector } from 'react-redux'
import CourseCard from '../components/CourseCard'
import { fetchAllCourses } from '../redux/enrollmentSlice'
import { selectCourses, selectCoursesLoading, selectCoursesError } from '../redux/selectors'

function CoursesPage() {
  const dispatch = useDispatch()
  const courses = useSelector(selectCourses)
  const loading = useSelector(selectCoursesLoading)
  const error = useSelector(selectCoursesError)

  const [searchTerm, setSearchTerm] = useState('')

 
  useEffect(() => {
    dispatch(fetchAllCourses())
  }, [dispatch])

  const filteredCourses = courses.filter((course) =>
    course.name.toLowerCase().includes(searchTerm.toLowerCase())
  )

  return (
    <main>
      <h2>Available Courses</h2>

      {loading && <p>Loading...</p>}
      {error && <p className="error-message">Something went wrong: {error}</p>}

      {!loading && !error && (
        <>
          <input
            type="text"
            placeholder="Search courses..."
            value={searchTerm}
            onChange={(event) => setSearchTerm(event.target.value)}
          />

          <div className="course-grid">
            {filteredCourses.map((course) => (
              <CourseCard
                key={course.id}
                id={course.id}
                name={course.name}
                code={course.code}
                credits={course.credits}
                grade={course.grade}
              />
            ))}
          </div>
        </>
      )}
    </main>
  )
}

export default CoursesPage