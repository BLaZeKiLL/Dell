import { Component, Input, OnChanges } from '@angular/core';
import { Chart } from 'chart.js';
import { MainChartLoaderService } from 'src/app/Services/main-chart-loader.service';
import { IMainChartData } from 'src/app/Models/main-chart-data.model';
import { ColorsService } from 'src/app/Services/colors.service';
import { LabelsService } from 'src/app/Services/labels.service';

@Component({
  selector: 'app-main-chart',
  templateUrl: './main-chart.component.html',
  styleUrls: ['./main-chart.component.css']
})
export class MainChartComponent implements OnChanges {

  @Input() regionCode: string;

  constructor(private loader: MainChartLoaderService, private colors: ColorsService, private labels: LabelsService) { }

  private chart: Chart;

  ngOnChanges() {
    this.loader.RequestMainChartData(this.regionCode).subscribe(
      (data) => {
        this.drawMainChart(data);
      },
      (error) => { console.log(error); }
    );
  }

  private drawMainChart(chartData: IMainChartData) {
    if (this.chart != null) {
      this.chart.destroy();
    }

    this.chart = new Chart('main-chart', {
      type: 'line',
      data: {
        labels: this.labels.quaters,
        datasets: [{
          label: 'Inspiron',
          borderColor: this.colors.inspiron,
          backgroundColor: this.colors.inspiron,
          fill: false,
          data: chartData[0]
        }, {
          label: 'XPS',
          borderColor: this.colors.xps,
          backgroundColor: this.colors.xps,
          fill: false,
          data: chartData[1]
        }, {
          label: 'AlienWare',
          borderColor: this.colors.alienware,
          backgroundColor: this.colors.alienware,
          fill: false,
          data: chartData[2]
        }]
      },
      options: {
        scales: {
          yAxes: [{
            scaleLabel: {
              display: true,
              labelString: 'Sales'
            }
          }]
        },
        responsive: true
      }
    });
  }

}
