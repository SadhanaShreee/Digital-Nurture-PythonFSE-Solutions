import { courses } from './data.js';

const loadingMessage = document.querySelector('.loading-message');
const courseGrid = document.querySelector('.course-grid');
const totalCreditsEl = document.querySelector('.total-credits');
const detailsEl = document.querySelector('.course-details');
const searchInput = document.querySelector('.search-input');
const sortButton = document.querySelector('.sort-button');

let currentCourses = [];


function renderCourses(courseList) {
  courseGrid.innerHTML = '';

  const fragment = document.createDocumentFragment();

  courseList.forEach((course) => {
    const card = document.createElement('article');
    card.className = 'course-card';
    card.dataset.id = course.id;
    card.innerHTML = `
      <h3>${course.name}</h3>
      <p>${course.code}</p>
      <span>${course.credits} Credits</span>
    `;
    fragment.appendChild(card);
  });

  courseGrid.appendChild(fragment);

  const sum = courseList.reduce((total, course) => total + course.credits, 0);
  totalCreditsEl.textContent = `Total Credits: ${sum}`;
}

// TASK 1:

/* Step 45: fetchUser using .then() chaining (console demo only) */
function fetchUser(id) {
  fetch('https://jsonplaceholder.typicode.com/users/' + id)
    .then((response) => response.json())
    .then((user) => console.log('User name (via .then):', user.name));
}
fetchUser(1);

/* Step 46: same thing, rewritten with async/await + try/catch */
async function fetchUserAsync(id) {
  try {
    const response = await fetch('https://jsonplaceholder.typicode.com/users/' + id);
    const user = await response.json();
    console.log('User name (via async/await):', user.name);
  } catch (error) {
    console.log('Something went wrong fetching the user:', error.message);
  }
}
fetchUserAsync(1);

/* Step 47: simulate a 1-second network delay, then return local courses */
async function fetchAllCourses() {
  await new Promise((resolve) => setTimeout(resolve, 1000));
  return courses;
}

/* Step 48: show loading message, fetch, then render */
async function loadAndRenderCourses() {
  loadingMessage.style.display = 'block';

  currentCourses = await fetchAllCourses(); // pauses ~1 second

  loadingMessage.style.display = 'none';
  renderCourses(currentCourses);
}

loadAndRenderCourses();

/* Step 49: Promise.all() — fetch two users at the same time */
async function fetchBothUsers() {
  const [user1Response, user2Response] = await Promise.all([
    fetch('https://jsonplaceholder.typicode.com/users/1'),
    fetch('https://jsonplaceholder.typicode.com/users/2')
  ]);
  const user1 = await user1Response.json();
  const user2 = await user2Response.json();
  console.log('Both users fetched together:', user1.name, '&', user2.name);
}
fetchBothUsers();


// Step 50: search and sort functionality

searchInput.addEventListener('input', (event) => {
  const query = event.target.value.toLowerCase();
  const filtered = currentCourses.filter((course) =>
    course.name.toLowerCase().includes(query)
  );
  renderCourses(filtered);
});

sortButton.addEventListener('click', () => {
  const sorted = [...currentCourses].sort((a, b) => b.credits - a.credits);
  renderCourses(sorted);
});

courseGrid.addEventListener('click', (event) => {
  const card = event.target.closest('.course-card');
  if (!card) return;

  const clickedId = Number(card.dataset.id);
  const course = currentCourses.find((c) => c.id === clickedId);

  if (course) {
    detailsEl.textContent = `${course.name} — Grade: ${course.grade}`;
  }
});