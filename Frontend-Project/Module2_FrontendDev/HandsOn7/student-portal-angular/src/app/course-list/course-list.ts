import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { CourseCard } from '../course-card/course-card';
import { Course } from '../course';

@Component({
  selector: 'app-course-list',
  standalone: true,
  imports: [CommonModule, FormsModule, CourseCard],
  templateUrl: './course-list.html',
  styleUrl: './course-list.css'
})
export class CourseList {
  courses: Course[] = [
    { id: 1, name: 'Data Structures & Algorithms', code: 'CS101', credits: 4, grade: 'A' },
    { id: 2, name: 'Database Management Systems', code: 'CS102', credits: 3, grade: 'A-' },
    { id: 3, name: 'Web Application Development', code: 'CS103', credits: 3, grade: 'B+' },
    { id: 4, name: 'Operating Systems', code: 'CS104', credits: 4, grade: 'A' },
    { id: 5, name: 'Machine Learning Foundations', code: 'CS105', credits: 4, grade: 'B+' }
  ];
  searchTerm = '';

  get filteredCourses(): Course[] {
    return this.courses.filter((course) =>
      course.name.toLowerCase().includes(this.searchTerm.toLowerCase())
    );
  }
}