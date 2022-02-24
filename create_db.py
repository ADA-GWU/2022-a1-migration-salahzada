import psycopg2
cursor=None
db=None
try:
    db = psycopg2.connect(dbname="postgres",user="postgres",password="elcin123",host="127.0.0.1",port=5432)

    query="""create table students (ST_ID int, ST_NAME varchar(15), ST_LAST varchar(15) );
insert into students values (1, 'Konul', 'Gurbanova');
insert into students values (2, 'Shahnur', 'Isgandarli');
insert into students values (3, 'Natavan', 'Mammadova');

create table interests (student_id int, interest varchar(15));
insert into interests values (1, 'Tennis');
insert into interests values (1, 'Literature');
insert into interests values (1, 'Math');
insert into interests values (2, 'Tennis');
insert into interests values (3, 'Math');
insert into interests values (3, 'Music');
insert into interests values (2, 'Football');
insert into interests values (1, 'Chemistry');
insert into interests values (3, 'Chess')"""
    cursor = db.cursor()
    cursor.execute(query)
    db.commit()
    print("Database has been created")
except Exception:
    print("Database has already been created")
finally:
    if cursor is not None:
        cursor.close()
    if db is not None:
        db.close()