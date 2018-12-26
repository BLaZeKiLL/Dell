import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { PieCardComponent } from './pie-card.component';

describe('PieCardComponent', () => {
  let component: PieCardComponent;
  let fixture: ComponentFixture<PieCardComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ PieCardComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(PieCardComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
