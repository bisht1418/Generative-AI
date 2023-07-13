import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-todo-list',
  template: `
    <ul>
      <li *ngFor="let todo of todos">
        <span>{{ todo }}</span>
        <button (click)="deleteTodoItem(todo)">Delete</button>
        <button (click)="updateTodoItem(todo)">Update</button>
      </li>
    </ul>
  `,
  styles: []
})
export class TodoListComponent {
  @Input() todos: string[] = [];

  deleteTodoItem(todo: string) {
    const index = this.todos.indexOf(todo);
    if (index !== -1) {
      this.todos.splice(index, 1);
    }
  }

  updateTodoItem(todo: string) {
    // Perform any update logic here
    console.log('Updating todo:', todo);
  }
}
