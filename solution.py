import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="phonebook",
    user="pp2_user",
    password="pp2"
)

cursor = conn.cursor()

# 1-task 

def get_all():
    cursor.execute('select get_all()') 
    conn.commit()
    for i in cursor.fetchall():
        print(i)

def get_all_2():
    cursor.callproc('get_all_2', ())
    for i in cursor.fetchall():
        print(i)


# 2-task
flag = ''
def insert_or_update():
    global flag
    name = input('type NAME: ')
    surname = input('type SURNAME: ')
    num = input('type NUMBER: ')
    email = input('type EMAIL: ')
    company = input('type COMPANY: ') 

    cursor.execute("select * from phone_book")
    for contact in cursor.fetchall():
        if contact[1] == name and contact[2] == surname:
            flag = 'update'
            break 

    if flag == 'update':
        cursor.execute(f"call upd('{name}', '{surname}', '{num}', '{email}', '{company}');")
        conn.commit()
    else:
        cursor.execute(f"call ins('{name}', '{surname}', '{num}', '{email}', '{company}');")
        conn.commit()


# 2-task 2-way (BEST WAY)
def ins_or_upd_2():
    name = input('type NAME: ')
    surname = input('type SURNAME: ')
    num = input('type NUMBER: ')
    email = input('type EMAIL: ')
    company = input('type COMPANY: ')

    cursor.execute(f"call ins_or_upd('{name}', '{surname}', '{num}', '{email}', '{company}');")
    conn.commit()


# 3-task 

a = [
    ['name11', 'surname11', '+1-100-111-0011', 'qr11@email.kz', 'company11'],
    ['name12', 'surname12', '+1-100-111-0012', 'qr12@email.kz', 'company12'],
    ['name11', 'surname13', '+1-100-111-0013', 'qr13@email.kz', 'company13'],
    ['name11', 'surname14', '+1-100-111-0014', 'qr14@email.kz', 'company14'],
    ['name11', 'surname15', '+1-100-111-0015', 'qr15@email.kz', 'company15'],
]

def insert_by_list(arr):
    for i in arr:
        cursor.execute(f"call ins('{i[0]}', '{i[1]}', '{i[2]}', '{i[3]}', '{i[4]}');")
        conn.commit()

# Other criterias such as: 
#    << Use loop and if statement in stored procedure.
#       Check correctness of phone in procedure and return all incorrect data>>
# I have done them in DataGrip

#------------------------------------------------------------

# 4-task 

def pagination():
    limit = int(input('type limit: '))
    offset = int(input('type offset: '))
    cursor.execute(f"select * from phone_book order by id limit {limit} offset {offset};")
    conn.commit()
    for i in cursor.fetchall():
        print(i)

# 5-task

def delete_data_by_name_or_number():
    number = input('type NUMBER that u wanna delete by: ')
    name = input('type NAME that u wanna delete by: ')

    cursor.execute(f"call delete_data('{name}', '{number}');")
    conn.commit()



