import { Component, ViewChild, Input, OnChanges } from '@angular/core';
import { PieCardComponent } from '../pie-card/pie-card.component';
import { GlobalAdoptionsService } from 'src/app/Services/global-adoptions.service';
import { ColorsService } from 'src/app/Services/colors.service';
import { LabelsService } from 'src/app/Services/labels.service';
import { LocalAdoptionsService } from 'src/app/Services/local-adoptions.service';

@Component({
  selector: 'app-adoption-charts',
  templateUrl: './adoption-charts.component.html',
  styleUrls: ['./adoption-charts.component.css']
})
export class AdoptionChartsComponent implements OnChanges {

  @Input() title: string;
  @Input() regionCode: string;

  @ViewChild('inspiron') inspiron: PieCardComponent;
  @ViewChild('xps') xps: PieCardComponent;
  @ViewChild('alienware') alienware: PieCardComponent;

  constructor(private globalLoader: GlobalAdoptionsService,
              private localLoader: LocalAdoptionsService,
              private colors: ColorsService,
              private lables: LabelsService) {  }

  ngOnChanges() {
    if (this.regionCode === 'GLO') {
      this.globalInit();
    } else {
      this.localInit();
    }
  }

  globalInit() {
    this.globalLoader.RequestGlobalAdoptions(this.title).subscribe(
      (data) => {
        switch (this.title) {
          case 'Market Share': {
            this.inspiron.drawChart(data.Inspiron, this.lables.regions, this.colors.inspiron5);
            this.xps.drawChart(data.XPS, this.lables.regions, this.colors.xps5);
            this.alienware.drawChart(data.AlienWare, this.lables.regions, this.colors.alienware5);
            break;
          }
          case 'Generations': {
            this.inspiron.drawChart(data.Inspiron, this.lables.generations, this.colors.inspiron3);
            this.xps.drawChart(data.XPS, this.lables.generations, this.colors.xps3);
            this.alienware.drawChart(data.AlienWare, this.lables.generations, this.colors.alienware3);
            break;
          }
          case 'Occupations': {
            this.inspiron.drawChart(data.Inspiron, this.lables.occupations, this.colors.inspiron6);
            this.xps.drawChart(data.XPS, this.lables.occupations, this.colors.xps6);
            this.alienware.drawChart(data.AlienWare, this.lables.occupations, this.colors.alienware6);
            break;
          }
        }
      },
      (error) => console.log(error)
    );
  }

  localInit() {
    this.localLoader.RequestLocalAdoptions(this.regionCode, this.title).subscribe(
      (data) => {
        switch (this.title) {
          case 'Generations': {
            this.inspiron.drawChart(data.Inspiron, this.lables.generations, this.colors.inspiron3);
            this.xps.drawChart(data.XPS, this.lables.generations, this.colors.xps3);
            this.alienware.drawChart(data.AlienWare, this.lables.generations, this.colors.alienware3);
            break;
          }
          case 'Occupations': {
            this.inspiron.drawChart(data.Inspiron, this.lables.occupations, this.colors.inspiron6);
            this.xps.drawChart(data.XPS, this.lables.occupations, this.colors.xps6);
            this.alienware.drawChart(data.AlienWare, this.lables.occupations, this.colors.alienware6);
            break;
          }
        }
      },
      (error) => console.log(error)
    );
  }
}
