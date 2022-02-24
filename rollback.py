import psycopg2

cursor = None
db = None
try:
    db = psycopg2.connect(dbname="postgres", user="postgres", password="password123", host="127.0.0.1", port=5432)

    # TASK 1
    query="ALTER TABLE students RENAME COLUMN student_id TO st_id"

    # TASK 2
    query1="ALTER TABLE students ALTER COLUMN ST_NAME TYPE varchar(30)"
    query2 = "ALTER TABLE students ALTER COLUMN ST_LAST TYPE varchar(30)"

    # TASK 3
    query3 = "drop table interests "  # task 3 (changing name)
    query4= """ 
create table interest (student_id int, interest varchar(15));
insert into interest values (1, 'Tennis');
insert into interest values (1, 'Literature');
insert into interest values (1, 'Math');
insert into interest values (2, 'Tennis');
insert into interest values (3, 'Math');
insert into interest values (3, 'Music');
insert into interest values (2, 'Football');
insert into interest values (1, 'Chemistry');
insert into interest values (3, 'Chess');
"""



    cursor = db.cursor()
    cursor.execute(query)
    cursor.execute(query1)
    cursor.execute(query2)

    cursor.execute(query3)
    cursor.execute(query4)


    db.commit()
    print("Rollback successfully complicated")
except Exception:
    print("You have already rolled back.")

finally:
    if cursor is not None:
        cursor.close()
    if db is not None:
        db.close()

