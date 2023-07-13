import { Component, Output, EventEmitter } from '@angular/core';

@Component({
  selector: 'app-add-todo',
  template: `
    <input type="text" [(ngModel)]="newTodo">
    <button (click)="addTodo()">Add Todo</button>
  `,
  styles: []
})
export class AddTodoComponent {
  newTodo: string = ''; // Update the type to string

  @Output() todoAdded = new EventEmitter<string>();

  addTodo() {
    if (this.newTodo.trim() !== '') {
      this.todoAdded.emit(this.newTodo);
      this.newTodo = '';
    }
  }
}
