<script setup>
import { useEnrollmentStore } from '../stores/enrollment'

// Step 120: calling the store gives you direct, reactive access to
// its state — no props, no prop drilling, same benefit Context/Redux
// gave you in React
const store = useEnrollmentStore()
</script>

<template>
  <header>
    <p class="site-name">Student Portal</p>
    <nav>
      <ul>
        <li><RouterLink to="/">Home</RouterLink></li>
        <li><RouterLink to="/courses">Courses</RouterLink></li>
        <li><RouterLink to="/profile">Profile</RouterLink></li>
      </ul>
    </nav>
    <p class="enrolled-count">Enrolled: {{ store.enrolledCourses.length }}</p>
  </header>
</template>

<style scoped>
header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem 1.2rem;
  background-color: #1a1a2e;
  color: #fff;
}
nav ul {
  list-style: none;
  display: flex;
  gap: 1.5rem;
}
nav a {
  color: #fff;
  text-decoration: none;
}
</style>