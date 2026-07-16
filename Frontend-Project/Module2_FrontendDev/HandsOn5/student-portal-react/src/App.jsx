import { useState, useEffect } from 'react';
import Header from './components/Header';
import Footer from './components/Footer';
import CourseCard from './components/CourseCard';
import StudentProfile from './components/StudentProfile';

function App() {
  // Step 71: courses now starts EMPTY — it gets filled in by the fetch below
  const [courses, setCourses] = useState([]);

  const [searchTerm, setSearchTerm] = useState('');
  const [enrolledCourses, setEnrolledCourses] = useState([]);

  // Step 72: true while we're waiting on the fetch
  const [loading, setLoading] = useState(true);

  // Step 73: holds an error message if the fetch fails, otherwise null
  const [error, setError] = useState(null);

 
  // fetch the courses from the API when the component mounts
  useEffect(() => {
    async function loadCourses() {
      try {
        setLoading(true);
        setError(null);

        const response = await fetch('https://jsonplaceholder.typicode.com/posts');
        if (!response.ok) {
          throw new Error(`Request failed with status ${response.status}`);
        }

        const posts = await response.json();

        // Map the first 5 posts into course-shaped objects, since
        // JSONPlaceholder doesn't actually have course data
        const mappedCourses = posts.slice(0, 5).map((post, index) => ({
          id: post.id,
          name: post.title,
          code: `CS10${index + 1}`,
          credits: 3 + (index % 2), // just alternates 3/4 for variety
          grade: 'A'
        }));

        setCourses(mappedCourses);
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false); // runs whether it succeeded or failed
      }
    }

    loadCourses();
  }, []); // empty array = run once, on mount

 
  useEffect(() => {
    console.log('Courses updated');
  }, [courses]);

  const filteredCourses = courses.filter((course) =>
    course.name.toLowerCase().includes(searchTerm.toLowerCase())
  );

  function handleEnroll(courseId) {
    const course = courses.find((c) => c.id === courseId);

    setEnrolledCourses((prevEnrolled) => {
      const alreadyEnrolled = prevEnrolled.some((c) => c.id === courseId);
      if (alreadyEnrolled) return prevEnrolled;
      return [...prevEnrolled, course];
    });
  }

  return (
    <>
      <Header siteName="Student Portal" enrolledCount={enrolledCourses.length} />

      <main>
        <h2>Available Courses</h2>

        
        {loading && <p>Loading...</p>}

        {/* Step 73: error message, shown only if error is not null */}
        {error && <p className="error-message">Something went wrong: {error}</p>}

        {/* Only show the search box and grid once loading is done */}
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
                  onEnroll={handleEnroll}
                />
              ))}
            </div>
          </>
        )}

        <StudentProfile />
      </main>

      <Footer />
    </>
  );
}

export default App;
