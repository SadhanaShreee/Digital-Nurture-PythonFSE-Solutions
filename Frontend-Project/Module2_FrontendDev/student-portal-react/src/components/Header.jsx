function Header({ siteName, enrolledCount }) {
  return (
    <header>
      <p className="site-name">{siteName}</p>
 
      <nav>
        <ul>
          <li><a href="#">Home</a></li>
          <li><a href="#">Courses</a></li>
          <li><a href="#">Profile</a></li>
        </ul>
      </nav>
 
      <p className="enrolled-count">Enrolled: {enrolledCount}</p>
    </header>
  );
}
 
export default Header;