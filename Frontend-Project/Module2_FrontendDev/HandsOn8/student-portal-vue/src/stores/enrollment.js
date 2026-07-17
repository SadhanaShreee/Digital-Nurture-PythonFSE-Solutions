import { ref, computed } from 'vue'
import { defineStore } from 'pinia'


export const useEnrollmentStore = defineStore('enrollment', () => {
  const enrolledCourses = ref([])

  const totalCredits = computed(() =>
    enrolledCourses.value.reduce((sum, course) => sum + course.credits, 0)
  )

  function enroll(course) {
    const alreadyEnrolled = enrolledCourses.value.some((c) => c.id === course.id)
    if (!alreadyEnrolled) {
      enrolledCourses.value.push(course)
    }
  }

  function unenroll(courseId) {
    enrolledCourses.value = enrolledCourses.value.filter((c) => c.id !== courseId)
  }

  return { enrolledCourses, totalCredits, enroll, unenroll }
})