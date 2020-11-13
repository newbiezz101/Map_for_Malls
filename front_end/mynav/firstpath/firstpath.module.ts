import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { FirstpathPageRoutingModule } from './firstpath-routing.module';

import { FirstpathPage } from './firstpath.page';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    FirstpathPageRoutingModule
  ],
  declarations: [FirstpathPage]
})
export class FirstpathPageModule {}
