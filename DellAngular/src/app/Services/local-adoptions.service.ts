import { Injectable } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
import { IAdoptionChartData } from '../Models/adoption-chart-data.model';
import { tap } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class LocalAdoptionsService {

  constructor(private http: HttpClient) { }

  RequestLocalAdoptions(regionCode: string, type: string) {
    let url = 'http://localhost:3000/data/local';

    switch (type) {
      case 'Generations': url += 'Generation'; break;
      case 'Occupations': url += 'Occupations'; break;
    }

    const options = { params: new HttpParams().set('region', regionCode) };
    return this.http.get<IAdoptionChartData>(url, options)
    .pipe(
      tap(data => {
        data.Inspiron = data.Inspiron.map((value: number) => +value.toFixed(2));
        data.XPS = data.XPS.map((value: number) => +value.toFixed(2));
        data.AlienWare = data.AlienWare.map((value: number) => +value.toFixed(2));
      })
    );
  }
}
