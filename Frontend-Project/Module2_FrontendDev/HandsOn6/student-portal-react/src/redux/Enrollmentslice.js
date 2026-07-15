import { createSlice } from '@reduxjs/toolkit';

const enrollmentSlice = createSlice({
  name: 'enrollment',            // used as a namespace/prefix for actions
  initialState: {
    enrolledCourses: []
  },
  reducers: {
    enroll(state, action) {
      const course = action.payload; // whatever was passed to dispatch(enroll(...))
      const alreadyEnrolled = state.enrolledCourses.some(
        (c) => c.id === course.id
      );
      if (!alreadyEnrolled) {
        state.enrolledCourses.push(course);
      }
    },

    //  unenroll - removes a course by id
    unenroll(state, action) {
      const courseId = action.payload;
      state.enrolledCourses = state.enrolledCourses.filter(
        (c) => c.id !== courseId
      );
    }
  }
});

// These are the functions components will call via dispatch(...)
export const { enroll, unenroll } = enrollmentSlice.actions;

// This is what gets registered in store.js
export default enrollmentSlice.reducer;