import { useState, useEffect } from 'react';
import { Routes, Route } from 'react-router-dom';
import Header from './components/Header';
import Footer from './components/Footer';
import HomePage from './pages/HomePage';
import CoursesPage from './pages/CoursesPage';
import CourseDetailPage from './pages/CourseDetailPage';
import ProfilePage from './pages/ProfilePage';

function App() {
  const [courses, setCourses] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

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
        const mappedCourses = posts.slice(0, 5).map((post, index) => ({
          id: post.id,
          name: post.title,
          code: `CS10${index + 1}`,
          credits: 3 + (index % 2),
          grade: 'A'
        }));

        setCourses(mappedCourses);
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    }

    loadCourses();
  }, []);

  return (
    <>
      {/* Note: Header no longer needs enrolledCount passed as a prop coz it reads it directly from context now... */}
      <Header siteName="Student Portal" />

      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route
          path="/courses"
          element={<CoursesPage courses={courses} loading={loading} error={error} />}
        />
        <Route
          path="/courses/:courseId"
          element={<CourseDetailPage courses={courses} />}
        />
        <Route path="/profile" element={<ProfilePage />} />
      </Routes>

      <Footer />
    </>
  );
}

export default App;