import { Component, OnInit} from '@angular/core';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-product',
  templateUrl: './product.component.html',
  styleUrls: ['./product.component.css']
})
export class ProductComponent implements OnInit {

  regionCode: string;

  constructor(private route: ActivatedRoute) {
    this.route.paramMap.subscribe(params => {
      this.regionCode = params.get('region');
    });
  }

  ngOnInit() {}

}