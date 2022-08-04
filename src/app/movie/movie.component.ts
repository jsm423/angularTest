import { Component, OnInit } from '@angular/core';
import { Movie } from '../movieList';
import { Movies } from '../movieData';

@Component({
  selector: 'app-movie',
  templateUrl: './movie.component.html',
  styleUrls: ['./movie.component.css']
})
export class MovieComponent implements OnInit {

  movies = Movies;                        //<1>

  // movie: Movie = {                     //<2>
  //   movieName : '영화1',
  //   date : '2022-07-01',
  //   rating : '4.5',
  //   director : '감독1'
  // };

  //  title = 'movie';
  //  data=[                               //<3>               
  //   {movieName: "영화1", date: "2022-07-01", rating: "5.0",director:"감독1"},
  //   {movieName: "영화2", date: "2022-07-02", rating: "1.0",director:"감독2"},
  //   {movieName: "영화3", date: "2022-07-03", rating: "4.0",director:"감독3"},
  //   {movieName: "영화4", date: "2022-07-04", rating: "4.3",director:"감독4"},
  //   {movieName: "영화5", date: "2022-07-05", rating: "3.0",director:"감독5"},
  //   {movieName: "영화6", date: "2022-07-06", rating: "5.0",director:"감독6"},
  //   {movieName: "영화7", date: "2022-07-07", rating: "2.2",director:"감독7"},
  //   {movieName: "영화8", date: "2022-07-08", rating: "4.4",director:"감독8"},
  //   {movieName: "영화9", date: "2022-07-09", rating: "3.1",director:"감독9"},
  //   {movieName: "영화10", date: "2022-07-10", rating: "2.0",director:"감독10"}
  // ]

  ngOnInit(): void {
  }

}
