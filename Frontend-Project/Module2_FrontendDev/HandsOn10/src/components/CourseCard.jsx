import { useDispatch } from 'react-redux';
import { Link, useNavigate } from 'react-router-dom';
import { enroll } from '../redux/enrollmentSlice';

function CourseCard({ id, name, code, credits, grade }) {
  const navigate = useNavigate();
  const dispatch = useDispatch();

  function handleEnrollClick(event) {
    event.stopPropagation();
    event.preventDefault();
    dispatch(enroll({ id, name, code, credits, grade }));

    navigate('/profile');
  }

  return (
    <Link to={`/courses/${id}`} className="course-card-link">
      <article className="course-card">
        <h3>{name}</h3>
        <p>{code}</p>
        <span>{credits} Credits</span>
        <p>Grade: {grade}</p>
        <button onClick={handleEnrollClick}>Enroll</button>
      </article>
    </Link>
  );
}

export default CourseCard;