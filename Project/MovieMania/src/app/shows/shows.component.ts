import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { HttpClient } from '@angular/common/http';
import { Movie } from '../models/movie.model';
import { trigger, state, style, animate, transition } from '@angular/animations';

@Component({
  selector: 'app-shows',
  templateUrl: './shows.component.html',
  styleUrls: ['./shows.component.css'],
  animations: [
    trigger('bookAnimation', [
      state('initial', style({
        transform: 'scale(1)',
      })),
      state('clicked', style({
        transform: 'scale(1.2)',
      })),
      transition('initial <=> clicked', animate('200ms ease-in-out')),
    ]),
  ],
})



export class ShowsComponent implements OnInit {
  movieId!: string;
  movie!: Movie;
  loading = false;
  seatRows!: number[][];
  selectedSeats: string[] = [];
  mymovie:  Movie | null = null;


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

  selectSeat(row: number, seat: number): void {
    if (this.seatRows[row][seat] === 0) {
      // Seat is available, select it
      this.seatRows[row][seat] = 2; // 2 represents "selected"
      this.selectedSeats.push(`${row + 1}${String.fromCharCode(65 + seat)}`);
    } else if (this.seatRows[row][seat] === 2) {
      // Seat is already selected, unselect it
      this.seatRows[row][seat] = 0; // 0 represents "available"
      const seatIndex = this.selectedSeats.indexOf(`${row + 1}${String.fromCharCode(65 + seat)}`);
      if (seatIndex !== -1) {
        this.selectedSeats.splice(seatIndex, 1);
      }
    }
  }
  

  shows = [
    { id: 1, date: this.getFormattedDate(0), time: 'Morning', seatsAvailable: Math.floor(Math.random() * 50) + 1 },
    { id: 2, date: this.getFormattedDate(0), time: 'Evening', seatsAvailable: Math.floor(Math.random() * 50) + 1 },
    { id: 3, date: this.getFormattedDate(1), time: 'Morning', seatsAvailable: Math.floor(Math.random() * 50) + 1 },
    { id: 4, date: this.getFormattedDate(1), time: 'Evening', seatsAvailable: Math.floor(Math.random() * 50) + 1 },
    { id: 5, date: this.getFormattedDate(2), time: 'Morning', seatsAvailable: Math.floor(Math.random() * 50) + 1 },
    { id: 6, date: this.getFormattedDate(2), time: 'Evening', seatsAvailable: Math.floor(Math.random() * 50) + 1 },
  ];
  
  getFormattedDate(offset: number): string {
    const currentDate = new Date();
    currentDate.setDate(currentDate.getDate() + offset);
    return currentDate.toISOString().slice(0, 10);
  }
}
