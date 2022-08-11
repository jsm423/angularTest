import { Component, OnInit } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
import { Observable } from 'rxjs';
import { THIS_EXPR } from '@angular/compiler/src/output/output_ast';


@Component({
  selector: 'app-movie',
  templateUrl: './movie.component.html',
  styleUrls: ['./movie.component.css']
})
export class MovieComponent implements OnInit {

  url = "http://127.0.0.1:5000";

  datas : any;
  searchType : any;
  keyword : any;
  sort : any;
  

  constructor(private http: HttpClient){ }  

  getData(){
    this.datas = this.http.get(this.url+'/movie')
  }
  getSearchData(){      
    console.log(this.searchType, this.keyword)
    this.datas = this.http.get(this.url+'/search?searchType='+this.searchType+'&keyword='+this.keyword)    
  }
  getSortData(){
    console.log(this.sort)
    this.datas = this.http.get(this.url+'/sort?sort='+this.sort)
  }
  ngOnInit(): void {
    this.datas = this.http.get(this.url+'/movie')
  }

}
