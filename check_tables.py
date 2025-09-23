import sqlite3
from pathlib import Path

# 数据库文件路径（和 settings.py 里一致）
db_path = Path(__file__).resolve().parent / "db.sqlite3"

con = sqlite3.connect(db_path)
cursor = con.cursor()

# 查询所有表名
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

print("当前数据库里的表：")
for t in tables:
    print("-", t[0])

con.close()
