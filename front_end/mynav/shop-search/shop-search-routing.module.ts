import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { ShopSearchPage } from './shop-search.page';

const routes: Routes = [
  {
    path: '',
    component: ShopSearchPage
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class ShopSearchPageRoutingModule {}
