// Step 30: ES6 import — pulling the named export `courses` from data.js
import { courses } from './data.js';
 
 
// Step 30: destructuring inside a loop — pulling out just the two
// fields we need instead of writing course.name / course.credits everywhere
for (const course of courses) {
  const { name, credits } = course;
  // Step 34: template literal for string interpolation
  console.log(`${name} carries ${credits} credits`);
}
 
// Step 31: Array.map() — build a new array of formatted strings
// Arrow function (Step 34) + template literal (Step 34) combined here
const formattedCourses = courses.map(
  (course) => `${course.code} — ${course.name} (${course.credits} credits)`
);
console.log("Formatted courses:", formattedCourses);
 
// Step 32: Array.filter() — only courses worth 4+ credits
const heavyCourses = courses.filter((course) => course.credits >= 4);
console.log("Courses with 4+ credits:", heavyCourses.length);
 
// Step 33: Array.reduce() — sum up total credits enrolled
const totalCredits = courses.reduce((sum, course) => sum + course.credits, 0);
console.log("Total credits enrolled:", totalCredits);
 
 
/* 
   TASK 2 — DOM SELECTION & DYNAMIC RENDERING (Steps 35-39)*/
 
// Step 36: select the (now empty) grid container from the HTML
const courseGrid = document.querySelector('.course-grid');
const totalCreditsEl = document.querySelector('.total-credits');
const detailsEl = document.querySelector('.course-details');
 
// Reusable render function — takes any array of courses and draws them.
// each time we re-render after a search or sort.
function renderCourses(courseList) {
  courseGrid.innerHTML = ''; // clear before re-rendering
 
  // DocumentFragment batches all the new nodes into one DOM update
  // instead of triggering a reflow on every single appendChild call.
  const fragment = document.createDocumentFragment();
 
  courseList.forEach((course) => {
    // Step 37: create the article element, set its class, build inner HTML
    const card = document.createElement('article');
    card.className = 'course-card';
    // data-id lets us find the right course object later via event delegation
    card.dataset.id = course.id;
 
    card.innerHTML = `
      <h3>${course.name}</h3>
      <p>${course.code}</p>
      <span>${course.credits} Credits</span>
    `;
 
    fragment.appendChild(card);
  });
 
  // Step 38: append everything to the grid in one go
  courseGrid.appendChild(fragment);
 
  // Step 39: update total credits dynamically based on what's showing
  const sum = courseList.reduce((total, course) => total + course.credits, 0);
  totalCreditsEl.textContent = `Total Credits: ${sum}`;
}
 
// Initial render on page load — full course list
renderCourses(courses);
 
 
/* 
   TASK 3 — EVENT LISTENERS & INTERACTIVITY (Steps 40-44) */
 
const searchInput = document.querySelector('.search-input');
const sortButton = document.querySelector('.sort-button');
 
// Step 41: filter-as-you-type search, case-insensitive
searchInput.addEventListener('input', (event) => {
  const query = event.target.value.toLowerCase();
  const filtered = courses.filter((course) =>
    course.name.toLowerCase().includes(query)
  );
  renderCourses(filtered);
});
 
// Step 42: sort by credits descending, then re-render
sortButton.addEventListener('click', () => {
  // spread into a new array so we don't mutate the original `courses` order
  const sorted = [...courses].sort((a, b) => b.credits - a.credits);
  renderCourses(sorted);
});
 
courseGrid.addEventListener('click', (event) => {
  const card = event.target.closest('.course-card');
  if (!card) return; // click was on the grid background, not a card
 
  const clickedId = Number(card.dataset.id);
  const course = courses.find((c) => c.id === clickedId);
 
  if (course) {
    // textContent used here since this is our own trusted data, not
    // user-generated input — but textContent is still the safer default
    detailsEl.textContent = `${course.name} — Grade: ${course.grade}`;
  }
});