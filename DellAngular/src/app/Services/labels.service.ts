import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class LabelsService {
  quaters = ['1st Quater',
             '2nd Quater',
             '3rd Quater',
             '4th Quater',
             '5th Quater',
             '6th Quater',
             '7th Quater',
             '8th Quater',
             '9th Quater',
             '10th Quater',
             '11th Quater',
             '12th Quater'];
  regions = ['CA', 'CAJ', 'SEA', 'USC', 'SWE'];
  generations = ['Gen 1', 'Gen 2', 'Gen 3'];
  occupations = ['Businessman', 'Developer', 'Farmer', 'Gamer', 'Manager', 'Student'];
}
