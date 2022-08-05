create table movie(
    movieName varchar2(50),
    releaseDate DATE,
    rating varchar2(10),
    director varchar2(30)    
);
select * from movie;
insert into movie(movieName, releaseDate, rating, director) values ('영화1','2022-07-01','5.0','감독1');
insert into movie(movieName, releaseDate, rating, director) values ('영화2','2022-07-02','1.0','감독2');
insert into movie(movieName, releaseDate, rating, director) values ('영화3','2022-07-03','4.0','감독3');
insert into movie(movieName, releaseDate, rating, director) values ('영화4','2022-07-04','4.3','감독4');
insert into movie(movieName, releaseDate, rating, director) values ('영화5','2022-07-05','3.0','감독5');
insert into movie(movieName, releaseDate, rating, director) values ('영화6','2022-07-06','5.0','감독6');
insert into movie(movieName, releaseDate, rating, director) values ('영화7','2022-07-07','2.2','감독7');
insert into movie(movieName, releaseDate, rating, director) values ('영화8','2022-07-08','4.4','감독8');
insert into movie(movieName, releaseDate, rating, director) values ('영화9','2022-07-09','3.1','감독9');
insert into movie(movieName, releaseDate, rating, director) values ('영화10','2022-07-10','2.0','감독10');

commit;

select movieName, to_date(releaseDate,'yyyy-mm-dd') as releasedate, rating, director from movie;