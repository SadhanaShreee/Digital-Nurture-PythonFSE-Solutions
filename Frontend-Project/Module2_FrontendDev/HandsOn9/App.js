const courseCards = document.querySelectorAll('.course-card');
const searchInput = document.querySelector('#course-search');
const resultsCount = document.querySelector('.results-count');
const menuToggle = document.querySelector('.menu-toggle');
const mainNav = document.querySelector('#main-nav');


function activateCard(card) {
  const courseName = card.dataset.course;
  alert(`Opening details for: ${courseName}`);
}

courseCards.forEach((card) => {
  card.addEventListener('click', () => activateCard(card));

  card.addEventListener('keydown', (event) => {
    // Only respond to Enter 
    if (event.key === 'Enter' || event.key === ' ') {
      event.preventDefault(); // stops the page from scrolling on Space
      activateCard(card);
    }
  });
});


searchInput.addEventListener('input', (event) => {
  const query = event.target.value.toLowerCase();
  let visibleCount = 0;

  courseCards.forEach((card) => {
    const name = card.dataset.course.toLowerCase();
    const matches = name.includes(query);
    card.style.display = matches ? '' : 'none';
    if (matches) visibleCount++;
  });

  resultsCount.textContent = `${visibleCount} course${visibleCount === 1 ? '' : 's'} found`;
});


menuToggle.addEventListener('click', () => {
  const isExpanded = menuToggle.getAttribute('aria-expanded') === 'true';
  menuToggle.setAttribute('aria-expanded', String(!isExpanded));
  mainNav.classList.toggle('nav-open');
});