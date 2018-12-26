import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { AdoptionChartsComponent } from './adoption-charts.component';

describe('AdoptionChartsComponent', () => {
  let component: AdoptionChartsComponent;
  let fixture: ComponentFixture<AdoptionChartsComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ AdoptionChartsComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(AdoptionChartsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
