import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';

import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { LayoutModule } from '@angular/cdk/layout';
import { MatToolbarModule,
         MatButtonModule,
         MatSidenavModule,
         MatIconModule,
         MatListModule,
         MatCardModule,
         MatInputModule,
         MatFormFieldModule
        } from '@angular/material';

import { AppRoutingModule } from './app-routing.module';

import { RegionPipe } from './Pipes/region.pipe';

import { AppComponent } from './app.component';
import { NavComponent } from './Components/nav/nav.component';
import { ProductComponent } from './Components/product/product.component';
import { MainChartComponent } from './Components/main-chart/main-chart.component';
import { PieCardComponent } from './Components/pie-card/pie-card.component';
import { InsightsComponent } from './Components/insights/insights.component';
import { AdoptionChartsComponent } from './Components/adoption-charts/adoption-charts.component';
import { MarketShareComponent } from './Components/market-share/market-share.component';

@NgModule({
  declarations: [
    AppComponent,
    NavComponent,
    ProductComponent,
    RegionPipe,
    MainChartComponent,
    PieCardComponent,
    InsightsComponent,
    AdoptionChartsComponent,
    MarketShareComponent,
  ],
  imports: [
    BrowserModule,
    BrowserAnimationsModule,
    HttpClientModule,
    LayoutModule,
    MatToolbarModule,
    MatButtonModule,
    MatSidenavModule,
    MatCardModule,
    MatIconModule,
    MatListModule,
    MatInputModule,
    MatFormFieldModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
