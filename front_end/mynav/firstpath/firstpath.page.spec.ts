import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { IonicModule } from '@ionic/angular';

import { FirstpathPage } from './firstpath.page';

describe('FirstpathPage', () => {
  let component: FirstpathPage;
  let fixture: ComponentFixture<FirstpathPage>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ FirstpathPage ],
      imports: [IonicModule.forRoot()]
    }).compileComponents();

    fixture = TestBed.createComponent(FirstpathPage);
    component = fixture.componentInstance;
    fixture.detectChanges();
  }));

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
