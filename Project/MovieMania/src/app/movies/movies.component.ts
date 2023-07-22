import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Movie } from '../models/movie.model';

@Component({
  selector: 'app-movie-list',
  templateUrl: './movies.component.html',
  styleUrls: ['./movies.component.css']
})
export class MoviesComponent implements OnInit {
  movies: Movie[] = [];
  pagedMovies: Movie[] = []; // Updated to store the currently displayed page
  loading = false;
  pageSize = 10; // Number of items per page
  pageSizeOptions: number[] = [5, 10, 25]; // Options for items per page

  constructor(private http: HttpClient) {}

  ngOnInit(): void {
    this.getMovies();
  }

  getMovies(): void {
    this.loading = true;
    this.http.get<Movie[]>('https://bored-handbag-dog.cyclic.app/movies').subscribe(
      (data) => {
        this.movies = data;
        this.loading = false;
        this.updatePagedMovies(0); // Display the first page on initial load
      },
      (error) => {
        console.log('Error fetching movies:', error);
        this.loading = false;
      }
    );
  }

  onPageChange(event: any): void {
    const pageIndex = event.pageIndex;
    this.updatePagedMovies(pageIndex);
  }

  updatePagedMovies(pageIndex: number): void {
    const startIndex = pageIndex * this.pageSize;
    const endIndex = startIndex + this.pageSize;
    this.pagedMovies = this.movies.slice(startIndex, endIndex);
  }
}
