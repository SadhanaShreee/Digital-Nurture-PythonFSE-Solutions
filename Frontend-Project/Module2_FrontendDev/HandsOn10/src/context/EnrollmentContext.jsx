import { createContext, useState } from 'react';
export const EnrollmentContext = createContext();

export function EnrollmentProvider({ children }) {
  const [enrolledCourses, setEnrolledCourses] = useState([]);

  function enrollCourse(course) {
    setEnrolledCourses((prevEnrolled) => {
      const alreadyEnrolled = prevEnrolled.some((c) => c.id === course.id);
      if (alreadyEnrolled) return prevEnrolled;
      return [...prevEnrolled, course];
    });
  }

  //remove a course from the enrolled list by id
  function removeCourse(courseId) {
    setEnrolledCourses((prevEnrolled) =>
      prevEnrolled.filter((c) => c.id !== courseId)
    );
  }

  // Whatever we put in `value` here is what useContext(EnrollmentContext)
  // will return, anywhere else in the app that asks for it.
  const value = {
    enrolledCourses,
    enrollCourse,
    removeCourse
  };

  return (
    <EnrollmentContext.Provider value={value}>
      {children}
    </EnrollmentContext.Provider>
  );
}