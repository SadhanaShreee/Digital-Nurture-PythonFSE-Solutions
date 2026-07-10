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

/* TASK 1:*/

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

/* TASK 2 */

const spinner = document.querySelector('.spinner');
const errorMessageEl = document.querySelector('.error-message');
const retryButton = document.querySelector('.retry-button');
const notificationList = document.querySelector('.notification-list');
 
/* -----------------------------------------------------------
   Step 50: apiFetch — a reusable "smart fetch" function.
 
   Why this matters: fetch() ONLY rejects when
   there's a real network failure - like you're offline. If the
   server responds with a 404 or 500, fetch() still thinks that
   counts as "success" as far as the Promise is concerned! So we
   have to manually check response.ok and throw our own error
   if the status code means something went wrong.
----------------------------------------------------------- */
async function apiFetch(url) {
  const response = await fetch(url);
 
  if (!response.ok) {
    // response.ok is false for any status like 404, 500, etc.
    // We throw a real Error object with a clear message —
    // this will be caught by whoever called apiFetch.
    throw new Error(`Request failed with status ${response.status}`);
  }
 
  return response.json(); // parsed JSON, ready to use
}
 

async function loadNotifications(url = 'https://jsonplaceholder.typicode.com/posts') {
  // reset UI to "loading" state every time this runs
  spinner.style.display = 'block';
  errorMessageEl.style.display = 'none';
  retryButton.style.display = 'none';
  notificationList.innerHTML = '';
 
  try {
    const posts = await apiFetch(url);
 
    // only show the first 5 posts, so the page isn't overwhelming
    const firstFive = posts.slice(0, 5);
 
    const fragment = document.createDocumentFragment();
    firstFive.forEach((post) => {
      const card = document.createElement('div');
      card.className = 'notification-card';
      card.innerHTML = `
        <h3>${post.title}</h3>
        <p>${post.body}</p>
      `;
      fragment.appendChild(card);
    });
    notificationList.appendChild(fragment);
 
  } catch (error) {
    // Step 53: user-friendly message in the UI, not just console.log
    errorMessageEl.textContent = `Couldn't load notifications: ${error.message}`;
    errorMessageEl.style.display = 'block';
    retryButton.style.display = 'block';
 
  } finally {
    // finally always runs, whether it succeeded or failed —
    // perfect place to hide the spinner either way
    spinner.style.display = 'none';
  }
}
 
// Initial load — real, working endpoint
loadNotifications();
 
/* Step 54: Retry button re-calls the same function */
retryButton.addEventListener('click', () => {
  loadNotifications(); // retry the REAL url, not the broken one
});

// TASK 3: Axios version of the same functionality
/* Step 56: the SAME idea as apiFetch, but using Axios instead of fetch(). Notice how much shorter this is:
   - No need to call .json() manually — Axios parses JSON for you
   - No need to check response.ok — Axios automatically throws
     an error for any non-2xx status code, so a plain try/catch is enough on its own */

async function apiFetchAxios(url) {
  const response = await axios.get(url);
  return response.data; // Axios puts the actual JSON body inside .data
}
 
 

async function fetchPostsForUser(userId) {
  try {
    const response = await axios.get('https://jsonplaceholder.typicode.com/posts', {
      params: { userId: userId }
    });
    console.log(`Posts by user ${userId}:`, response.data);
  } catch (error) {
    console.log('Axios request failed:', error.message);
  }
}
 
fetchPostsForUser(1);

axios.interceptors.request.use((config) => {
  console.log('API call started:', config.url);
  return config; // must always return config, or the request gets blocked
});