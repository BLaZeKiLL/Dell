import { TestBed } from '@angular/core/testing';

import { LocalAdoptionsService } from './local-adoptions.service';

describe('LocalAdoptionsService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: LocalAdoptionsService = TestBed.get(LocalAdoptionsService);
    expect(service).toBeTruthy();
  });
});
