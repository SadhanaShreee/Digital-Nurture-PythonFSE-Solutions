<script setup>
import { computed } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { courses } from '../data/courses'
import { useEnrollmentStore } from '../stores/enrollment'

const route = useRoute()
const router = useRouter()
const store = useEnrollmentStore()

const course = computed(() =>
  courses.find((c) => c.id === Number(route.params.id))
)

function handleEnroll() {
  store.enroll(course.value)
  router.push('/profile')
}
</script>

<template>
  <main v-if="course">
    <h2>{{ course.name }}</h2>
    <p>Code: {{ course.code }}</p>
    <p>Credits: {{ course.credits }}</p>
    <p>Grade: {{ course.grade }}</p>
    <button @click="handleEnroll">Enroll</button>
  </main>
  <main v-else>
    <p>Course not found.</p>
  </main>
</template>

<style scoped></style>