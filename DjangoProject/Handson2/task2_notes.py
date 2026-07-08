

# In [14]: Course.objects.filter(department__name='Computer Science')
#Out[14]: <QuerySet [<Course: Data Structures>, <Course: Algorithms>]>

#In [15]: Department.objects.annotate(course_count=Count('course')).values('name', 'course_count')
#Out[15]: <QuerySet [{'name': 'Computer Science', 'course_count': 2}, {'name': 'Mechanical', 'course_count': 2}]>



# In [17]: list(Student.objects.select_related('department').all())
#Out[17]: 
#[<Student: Asha Kumar>,
 #<Student: Ravi Menon>,
 #<Student: Priya Nair>,
 #<Student: Karthik S>,
 #<Student: Divya R>]

#In [18]: print(connection.queries[-1])
#{'sql': 'SELECT "CourseManagementApp_student"."id", "CourseManagementApp_student"."first_name", "CourseManagementApp_student"."last_name", "CourseManagementApp_student"."email", "CourseManagementApp_student"."department_id", "CourseManagementApp_student"."enrollment_year", "CourseManagementApp_department"."id", "CourseManagementApp_department"."name", "CourseManagementApp_department"."hod", "CourseManagementApp_department"."budget" FROM "CourseManagementApp_student" INNER JOIN "CourseManagementApp_department" ON ("CourseManagementApp_student"."department_id" = "CourseManagementApp_department"."id")', 'time': '0.000'}

#In [19]: Department.objects.update(budget=F('budget') * 1.1)
#Out[19]: 2

