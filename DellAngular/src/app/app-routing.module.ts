import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { ProductComponent } from './Components/product/product.component';

const routes: Routes = [
  { path: '', redirectTo: 'product/GLO', pathMatch: 'full' },
  { path: 'product/:region', component: ProductComponent },
];

@NgModule({
  imports: [ RouterModule.forRoot(routes) ],
  exports: [ RouterModule ]
})
export class AppRoutingModule {}
