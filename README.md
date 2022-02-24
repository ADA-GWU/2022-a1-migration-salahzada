# 2022-a1-migration-salahzada
This project is written in Python language. User must install python language from https://www.python.org/downloads/

The database is created based on PosgreSQL. So, user need PosgreSQL environment.

After installation user must create python environment to run commands. 

These files provide to create and modifying database. 
It consists 3 parts:

1) Creation database -> create_db.py
2) Migration of datas -> migrate.py
3) Migration datas to initial version -> rollback.py


1. First command : python create_db.py   -> creates tables and columns 
2. Second command : python migrate.py    -> migrates tables and columns 
3. Third command : python rollback.py    -> migrates tables and columns to initial version (as first creation) 

1) For checking creation database take attention below:
There are two tables : Students and Interests
Students has 2 columns and interests has 9 columns. 

If you have those changes all goes well.

2) For cheking migration please take attention below:


There are 3 columns in Students and 9 columns in Interests.

After migration there will be 3 columns in Interests and column name of students will change.

If you see those changes after migration all goes well.



