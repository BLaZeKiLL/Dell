import { TestBed } from '@angular/core/testing';

import { GlobalAdoptionsService } from './global-adoptions.service';

describe('GlobalAdoptionsService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: GlobalAdoptionsService = TestBed.get(GlobalAdoptionsService);
    expect(service).toBeTruthy();
  });
});
