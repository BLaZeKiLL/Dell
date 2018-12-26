import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class ColorsService {
  inspiron = '#2196f3';
  xps = '#263238';
  alienware: '#D32F2F';

  inspiron3 = ['#90caf9', '#2196f3', '#0d47a1'];
  xps3 = ['#cfd8dc', '#757575', '#263238'];
  alienware3 = ['#E57373', '#F44336', '#D32F2F'];

  inspiron5 = ['#90caf9', '#64b5f6', '#2196f3', '#1976d2', '#0d47a1'];
  xps5 = ['#cfd8dc', '#90a4ae', '#757575', '#546e7a', '#263238'];
  alienware5 = ['#FFCDD2', '#E57373', '#F44336', '#D32F2F', '#B71C1C'];

  inspiron6 = ['#90caf9', '#64b5f6', '#2196f3', '#1976d2', '#0d47a1', '#021350'];
  xps6 = ['#cfd8dc', '#90a4ae', '#757575', '#546e7a', '#263238', '#0a0a0a'];
  alienware6 = ['#FFCDD2', '#E57373', '#F44336', '#D32F2F', '#B71C1C', '#610b05'];
}
