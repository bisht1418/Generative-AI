import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Movie } from '../models/movie.model';

@Component({
  selector: 'app-search',
  templateUrl: './search.component.html',
  styleUrls: ['./search.component.css']
})
export class SearchComponent implements OnInit {
  searchQuery = '';
  loading = false;
  movies: Movie[] = [];
  filteredMovies: Movie[] = [];

  constructor(private http: HttpClient) { }

  ngOnInit(): void {
    this.getMovies();
  }

  onSearch(): void {
    if (this.searchQuery.trim() !== '') {
      this.filteredMovies = this.movies.filter((movie) =>
        movie.Title.toLowerCase().includes(this.searchQuery.toLowerCase())
      );
    } else {
      this.filteredMovies = this.movies; // Show all movies when search query is empty
    }
  }

  getMovies(): void {
    this.loading = true;
    this.http.get<Movie[]>('https://bored-handbag-dog.cyclic.app/movies').subscribe(
      (data) => {
        this.movies = data;
        this.filteredMovies = data; // Initialize the filtered list with all movies
        this.loading = false;
      },
      (error) => {
        console.log('Error fetching movies:', error);
        this.loading = false;
      }
    );
  }
}
