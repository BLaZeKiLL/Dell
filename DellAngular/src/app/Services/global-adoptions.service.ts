import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { IAdoptionChartData } from '../Models/adoption-chart-data.model';
import { tap } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class GlobalAdoptionsService {

  constructor(private http: HttpClient) { }

  RequestGlobalAdoptions(type: string): Observable<IAdoptionChartData> {
    let url = 'http://localhost:3000/data/';

    switch (type) {
      case 'Market Share': url += 'globalAnalysis'; break;
      case 'Generations': url += 'globalGenerations'; break;
      case 'Occupations': url += 'globalOccupations'; break;
    }

    return this.http.get<IAdoptionChartData>(url)
    .pipe(
      tap(data => {
        data.Inspiron = data.Inspiron.map((value: number) => +value.toFixed(2));
        data.XPS = data.XPS.map((value: number) => +value.toFixed(2));
        data.AlienWare = data.AlienWare.map((value: number) => +value.toFixed(2));
      })
    );
  }

}
