import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { MarketShareComponent } from './market-share.component';

describe('MarketShareComponent', () => {
  let component: MarketShareComponent;
  let fixture: ComponentFixture<MarketShareComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ MarketShareComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(MarketShareComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
