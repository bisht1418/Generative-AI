import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { environment } from 'src/environments/environment';

interface ChatMessage {
  sender: 'user' | 'chatbot';
  text: string;
}

@Component({
  selector: 'app-chatbot',
  templateUrl: './chatbot.component.html',
  styleUrls: ['./chatbot.component.css']
})
export class ChatbotComponent implements OnInit {
  userQuery: string = '';
  chatMessages: ChatMessage[] = [];
  isExpanded: boolean = false;
  openAIApiKey = environment.apiKey; // Replace this with your actual OpenAI API key

  constructor(private http: HttpClient) { }

  ngOnInit(): void {
  }

  onSubmit(): void {
    if (this.userQuery.trim() !== '') {
      this.chatMessages.push({ sender: 'user', text: this.userQuery });

      const apiUrl = 'https://api.openai.com/v1/engines/text-davinci-003/completions';
      const headers = {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${this.openAIApiKey}`
      };

      const requestData = {
        prompt: this.userQuery,
        max_tokens: 50,
        n: 1,
        stop: null,
        temperature: 0.7
      };

      this.http.post<any>(apiUrl, requestData, { headers }).subscribe(
        (response) => {
          const chatbotResponse = response.choices[0].text.trim();
          this.chatMessages.push({ sender: 'chatbot', text: chatbotResponse });
        },
        (error) => {
          console.log('Error fetching chatbot response:', error);
        }
      );
    }
    this.userQuery = '';
  }

  toggleChat(): void {
    this.isExpanded = !this.isExpanded;
  }
}
