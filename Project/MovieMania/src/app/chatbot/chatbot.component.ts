import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-chatbot',
  templateUrl: './chatbot.component.html',
  styleUrls: ['./chatbot.component.css']
})
export class ChatbotComponent implements OnInit {
  isExpanded: boolean = false;
  messages: { text: string; isUser: boolean }[] = [];
  userInput = '';

  constructor() { }

  ngOnInit(): void {
    // Welcome message from the chatbot
    this.addMessage('Hello! How can I assist you today?', false);
  }

  addMessage(text: string, isUser: boolean): void {
    this.messages.push({ text, isUser });
  }

  sendMessage(): void {
    const userMessage = this.userInput.trim();
    if (userMessage) {
      this.addMessage(userMessage, true);
      // Here you can implement your chatbot logic to generate a response
      // For now, let's just echo the user's message as a placeholder
      this.addMessage(`You said: "${userMessage}"`, false);
      this.userInput = '';
    }
  }

  toggleChatbox(): void {
    this.isExpanded = !this.isExpanded;
  }


}
