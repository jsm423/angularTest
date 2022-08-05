create table movie(
    movieName varchar2(50),
    releaseDate DATE,
    rating varchar2(10),
    director varchar2(30)    
);
select * from movie;
insert into movie(movieName, releaseDate, rating, director) values ('��ȭ1','2022-07-01','5.0','����1');
insert into movie(movieName, releaseDate, rating, director) values ('��ȭ2','2022-07-02','1.0','����2');
insert into movie(movieName, releaseDate, rating, director) values ('��ȭ3','2022-07-03','4.0','����3');
insert into movie(movieName, releaseDate, rating, director) values ('��ȭ4','2022-07-04','4.3','����4');
insert into movie(movieName, releaseDate, rating, director) values ('��ȭ5','2022-07-05','3.0','����5');
insert into movie(movieName, releaseDate, rating, director) values ('��ȭ6','2022-07-06','5.0','����6');
insert into movie(movieName, releaseDate, rating, director) values ('��ȭ7','2022-07-07','2.2','����7');
insert into movie(movieName, releaseDate, rating, director) values ('��ȭ8','2022-07-08','4.4','����8');
insert into movie(movieName, releaseDate, rating, director) values ('��ȭ9','2022-07-09','3.1','����9');
insert into movie(movieName, releaseDate, rating, director) values ('��ȭ10','2022-07-10','2.0','����10');

commit;

select movieName, to_date(releaseDate,'yyyy-mm-dd') as releasedate, rating, director from movie;