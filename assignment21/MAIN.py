import sqlite3
con = sqlite3.connect("data.db")
cur=con.cursor()
#cur.execute("CREATE TABLE PRODUCTS (name, price, count)")
cur.execute("""
    INSERT INTO PRODUCTS VALUES
        ('IDTEM1', 1000, 3),
        ('IDTEM2', 2000, 4)
""")
con.commit()
res=cur.execute("SELECT * FROM PRODUCTS")

R=res.fetchall()
print(R)