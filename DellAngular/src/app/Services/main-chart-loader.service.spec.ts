import { TestBed } from '@angular/core/testing';

import { MainChartLoaderService } from './main-chart-loader.service';

describe('MainChartLoaderService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: MainChartLoaderService = TestBed.get(MainChartLoaderService);
    expect(service).toBeTruthy();
  });
});
