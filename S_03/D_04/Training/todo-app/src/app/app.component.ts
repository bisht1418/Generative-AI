import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  template: `
    <h1>Todo App</h1>
    <app-add-todo (todoAdded)="addTodoItem($event)"></app-add-todo>
    <app-todo-list [todos]="todos"></app-todo-list>
  `,
  styles: []
})
export class AppComponent {
  todos: Array<string | any> = [];

  addTodoItem(todo: string) {
    this.todos.push(todo);
  }
}
