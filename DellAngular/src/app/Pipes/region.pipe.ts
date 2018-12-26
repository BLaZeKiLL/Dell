import { Pipe, PipeTransform } from '@angular/core';

@Pipe({ name: 'region' })
export class RegionPipe implements PipeTransform {
  transform(value: string) {
    switch (value) {
      case 'GLO': return 'Global';
      case 'USC': return 'US & Canada';
      case 'WSE': return 'South West Europe';
      case 'CAJ': return 'China & Japan';
      case 'SEA': return 'South East Asia';
      case 'CA': return 'Central Africa';
      default: return '';
    }
  }
}
