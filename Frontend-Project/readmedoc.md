# Module 2: Frontend Development — Digital Nurture 5.0

A progressive series of hands-on exercises covering frontend development,
from plain HTML/CSS through modern frameworks and production concerns
like accessibility and state management.

## handson_01 — Semantic HTML5 & CSS3 Foundations
Built the Student Portal skeleton using proper semantic elements
(`header`, `nav`, `main`, `section`, `article`, `footer`). Covered CSS
selectors, specificity, the box model, and basic typography.

## handson_02 — Flexbox & CSS Grid
Rebuilt the header, hero, and stats bar using Flexbox for 1D layouts,
and the course cards using CSS Grid for a responsive multi-column layout
(including `auto-fit`/`minmax` for layouts with no media queries).

## handson_03 — JavaScript DOM & Interactivity
Replaced hardcoded HTML with data-driven rendering: course data in a
separate `data.js`, DOM elements built with `createElement`, live search
filtering, sorting, and click events handled via event delegation.

## handson_04 — Async JavaScript & APIs
Covered Promises, `async`/`await`, and `Promise.all`. Built a reusable
`apiFetch` wrapper with proper error handling, a loading spinner, and a
Retry button. Compared `fetch` vs Axios, including interceptors.

## handson_05 — React Fundamentals
Rebuilt the portal in React: functional components, props, `useState`
for enrollment and search, `useEffect` for data fetching, and a
`StudentProfile` form with controlled inputs.

## handson_06 — React Router, Context API & Redux Toolkit
Added multi-page navigation with React Router (`Routes`, `Link`,
`useParams`, `useNavigate`), then moved shared enrollment state first
into Context API, then refactored again into Redux Toolkit with
`createSlice` and Redux DevTools.

## handson_07 — Angular
Rebuilt the portal in Angular: components with `@Input()` bindings,
a `CourseService` using `HttpClient` and Dependency Injection, Angular
Router, and a Reactive Form with validators for the profile page.

## handson_08 — Vue 3
Rebuilt the portal again in Vue 3: Composition API (`ref`, `computed`,
`onMounted`), Vue Router for navigation, and Pinia for shared enrollment
state across components.

## handson_09 — Accessibility & Cross-Browser Compatibility
Audited the original HTML/CSS portal with Lighthouse, fixed semantic
and labeling issues, added ARIA attributes and full keyboard navigation,
checked colour contrast against WCAG AA, and documented cross-browser
support findings.

## handson_10 — Centralised API Layer & Advanced State Management
Built a proper Axios-based API layer (`apiClient` + `courseApi`) with
request/response interceptors, wired it into Redux Toolkit using
`createAsyncThunk` for async data fetching, added a React Error Boundary
for global error handling, and compared state management approaches
across React (Redux), Angular (NgRx), and Vue (Pinia).

---

**Stack covered across the series:** HTML5, CSS3, JavaScript,
React, Angular, Vue 3, React Router, Vue Router, Angular Router, Context
API, Redux Toolkit, Pinia, Axios, Fetch API, and accessibility
standards.
