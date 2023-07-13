import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { HelloWorldComponent } from './hello-world/hello-world.component';
import { CounterComponent } from './counter/counter.component';

const routes: Routes = [
  { path: 'hello', component: HelloWorldComponent },
  { path: 'counter', component: CounterComponent },
  { path: '', redirectTo: '/counter', pathMatch: 'full' }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
