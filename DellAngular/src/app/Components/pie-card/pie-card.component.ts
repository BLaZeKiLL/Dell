import { Component, Input, ViewChild, ElementRef } from '@angular/core';
import { Chart } from 'chart.js';

@Component({
  selector: 'app-pie-card',
  templateUrl: './pie-card.component.html',
  styleUrls: ['./pie-card.component.css']
})
export class PieCardComponent {

  @Input() model: string;
  @ViewChild('piechart') pieChart: ElementRef;

  constructor() { }

  private chart: Chart;

  drawChart(data: number[], lables: string[], colors: string[]) {
    if (this.chart != null) {
      this.chart.destroy();
    }

    this.chart = new Chart(this.pieChart.nativeElement, {
      type: 'doughnut',
      data: {
        labels: lables,
        datasets: [{
          data: data,
          backgroundColor: colors
        }]
      }
    });
  }
}
