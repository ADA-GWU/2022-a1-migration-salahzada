import psycopg2
cursor=None
db=None
try:
    db = psycopg2.connect(dbname="postgres",user="postgres",password="password123",host="127.0.0.1",port=5432)

    #TASK 1
    query="ALTER TABLE students RENAME COLUMN st_id TO student_id"

    #TASK2
    query1="ALTER TABLE students ALTER COLUMN st_name TYPE varchar(30)"
    query2 = "ALTER TABLE students ALTER COLUMN st_last TYPE varchar(30)"

    # TASK3
    query3 = "ALTER TABLE interest RENAME TO interests;"
    query4="""
alter table interests add column interests varchar(15)[];
insert into interests(student_id, interests) select student_id, array_agg(interest) from interests group by(student_id);
delete from interests where interests.interests is null;
alter table interests drop column interest;
    """

    cursor = db.cursor()
    cursor.execute(query)
    cursor.execute(query1)
    cursor.execute(query2)
    cursor.execute(query3)
    cursor.execute(query4)


    db.commit()
    print("Migration successfully complicated")
except Exception:
    print("Has already been migrated.")

finally:
    if cursor is not None:
        cursor.close()
    if db is not None:
        db.close()
        
