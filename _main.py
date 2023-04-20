import psycopg2

conn = psycopg2.connect(
    host ="localhost",
    database = "postgres",
    user = "postgres",
    password = "510149361Karim",
)

cursor = conn.cursor() 

# CREATE entering user name, phone from console
# READ Querying data from the tables (with different filters)
# UPDATE Implement updating data in the table (change user first name or phone)
# DELETE Implement deleting data from tables by username of phone

init_action = input('''Please 
                \n\ttype 'create' to CREATE contact
                \n\ttype 'read' to GET contact from phonebook
                \n\ttype 'update' to CHANGE something 
                \n\ttype 'delete' to DELETE contact 
       ---> : ''')


def func(action):
    if action == 'create':
        name = input('type your NAME: ')
        email = input('type your EMAIL: ')
        number = input('type your PHONE NUMBER: ')
        company = input('type your COMPANY: ')
        cursor.execute(f"insert into phonebooks (name, email, number, company) values ('{name}', '{email}', '{number}', '{company}');")
        conn.commit()
        print(f'\nYou have succesfully created contact of {name}\n')
        

    if action == 'read':
        name = input('Who?, type NAME:  ')
        cursor.execute(f"select * from phonebooks where name = '{name}';")
        conn.commit() 
        contacts = cursor.fetchall()
        for contact in contacts:
            print(f"\n\tNAME: {contact[0]} | EMAIL: {contact[1]} | NUMBER: {contact[2]} | COMPANY: {contact[3]}\n")


    if action == 'update':
        name = input('Who?, type NAME:  ')
        a = input(f"What do u wanna CHANGE in {name}'s contact? Type 'email', 'number', 'company'! :   ")
        if a == 'email':
            email = input('type email: ')
            cursor.execute(f"update phonebooks set email = '{email}' where name = '{name}';")
            conn.commit()
        if a == 'number':
            number = input('type number: ')
            cursor.execute(f"update phonebooks set number = '{number}' where name = '{name}';")
            conn.commit()
        if a == 'company':
            company = input('type company: ')
            cursor.execute(f"update phonebooks set company = '{company}' where name = '{name}';")
            conn.commit()
        print('\nSuccessfully updated!\n')

    if action == 'delete':
        name = input('Who?, type NAME:  ')
        cursor.execute(f"delete from phonebooks where name = '{name}'")
        print('\nSuccessfully deleted!\n')

    act = input('''What else do you want to do? 
                    If NOTHING, push any button.
                    If YES, please type 'create', 'read', 'update', 'delete' :  ''')
    if len(act) <= 3:
        print('\nOk, thank you!\n')
        cursor.close()
        conn.close() 
        return 
    else:
        return func(act)


func(init_action)