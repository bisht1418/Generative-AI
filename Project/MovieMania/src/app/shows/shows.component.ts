// src/app/shows/shows.component.ts

import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { HttpClient } from '@angular/common/http';
import { Movie } from '../models/movie.model';

@Component({
  selector: 'app-shows',
  templateUrl: './shows.component.html',
  styleUrls: ['./shows.component.css']
})
export class ShowsComponent implements OnInit {
  movieId!: string; // Add '!' to tell TypeScript that it will be initialized later
  movie!: Movie; // Add '!' to tell TypeScript that it will be initialized later
  loading = false;
  seatRows!: number[][]; // Add '!' to tell TypeScript that it will be initialized later

  constructor(private route: ActivatedRoute, private http: HttpClient) { }

  ngOnInit(): void {
    this.route.params.subscribe(params => {
      this.movieId = params['id'];
      this.getMovieDetails();
    });
  }

  getMovieDetails(): void {
    this.loading = true;
    this.http.get<Movie>('http://127.0.0.1:5000/movies/' + this.movieId).subscribe(
      (data) => {
        this.movie = data;
        this.loading = false;
        // Initialize the seatRows array with mock seat data (0: available, 1: booked, 2: selected)
        this.initializeSeatRows();
      },
      (error) => {
        console.log('Error fetching movie details:', error);
        this.loading = false;
      }
    );
  }

  initializeSeatRows(): void {
    // Mock data for the seat booking diagram (Assuming 5 rows and 10 seats per row)
    this.seatRows = [];
    const numRows = 5;
    const seatsPerRow = 10;
    for (let i = 0; i < numRows; i++) {
      const rowSeats = new Array(seatsPerRow).fill(0); // All seats are initially available (0)
      this.seatRows.push(rowSeats);
    }
  }


}
