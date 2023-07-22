// profile.component.ts

import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';

interface User {
  email: string;
  // Add other properties of the user object here if available
}

interface UserResponse {
  users: User[];
}

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.css']
})


export class ProfileComponent implements OnInit {
  user: any;
  loading = false;
  bookedData: any[] = [];

  constructor(private http: HttpClient) { }

  ngOnInit(): void {
    // Retrieve user email from local storage (assuming you have stored it there during login)
    const userEmail = localStorage.getItem('email');
    console.log(userEmail)

    if (userEmail) {
      this.getUserDetails(userEmail);
      this.getBookedDataByEmail(userEmail)
    } else {
      console.log('User email not found in local storage');
    }
  }

  getUserDetails(email: string): void {
    this.loading = true;
    // Make a GET request to fetch all users
    this.http.get<UserResponse>('https://bored-handbag-dog.cyclic.app/users').subscribe(
      (response) => {
        console.log('Response:', response);
        // Find the user with the matching email
    
        this.user = response.users.find((user) => user.email === email);
        this.loading = false;
      },
      (error) => {
        console.log('Error fetching users:', error);
        this.loading = false;
      }
    );
  }

  generateSeatCode(totalSeats: number): string {
    const row = Math.floor(Math.random() * 10) + 1; // Random row number from 1 to 10
    const seatLetter = String.fromCharCode(65 + Math.floor(Math.random() * 20)); // Random seat letter from A to T

    return `${row}${seatLetter}`;
  }

  getBookedDataByEmail(email: string): void {
    const apiUrl = 'https://bored-handbag-dog.cyclic.app/book';
    this.http.get<any[]>(apiUrl).subscribe(
      (data) => {
        this.bookedData = data.filter((item) => item.email === email);
      },
      (error) => {
        console.log('Error fetching booked data:', error);
      }
    );
  }
  
}
