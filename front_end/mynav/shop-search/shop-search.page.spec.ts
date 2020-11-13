import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { IonicModule } from '@ionic/angular';

import { ShopSearchPage } from './shop-search.page';

describe('ShopSearchPage', () => {
  let component: ShopSearchPage;
  let fixture: ComponentFixture<ShopSearchPage>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ShopSearchPage ],
      imports: [IonicModule.forRoot()]
    }).compileComponents();

    fixture = TestBed.createComponent(ShopSearchPage);
    component = fixture.componentInstance;
    fixture.detectChanges();
  }));

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
