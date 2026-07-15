import { useParams } from 'react-router-dom';

function CourseDetailPage({ courses }) {
  // Step 79: read the :courseId part of the current URL
  const { courseId } = useParams();

  // a Number, since URL params are always strings
  const course = courseId
    ? courses.find((c) => c.id === Number(courseId))
    : null;

  if (!course) {
    return <p>Course not found.</p>;
  }

  return (
    <main>
      <h2>{course.name}</h2>
      <p>Code: {course.code}</p>
      <p>Credits: {course.credits}</p>
      <p>Grade: {course.grade}</p>
    </main>
  );
}

export default CourseDetailPage;