<script setup>
import { useEnrollmentStore } from '../stores/enrollment'

const store = useEnrollmentStore()
</script>

<template>
  <main>
    <h2>My Profile</h2>

    <section class="enrolled-list">
      <h3>My Enrolled Courses</h3>

      <p v-if="store.enrolledCourses.length === 0">
        You haven't enrolled in any courses yet.
      </p>

      <div v-for="course in store.enrolledCourses" :key="course.id" class="enrolled-item">
        <span>{{ course.name }} ({{ course.code }})</span>
        <button @click="store.unenroll(course.id)">Remove</button>
      </div>

      <p class="total-credits" v-if="store.enrolledCourses.length > 0">
        Total Credits: {{ store.totalCredits }}
      </p>
    </section>
  </main>
</template>

<style scoped></style>