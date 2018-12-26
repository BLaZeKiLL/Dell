import { Component } from '@angular/core';
import { PredictionService } from 'src/app/Services/prediction.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-insights',
  templateUrl: './insights.component.html',
  styleUrls: ['./insights.component.css']
})
export class InsightsComponent {

  predictionAvaliable: boolean;
  predictionHTML: string;

  constructor(private prediction: PredictionService, private router: Router) {
    this.predictionAvaliable = false;
    this.router.events.subscribe(() => this.clear());
  }

  peridct(quater: number) {
    console.log(quater);
    this.prediction.globalPrediction(quater).subscribe(
      (data) => {
        this.predictionHTML = `
          <ul>
            <li><h4>Inspiron: ${data.value[0]}$</h4></li>
            <li><h4>Xps: ${data.value[1]}$</h4></li>
            <li><h4>Alienware: ${data.value[2]}$</h4></li>
          </ul>
        `;
        this.predictionAvaliable = true;
        console.log(data.value);
      },
      (error) => console.log(error)
    );
  }

  clear() {
    this.predictionAvaliable = false;
    this.predictionHTML = null;
  }
}
