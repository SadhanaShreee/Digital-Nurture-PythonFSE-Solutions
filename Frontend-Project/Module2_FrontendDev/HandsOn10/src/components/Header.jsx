import { useSelector } from 'react-redux';
import { Link } from 'react-router-dom';

function Header({ siteName }) {
  const enrolledCourses = useSelector((state) => state.enrollment.enrolledCourses);

  return (
    <header>
      <p className="site-name">{siteName}</p>

      <nav>
        <ul>
          <li><Link to="/">Home</Link></li>
          <li><Link to="/courses">Courses</Link></li>
          <li><Link to="/profile">Profile</Link></li>
        </ul>
      </nav>

      <p className="enrolled-count">Enrolled: {enrolledCourses.length}</p>
    </header>
  );
}

export default Header;