-- Lab10 --> 2-task

create table snake_game (
    id serial primary key not null,
    username text not null ,
    user_score int
);

insert into snake_game (username, user_score)
values ('user1', 0),
       ('user2', 0),
       ('user3', 0),
       ('user4', 0);

alter table snake_game
add column user_level text;

alter table snake_game
add column user_speed int;

select * from snake_game;

update snake_game
set user_level = 'easy'
where id in (1, 2, 3, 4);

update snake_game
set user_speed = 0
where id in (1, 2, 3, 4);

alter table snake_game
add column password text;

update snake_game
set password = 'hello'
where id in (1, 2, 3, 4);

alter table snake_game
drop column user_speed;

insert into snake_game (username, user_score, user_level, password)
values ('user5', 0, 'easy', 'hellobek');


update snake_game set user_score = 1 where id = 3;
update snake_game set user_level = 'medium' where id = 3;

drop table snake_game;

create table snake_game (
    id serial not null ,
    username text not null ,
    user_score int,
    user_level text,
    password text not null,
    primary key (id, username)
);

insert into snake_game (username, user_score, user_level, password)
values ('user1', 0, 'Easy', 'pass1'),
       ('user2', 0, 'Easy', 'pass2'),
       ('user3', 0, 'Easy', 'pass3'),
       ('user4', 0, 'Easy', 'pass4'),
       ('user5', 0, 'Easy', 'pass5');

select * from snake_game
order by user_score asc ;

update snake_game
set user_level = 'Senior'
where user_level = 'Hard';