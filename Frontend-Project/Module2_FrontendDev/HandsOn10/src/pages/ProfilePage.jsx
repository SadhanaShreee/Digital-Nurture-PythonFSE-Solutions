import { useSelector, useDispatch } from 'react-redux';
import { unenroll } from '../redux/enrollmentSlice';
import StudentProfile from '../components/StudentProfile';

function ProfilePage() {
  const enrolledCourses = useSelector((state) => state.enrollment.enrolledCourses);
  const dispatch = useDispatch();

  return (
    <main>
      <StudentProfile />

      <section className="enrolled-list">
        <h2>My Enrolled Courses</h2>

        {enrolledCourses.length === 0 && <p>You haven't enrolled in any courses yet.</p>}

        {enrolledCourses.map((course) => (
          <div key={course.id} className="enrolled-item">
            <span>{course.name} ({course.code})</span>
            <button onClick={() => dispatch(unenroll(course.id))}>Remove</button>
          </div>
        ))}
      </section>
    </main>
  );
}

export default ProfilePage;