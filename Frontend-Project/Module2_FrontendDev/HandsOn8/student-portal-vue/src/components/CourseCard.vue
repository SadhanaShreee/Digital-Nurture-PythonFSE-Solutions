<script setup>
// defineProps is a Vue compiler macro -  you don't import it,
// it's just globally available inside <script setup>. This is Vue's
// equivalent of React's props or Angular's @Input().
defineProps({
  name: String,
  code: String,
  credits: Number,
  grade: String
})
</script>

<template>
  <!--  In CourseCard.vue, define props using defineProps({ name: String, code: String, credits: Number, grade: String }). Render them in the template. -->
  <article class="course-card">
    <h3>{{ name }}</h3>
    <p>{{ code }}</p>
    <span>{{ credits }} Credits</span>
    <p>Grade: {{ grade }}</p>
  </article>
</template>

<style scoped>
.course-card {
  background-color: #fff;
  padding: 1.2rem;
  border: 1px solid #ddd;
  border-radius: 8px;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.1);
}
</style>