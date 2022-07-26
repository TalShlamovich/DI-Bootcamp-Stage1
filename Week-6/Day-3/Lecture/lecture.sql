-- create table colours(
-- colour_id serial primary key,
-- name varchar(100) not null)

-- CREATE TABLE cars(
-- car_id SERIAL PRIMARY KEY,
-- car_colour INTEGER REFERENCES colours (colour_id) ON DELETE RESTRICT,
-- car_name TEXT);

-- insert into colours (name) values
-- ('red'),
-- ('orange'),
-- ('yellow'),
-- ('green'),
-- ('blue')

-- insert into cars values
-- (default, 
--     (select colour_id from colours where name ilike '%blue%'),
--     'Honda')

-- select name, car_name
-- from cars
-- inner join colours
-- on cars.car_colour = colours.colour_id

delete from colours where name ilike '%blue%'