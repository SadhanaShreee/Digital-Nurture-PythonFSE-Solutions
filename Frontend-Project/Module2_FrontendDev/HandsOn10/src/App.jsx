import { Routes, Route } from 'react-router-dom'
import Header from './components/Header'
import Footer from './components/Footer'
import HomePage from './pages/HomePage'
import CoursesPage from './pages/CoursesPage'
import CourseDetailPage from './pages/CourseDetailPage'
import ProfilePage from './pages/ProfilePage'

// App.jsx no longer holds courses/loading/error state at
// all — that all lives in Redux now, and CoursesPage dispatches the
// thunk itself. App.jsx goes back to being purely about routing.
function App() {
  return (
    <>
      <Header siteName="Student Portal" />

      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/courses" element={<CoursesPage />} />
        <Route path="/courses/:courseId" element={<CourseDetailPage />} />
        <Route path="/profile" element={<ProfilePage />} />
      </Routes>

      <Footer />
    </>
  )
}

export default App