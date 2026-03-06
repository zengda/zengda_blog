import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

with open('db.sql', 'r', encoding='utf-8') as f:
    sql_script = f.read()

cursor.executescript(sql_script)

conn.commit()
conn.close()

print('数据库初始化完成！')