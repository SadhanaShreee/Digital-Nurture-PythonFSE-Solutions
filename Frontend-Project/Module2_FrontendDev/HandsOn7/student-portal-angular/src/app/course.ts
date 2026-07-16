import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';

export interface Course {
  id: number;
  name: string;
  code: string;
  credits: number;
  grade: string;
}

@Injectable({
  providedIn: 'root'
})
export class CourseService {
  constructor(private http: HttpClient) {}

  getCourses(): Observable<Course[]> {
    return this.http
      .get<any[]>('https://jsonplaceholder.typicode.com/posts?_limit=5')
      .pipe(
        map((posts) =>
          posts.map((post, index) => ({
            id: post.id,
            name: post.title,
            code: `CS10${index + 1}`,
            credits: 3 + (index % 2),
            grade: 'A'
          }))
        )
      );
  }
}
