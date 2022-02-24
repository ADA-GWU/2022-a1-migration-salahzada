# 2022-a1-migration-salahzada
This project is written in Python language. User must install python language from https://www.python.org/downloads/

The database is created based on PosgreSQL. So, user need PosgreSQL environment. Download link: https://www.postgresql.org/download/

After installation user must create python environment to run commands. 

These files provide to create and modifying database. 
It consists 3 parts:

1) Creation database -> create_db.py
2) Migration of datas -> migrate.py
3) Migration datas to initial version -> rollback.py

Use your command line and mention the location of directory on command line.

1. First command : python create_db.py   -> creates tables and columns 
2. Second command : python migrate.py    -> migrates tables and columns 
3. Third command : python rollback.py    -> migrates tables and columns to initial version (as first creation) 

If you run correctly, you will see successful message.



