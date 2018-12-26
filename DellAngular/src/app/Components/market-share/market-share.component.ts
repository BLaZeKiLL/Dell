import { Component, OnChanges, Input, ViewChild, ElementRef } from '@angular/core';
import { PieCardComponent } from '../pie-card/pie-card.component';
import { LocalAdoptionsService } from 'src/app/Services/local-adoptions.service';
import { LabelsService } from 'src/app/Services/labels.service';
import { ColorsService } from 'src/app/Services/colors.service';
import { tap } from 'rxjs/operators';

@Component({
  selector: 'app-market-share',
  templateUrl: './market-share.component.html',
  styleUrls: ['./market-share.component.css']
})
export class MarketShareComponent implements OnChanges {

  @Input() regionCode: string;

  @ViewChild('piecard') pieCard: PieCardComponent;
  @ViewChild('dominance') domspan: ElementRef;
  @ViewChild('alienware') alienware: ElementRef;
  @ViewChild('inspiron') inspiron: ElementRef;
  @ViewChild('xps') xps: ElementRef;

  constructor(private loader: LocalAdoptionsService, private labels: LabelsService, private colors: ColorsService) {}

  ngOnChanges() {
    this.loader.RequestMarketShare(this.regionCode)
    .pipe(
      tap(data => {
        let i = 0, x = data.shares[0], index = 0;

        for (i = 1; i < data.shares.length; i++) {
          if (data.shares[i] > x) {
            x = data.shares[i];
            index = i;
          }
        }

        let dominance: string;

        switch (index) {
          case 0: dominance = 'Alienware'; break;
          case 1: dominance = 'Inspiron'; break;
          case 2: dominance = 'XPS'; break;
        }

        this.summary(dominance, data.shares);
      })
    )
    .subscribe(
      (data) => {
        this.pieCard.drawChart(data.shares, this.labels.market, [this.colors.alienware, this.colors.inspiron, this.colors.xps]);
      }
    );
  }

  summary(dominance: string, shares: number[]) {
    this.domspan.nativeElement.innerHTML = dominance;
    this.alienware.nativeElement.innerHTML = shares[0];
    this.inspiron.nativeElement.innerHTML = shares[1];
    this.xps.nativeElement.innerHTML = shares[2];
  }

}
