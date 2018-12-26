import { Injectable } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
import { IAdoptionChartData } from '../Models/adoption-chart-data.model';
import { Observable } from 'rxjs';
import { IMarketData } from '../Models/market-data.model';
import { map, tap } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class LocalAdoptionsService {

  constructor(private http: HttpClient) { }

  RequestMarketShare(regionCode: string): Observable<IMarketData> {
    const options = { params: new HttpParams().set('region', regionCode) };
    return this.http.get<number[]>('http://localhost:3000/data/localAnalysis', options)
    .pipe(
      map((data) => {
        return <IMarketData>{ shares: data.map(values => +values.toFixed(2)) };
      })
    );
  }

  RequestLocalAdoptions(regionCode: string, type: string): Observable<IAdoptionChartData> {
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
