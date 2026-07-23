# Microservices Decomposition — Course Management System

| Service Name          | Responsibility                          | Endpoints Owned                          | Database Owned         |
|------------------------|------------------------------------------|-------------------------------------------|--------------------------|
| Course Service         | Department and course CRUD               | /api/courses/, /api/departments/          | course_service.db       |
| Student Service        | Student CRUD, enrollment                  | /api/students/, /api/students/{id}/enroll | student_service.db      |
| Auth Service  | Registration, login, token validation     | /api/auth/register/, /api/auth/login/     | auth_service.db         |
| Notification Service | Sending email confirmations         | (internal, triggered by events)           | none (stateless)         |



## Synchronous (HTTP) vs Asynchronous Communication

**Synchronous (what we built here):** Student Service directly calls Course Service over HTTP and waits for a response before continuing. Simple to debug, but creates
tight coupling -> if Course Service is slow or down, enrollment fails immediately.

**Asynchronous (message queue):** Student Service would instead publish
an "enrollment requested" event to a queue and return immediately. Course Service (or a
worker) processes it later, independently. This decouples the services -> Course Service being down doesn't block enrollment, it just delays confirmation -> but introduces eventual consistency (the enrollment isn't confirmed instantly) and more operational complexity
(you now need to run and monitor).

**When to use a queue instead:** when the operation doesn't need an immediate response
(e.g. sending a notification, logging an event, generating a report), or when you want
services to keep working even if a downstream service is temporarily unavailable.