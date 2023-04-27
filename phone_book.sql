------- Lab 11 ---------------------------
------------------------------------------

create role pp2_user with password 'pp2' login;
grant all privileges on database PhoneBook to pp2_user;

create table phone_book (
    id serial primary key not null,
    name text,
    surname text,
    number text,
    email text,
    company text
);

grant all privileges on table phone_book to pp2_user;
grant usage, select on sequence phone_book_id_seq to pp2_user;

insert into phone_book (name, surname, number, email, company)
values ('user_name_1', 'user_surname_1', '+1-700-999-0001', '1@kbtu.fit', 'jetbrains'),
        ('user_name_2', 'user_surname_2', '+1-123-999-0002', '2@kbtu.fit' ,'facebook'),
        ('user_name_3', 'user_surname_3', '+1-444-999-0003', '3@kbtu.fit' ,'telegram'),
        ('user_name_4', 'user_surname_4', '+1-555-999-0004', '4@kbtu.fit' ,'google'),
        ('user_name_5', 'user_surname_5', '+1-666-999-0005', '5@kbtu.fit' ,'amazon');

-- 1. Function that returns all records based on a pattern
create or replace function get_all()
    returns setof phone_book
as
    $$
    begin
        return query
            select * from phone_book;
    end;
    $$ language plpgsql;

drop function get_all();

select get_all();



-- DROP FUNCTION get_all_2();

---- second version RETURNS TABLE
create or replace function get_all_2()
returns table
        (
            id int,
            name    text,
            surname text,
            number  text,
            email text ,
            company text
        )
as
    $$
    begin
        return query
        select * from phone_book;
    end;
    $$ language plpgsql;

select * from get_all_2();

-------------------------------------------------------------------

-- 2. Create procedure to insert new user by name and phone,
-- update phone if user already exists

create or replace procedure ins(_name text, _surname text, _number text, _email text, _c text)
as
    $$
    begin
        insert into phone_book(name, surname, number, email, company)
        values ($1, $2, $3, $4, $5);
    end;
    $$ language plpgsql;

call ins('use6', 'use44', '+1-112-121-1212', 'r@gmail.com', 'hello');


DROP PROCEDURE ins(text,text,text,text,text);

create or replace procedure upd(_name text, _surname text, _number text, _email text, _c text)
as
    $$
    begin
        update phone_book
        set number = $3 , email = $4, company = $5
        where name = $1 and surname = $2;
    end;
    $$ language plpgsql;


call upd('Mike', 'Tyson', '+1-000-000-0000', 'sdsgs@gmail.com', 'hsdfsdfsfdello');


create or replace procedure ins_or_upd(_name text, _surname text, _number text, _email text, _c text)
as
    $$
        begin
            if exists(select * from phone_book where name = $1 and surname = $2) then
                update phone_book
                set number = $3 , email = $4, company = $5
                where name = $1 and surname = $2;
            else
                insert into phone_book(name, surname, number, email, company)
                values ($1, $2, $3, $4, $5);
            end if;
        end;
    $$ language plpgsql;

call ins_or_upd('Mike', 'Tyson', '+1-123-123-0000', '123123@gmail.com', '123123');
call ins_or_upd('joh', 'hey', '+1-453-5656-565', '2345.ocm', 'oracle')
--------------------------------------------------------------------

-- 3. Create procedure to insert many new users by list of name and phone.
-- Use loop and if statement in stored procedure.
-- Check correctness of phone in procedure and return all incorrect data.


create or replace procedure check_phone()
as
    $$
    declare
        nums text;
    begin
        for nums in select number from phone_book
            loop
            if (length(nums) <= 15 and length(nums) >= 11) then
                raise notice 'correct numbers= %', nums;
            else
                raise notice 'uncorrect numbers = %', nums;
            end if;
            end loop;

    end
    $$ language plpgsql;

insert into phone_book (name, surname, number, email, company)
values ('user_name_441', 'user_surname_441', '+34341-700-999-0001', '1@kbtu.fit', 'jetbrains'),
        ('user_name_442', 'user_surname_442', '+190002', '2@kbtu.fit' ,'facebook'),
        ('user_name_443', 'user_surname_443', '+-0003', '3@kbtu.fit' ,'telegram');


call check_phone();

----------------------------------------------------------------------------

-- 4.Create function to querying data from
-- the tables with pagination (by limit and offset)

select * from phone_book order by id limit 5 offset 3;

-- 5.Implement procedure to deleting
-- data from tables by username or phone

create or replace procedure delete_data(usnm text, phone text)
as
    $$
    begin
        delete from phone_book
        where name = $1 or number = $2;
    end;
    $$ language plpgsql;

call delete_data('', '87989');
call delete_data('name12', '');