import { Injectable } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
import { Observable } from 'rxjs';
import { IMainChartData } from '../Models/main-chart-data.model';
import { tap } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class MainChartLoaderService {

  constructor(private http: HttpClient) { }

  RequestMainChartData(regionCode: string): Observable<IMainChartData> {
    if (regionCode === 'GLO') {
      return this.http.get<IMainChartData>('http://localhost:3000/data/globalSales')
      .pipe(
        tap(data => {
          data[0] = data[0].map((value: number) => Math.floor(value));
          data[1] = data[1].map((value: number) => Math.floor(value));
          data[2] = data[2].map((value: number) => Math.floor(value));
        })
      );
    } else {
      const options = { params: new HttpParams().set('region', regionCode) };
      return this.http.get<IMainChartData>('http://localhost:3000/data/localSales', options)
      .pipe(
        tap(data => {
          data[0] = data[0].map((value: number) => Math.floor(value));
          data[1] = data[1].map((value: number) => Math.floor(value));
          data[2] = data[2].map((value: number) => Math.floor(value));
        })
      );
    }
  }

}
