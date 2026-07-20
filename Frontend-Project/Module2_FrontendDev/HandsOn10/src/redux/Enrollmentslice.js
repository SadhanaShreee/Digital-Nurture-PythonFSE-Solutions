import { createSlice, createAsyncThunk } from '@reduxjs/toolkit'
import { getAllCourses } from '../api/courseApi'

export const fetchAllCourses = createAsyncThunk(
  'courses/fetchAll',
  async () => {
    return await getAllCourses()
  }
)

const enrollmentSlice = createSlice({
  name: 'enrollment',
  initialState: {
    enrolledCourses: [],
    courses: [],       // all available courses (now fetched via thunk)
    loading: false,
    error: null
  },
  reducers: {
    enroll(state, action) {
      const course = action.payload
      const alreadyEnrolled = state.enrolledCourses.some((c) => c.id === course.id)
      if (!alreadyEnrolled) {
        state.enrolledCourses.push(course)
      }
    },
    unenroll(state, action) {
      const courseId = action.payload
      state.enrolledCourses = state.enrolledCourses.filter((c) => c.id !== courseId)
    }
  },

  extraReducers: (builder) => {
    builder
      .addCase(fetchAllCourses.pending, (state) => {
        state.loading = true
        state.error = null
      })
      .addCase(fetchAllCourses.fulfilled, (state, action) => {
        state.courses = action.payload
        state.loading = false
      })
      .addCase(fetchAllCourses.rejected, (state, action) => {
        state.error = action.error.message
        state.loading = false
      })
  }
})

export const { enroll, unenroll } = enrollmentSlice.actions
export default enrollmentSlice.reducer