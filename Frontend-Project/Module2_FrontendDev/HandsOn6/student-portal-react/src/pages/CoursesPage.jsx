import { useState } from 'react';
import CourseCard from '../components/CourseCard';

// This page still receives the course LIST as props from App.jsx -
// only enrollment moved to Context, not the course data itself.
function CoursesPage({ courses, loading, error }) {
  const [searchTerm, setSearchTerm] = useState('');

  const filteredCourses = courses.filter((course) =>
    course.name.toLowerCase().includes(searchTerm.toLowerCase())
  );

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
  );
}

export default CoursesPage;