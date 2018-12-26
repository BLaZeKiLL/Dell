import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { IPredictionData } from '../Models/prediction-data-.model';
import { tap } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class PredictionService {

  constructor(private http: HttpClient) { }

  globalPrediction(quater: number): Observable<IPredictionData> {
    return this.http.post<IPredictionData>('http://localhost:3000/prediction/global', { quater: quater })
    .pipe(
      tap(
        data => data.value = data.value.map(value => +value.toFixed(2))
      )
    );
  }
}
