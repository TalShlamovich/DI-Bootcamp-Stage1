-- select * from actors

-- select avg(number_oscars) from actors

-- select * from actors order by number_oscars desc

-- select first_name, last_name from actors where age > '1970-01-01'

-- select * from actors where first_name in ('David', 'Morgan', 'Will')

-- update actors set number_oscars = 0 where first_name = 'Matt'

-- alter table actors add column full_name varchar(100)
-- default null;

-- update actors set full_name = first_name ||' '|| last_name

-- update actors set first_name='Matty' where first_name='Matt'
-- select * from actors

-- update actors set number_oscars = 4 where first_name = 'George'

-- alter table actors rename column age to birthdate

-- DELETE FROM actors WHERE actor_id=4
-- RETURNING actor_id, first_name, last_name, number_oscars;

-- CREATE TABLE movies(
-- movie_id SERIAL,
-- movie_title VARCHAR (50) NOT NULL,
-- movie_story TEXT,
-- actor_playing_id INTEGER,
-- PRIMARY KEY (movie_id),
-- FOREIGN KEY (actor_playing_id) REFERENCES actors (actor_id)
-- );

-- INSERT INTO movies (movie_title, movie_story, actor_playing_id) VALUES
--     ( 'Good Will Hunting', 
--     'Written by Affleck and Damon, the film follows 20-year-old South Boston janitor Will Hunting',
--     (SELECT actor_id from actors WHERE first_name='Jack')),
--     ( 'Oceans Eleven', 
--     'American heist film directed by Steven Soderbergh and written by Ted Griffin.', 
--     (SELECT actor_id from actors WHERE first_name='Jack'));

-- select * from movies

-- select movie_title, full_name
-- from movies
-- join actors
-- on movies.actor_playing_id = actors.actor_id

-- create table producers(
-- prod_id serial,
-- name_of VARCHAR (50) NOT NULL,
-- produced_movie_id integer,
-- PRIMARY KEY (prod_id),
-- FOREIGN KEY (produced_movie_id) REFERENCES movies (movie_id)
-- )

-- insert into producers (name_of, produced_movie_id) values
-- ('producer 1', (select movie_id from movies where movie_title='Good Will Hunting')),
-- ('producer 2', (select movie_id from movies where movie_title='Oceans Eleven'));

select name_of, movie_title
from producers
join movies
on producers.produced_movie_id = movies.movie_id


