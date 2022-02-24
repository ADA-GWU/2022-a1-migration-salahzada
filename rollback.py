import psycopg2

cursor = None
db = None
try:
    db = psycopg2.connect(dbname="postgres", user="postgres", password="elcin123", host="127.0.0.1", port=5432)

    # TASK 1
    query="ALTER TABLE students RENAME COLUMN student_id TO st_id"

    # TASK 2
    query1="ALTER TABLE students ALTER COLUMN ST_NAME TYPE varchar(30)"
    query2 = "ALTER TABLE students ALTER COLUMN ST_LAST TYPE varchar(30)"

    # TASK 3
    query3 = "drop table interests "  # task 3 (changing name)
    query4= """ 
create table interests (student_id int, interest varchar(15));
insert into interests values (1, 'Tennis');
insert into interests values (1, 'Literature');
insert into interests values (1, 'Math');
insert into interests values (2, 'Tennis');
insert into interests values (3, 'Math');
insert into interests values (3, 'Music');
insert into interests values (2, 'Football');
insert into interests values (1, 'Chemistry');
insert into interests values (3, 'Chess');
"""
    query5 = "ALTER TABLE interests RENAME COLUMN interests TO interest"


    cursor = db.cursor()
    cursor.execute(query)
    cursor.execute(query1)
    cursor.execute(query2)

    cursor.execute(query3)
    cursor.execute(query4)
    cursor.execute(query5)

    db.commit()
    print("Rollback successfully complicated")
except Exception:
    print("You have already rolled back.")

finally:
    if cursor is not None:
        cursor.close()
    if db is not None:
        db.close()






