# Microservices Decomposition — Course Management System

| Service Name          | Responsibility                          | Endpoints Owned                          | Database Owned         |
|------------------------|------------------------------------------|-------------------------------------------|--------------------------|
| Course Service         | Department and course CRUD               | /api/courses/, /api/departments/          | course_service.db       |
| Student Service        | Student CRUD, enrollment                  | /api/students/, /api/students/{id}/enroll | student_service.db      |
| Auth Service  | Registration, login, token validation     | /api/auth/register/, /api/auth/login/     | auth_service.db         |
| Notification Service | Sending email confirmations         | (internal, triggered by events)           | none (stateless)         |

