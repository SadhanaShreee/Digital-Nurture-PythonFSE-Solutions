1.1 The V-Model (Explained in Simple Words)

The V-Model gets its name because it looks like the letter "V" ->  one side going down, and one side going up, meeting at a point in the middle.

The left side is the SDLC - the building phases, in order: Requirements → System Design → Architecture Design → Module Design → Coding.
The bottom point of the V is Coding - this is where building ends and testing begins.
The right side is the TDLC - the testing phases, in order: Unit Testing → Integration Testing → System Testing → Acceptance Testing.

1.2 SDLC Phase → TDLC Phase → Test Artifact Produced
SDLC Phase-  Requirements
TDLC Phase - Acceptance Testing
Test Artifact Produced During This Phase
		
SDLC Phase - System Design	
TDLC Phase - System Testing	
Test Artifact Produced During This Phase - System Test Plan (covers end-to-end flows of the Course Management API, like create → enroll → list courses)

SDLC Phase - Architecture Design
TDLC Phase - Integration Testing	
Test Artifact Produced During This Phase - Integration Test Plan (covers how modules like Course Service, Enrollment Service, and Database talk to each other)

SDLC Phase - Module Design	
TDLC Phase - Unit Testing	
Test Artifact Produced During This Phase - Unit Test Cases (covers individual functions, e.g., createCourse(), validateCourseCode())

SDLC Phase - Coding	
TDLC Phase - —	
Test Artifact Produced During This Phase - Code is written here; this is the bottom vertex where SDLC turns into TDLC


1.3 Entry and Exit Criteria for Each Testing Level
a) Unit Testing

Entry Criteria:

Module design document is complete and approved
Code for the specific unit/function is written and compiles without errors
Unit test cases are written and reviewed

Exit Criteria:

All planned unit test cases have been executed
Code coverage meets the agreed target (e.g., 80%)
No open critical/high severity defects in the unit
All unit test results are documented
b) Integration Testing

Entry Criteria:

Unit testing is complete and passed for all modules being integrated
Architecture design document is available (shows how modules connect)
Integration test environment and test data are ready
Interfaces/APIs between modules are defined (e.g., Course Service ↔ Enrollment Service)

Exit Criteria:

All planned integration test cases executed
All module interfaces work correctly together
Defect count is below the agreed threshold
No open critical/high defects related to module communication
c) System Testing

Entry Criteria:

Integration testing is complete and passed
System design document is available
Full system build is deployed in the test environment
Test data covering all major workflows is ready

Exit Criteria:

All planned system test cases executed (functional + non-functional, e.g., performance, security)
Defect count below threshold
No open critical/high defects
System behaves as expected end-to-end (e.g., a course can be created, listed, and enrolled in)
d) Acceptance Testing

Entry Criteria:

System testing is complete and passed
Requirements document / user stories are finalized and available
Business/end users (or their representatives) are available to test
Acceptance test environment mirrors production

Exit Criteria:

All acceptance criteria (Given-When-Then scenarios) pass
Business/client sign-off is received
No open critical/high defects
Product is ready for release/deployment



Task 2: Agile QA and Shift-Left Testing

2.1 Three Problems Caused by Waterfall Testing :
- Defects are found too late and are expensive to fix. 
- If QA only tests the Course Management API after all coding is done, a basic issue (like the "create course" API not validating a duplicate course code) may only surface at the very end by which point fixing it means reworking code, database logic, and possibly the UI, all at once.

- No time buffer for fixes before release. Since testing happens only at the end of the timeline, if major defects are found (e.g., enrollment doesn't decrease available seats), there is very little time left to fix and retest before the deadline. 
- This often leads to rushed fixes or shipping known bugs.

- Requirements misunderstandings are discovered very late. If the admin actually wanted course codes to be auto-generated but developers built manual entry, this mismatch is only caught during Acceptance Testing - near the end - instead of during the Requirements phase, wasting the entire development effort on the wrong feature.


2.2: QA Role in Each Agile Ceremony

1. Sprint Planning	- QA helps define clear Acceptance Criteria for each user story before the sprint starts (e.g., for "create a course," QA clarifies what counts as valid input, what errors should show, etc.), so developers know exactly what "done" means.
Daily Standup - QA reports testing progress and raises any blocking issues - for example, "I can't test the enroll API because the test environment is down" - so the team can resolve blockers quickly.
Sprint Review - QA helps demo the working feature to stakeholders, showing that the Course Management API feature (e.g., course creation) actually works as intended, and highlights any known limitations.
Retrospective - QA reflects on what testing-related process worked well and what didn't (e.g., "test data setup took too long this sprint") and suggests improvements for the next sprint.

2.3 Shift-Left Practices Applied to the Course Management API

(a) Reviewing Requirements for Testability Before development starts:  QA reviews the user story "As a college admin, I want to create a new course" and asks: What is a valid course code format? What fields are mandatory? What error message should show for duplicates? This removes ambiguity before coding begins.

(b) Writing Test Cases Before Code :  QA and developers write Given-When-Then scenarios for the "create course" feature before the actual code is written. Developers can then write code that is designed to pass these scenarios from day one, rather than testing being an afterthought.

(c) Static Code Analysis Tools automatically scan the Course Management API code for issues - unused variables, security risks, code smells, poor formatting - as soon as code is committed, before it even reaches manual or automated testing. This catches simple mistakes instantly instead of during later test cycles.

(d) API Contract Testing Before Integration : Before the Course Service and Enrollment Service are fully integrated, QA verifies that the API contract (e.g., the "create course" endpoint returns a courseId and courseCode in a specific JSON format) is followed correctly by both sides. This is done using contract testing tools so integration issues are caught early, without needing the full system to be built first.

2.4 Feature: Create a new course

  Scenario: Successfully create a course (Happy Path)
    Given the admin is logged into the Course Management system
    And the admin provides a unique course code "CS101" and a valid course name "Intro to Programming"
    When the admin submits the create course request
    Then the course should be created successfully
    And the system should return a success message with the new course ID

  Scenario: Fail to create a course with a duplicate course code
    Given a course with the code "CS101" already exists in the system
    When the admin tries to create a new course using the code "CS101"
    Then the system should reject the request
    And the system should display an error message "Course code already exists"

  Scenario: Fail to create a course with missing required fields
    Given the admin is logged into the Course Management system
    When the admin submits a create course request without a course code or course name
    Then the system should reject the request
    And the system should display an error message indicating which required fields are missing