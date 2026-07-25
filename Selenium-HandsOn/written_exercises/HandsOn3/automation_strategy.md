Task 1: Automation Decision and Test Case Selection
1.1 Five Criteria for Automating a Test Case

Test: "POST /api/courses/ returns 201 with correct data when valid input is given."

Repeatability – This test will run again and again on every build. → Good to automate.
Stability – Creating a course is a core feature that won't change much. → Good to automate.
Business risk – If this breaks, admins can't add courses at all. → High risk, so automate.
Clear pass/fail – A script can easily check status code 201 and the response data. → Good to automate.
Effort vs benefit – Takes ~1 hour to automate but saves time on every future run. → Worth it.

Conclusion: This test case is a great fit for automation.

1.2 
		
(a) Test Case - Regression test for all CRUD endpoints	
    Decision - Automate	
    Reason - Repeats every code change, easy to check pass/fail

(b) Test Case - Exploratory testing of new search feature	
    Decision - Manual	
    Reason - Needs human thinking and creativity, no fixed steps

(c) Test Case - Performance test: 100 concurrent users	
    Decision - Automate	
    Reason - Impossible to do manually, needs load-testing tools

(d) Test Case - UI test for login form	
    Decision - Automate
    Reason Simple, repeatable steps, good for Selenium

(e) Test Case - Verify Swagger docs are accurate	
    Decision - Manual	
    Reason - Needs human judgment to compare docs vs behavior

(f) Test Case - Smoke test after deployment	
    Decision - Automate	
    Reason - Runs after every deployment, quick and simple check

1.3 Test Automation ROI

Meaning: ROI tells us after how many runs automating a test becomes cheaper than doing it manually every time.

Given: Automating takes 4 hours (240 min). Manual run takes 30 min. After the 10th run, add 20% maintenance overhead per run.

Break-even point = 240 / 30 = 8 runs

Since 8 runs happen before the 10th run, automation already pays off before any overhead starts. Even after adding 20% overhead (6 extra minutes) from run 11 onwards, automation still stays much cheaper than manual testing in the long run.


1.4 Flaky Tests

Definition: A flaky test is one that sometimes passes and sometimes fails, even though nothing actually changed in the code.

Example: A Selenium test checks if a new course appears in the list right after creating it, but fails sometimes because the page hadn't fully loaded yet.

3 Ways to Fix Flaky Tests:

Use explicit waits (wait for element to appear) instead of fixed sleep timers.
Make each test independent — create and clean up its own data.
Use stable locators like id instead of fragile ones like text or position.



Task 2: Automation Framework Types

2.1 The Five Frameworks (Short Overview)

	Description			
Framework - Linear	
Description - Steps written/recorded one after another, no reuse	
Advantage - Quick to create	
Disadvantage - Hard to maintain, no reuse	
Example Use - Quick one-time check of "create course" page

Framework - Modular	
Description - App broken into reusable pieces (Login, Create Course, etc.)	
Advantage - Reusable code	
Disadvantage - Data still hardcoded	
Example Use - Reusable Login module for all tests

Framework - Data-Driven	
Description - Test logic separate from test data (stored in Excel/CSV)	
Advantage - Test many data sets easily	
Disadvantage - Extra setup for data files	
Example Use - Testing 20 course code variations

Framework - Keyword-Driven
Description - 	Steps written as simple keywords, non-tech people can write tests	
Advantage - Easy for non-coders	
Disadvantage - Takes time to build keyword engine	
Example Use - Analyst writes "Login

Framework Hybrid	
Description - Combines Modular + Data-Driven (+ Keyword)	
Advantage - Most flexible, scalable	
Disadvantage - More complex to set up	
Example Use - Full frontend suite for Course Management

2.2 Recommended Framework for the Login Test Suite

Needs: 50 login combinations, reuse login steps in 20 tests, both technical and non-technical people writing tests.

Recommendation: Hybrid Framework
Why:

Reusing login steps → needs Modular design (one Login component used everywhere)
50 data combinations → needs Data-Driven design (data in a CSV/Excel file)
Non-technical team members → needs a Keyword-Driven layer on top

Since all three needs exist together, a Hybrid framework combining all three is the best fit.

2.3 Hybrid Folder Structure

CourseManagement-AutomationSuite/
├── config/          → environment settings, browser type
├── testdata/         → login_data.csv, course_data.xlsx
├── pageobjects/      → LoginPage.java, CreateCoursePage.java
├── utils/            → WaitUtils.java, ExcelReader.java
├── testcases/        → LoginTest.java, CreateCourseTest.java
├── reports/          → auto-generated test reports
└── README.md         → setup and run instructions

pageobjects/ → reusable modules (Modular part)
testdata/ → external data files (Data-Driven part)
testcases/ → actual test scripts, can use keywords for non-tech users