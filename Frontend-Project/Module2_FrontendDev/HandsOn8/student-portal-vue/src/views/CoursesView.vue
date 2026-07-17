<script setup>
import { ref, onMounted, computed } from 'vue'
import CourseCard from '../components/CourseCard.vue'
import { courses as courseData } from '../data/courses'

const courses = ref([])
const searchTerm = ref('')

onMounted(() => {
  courses.value = courseData
})

const filteredCourses = computed(() =>
  courses.value.filter((course) =>
    course.name.toLowerCase().includes(searchTerm.value.toLowerCase())
  )
)
</script>

<template>
  <main>
    <h2>Available Courses</h2>

    <input
      type="text"
      placeholder="Search courses..."
      v-model="searchTerm"
    />

    <div class="course-grid">
      <RouterLink
        v-for="course in filteredCourses"
        :key="course.id"
        :to="`/courses/${course.id}`"
        class="card-link"
      >
        <CourseCard
          :name="course.name"
          :code="course.code"
          :credits="course.credits"
          :grade="course.grade"
        />
      </RouterLink>
    </div>

    <p v-if="filteredCourses.length === 0">No courses found</p>
  </main>
</template>

<style scoped>
.course-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1rem;
  margin-top: 1rem;
}
.card-link {
  text-decoration: none;
  color: inherit;
}
</style>