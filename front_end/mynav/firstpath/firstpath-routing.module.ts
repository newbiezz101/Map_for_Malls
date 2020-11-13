import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { FirstpathPage } from './firstpath.page';

const routes: Routes = [
  {
    path: '',
    component: FirstpathPage
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class FirstpathPageRoutingModule {}
