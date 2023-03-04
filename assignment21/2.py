import qrcode
import sqlite3

PRODUCTS = []
bill = []
n=0
con = sqlite3.connect("data.db")
cur=con.cursor()
cur.execute("CREATE TABLE PRODUCTS (code, name, price, count)")

def make_qr_code():
    user_input = input("Enter the code of the product: ")
    for product in PRODUCTS:
        if product["code"] == user_input:
            img = qrcode.make(product)
            img.save("img"+str(n)+".png")
            n+=1

def show_menu():
    print("1- Add")
    print("2- Edit")
    print("3- Remove")
    print("4- Search")
    print("5- Show List")
    print("6- Buy")
    print("7- Make QR-code")
    print("8- Exit")

def add():
    code = input("code: ")
    name = input("name: ")
    price = input("price: ")
    count = input("count: ")
    con = sqlite3.connect("data.db")
    cur=con.cursor()
    cur.execute(f"INSERT INTO PRODUCTS VALUES ({code},'{(name)}', {price}, {count})")
    con.commit()
    print("done!")

def edit():
    user_input = int(input("code of the product: "))
    res=cur.execute("SELECT * FROM PRODUCTS")
    f=res.fetchall()
    for product in f:
        if product[0] == user_input:
            choice = int(input("1:name \n2:price\n3:count\n"))
            if choice == 1:
                new_name = input("new Name: ")
                res.execute(f"""UPDATE PRODUCTS
                SET name = '{new_name}'
                WHERE code = {user_input}""")
            elif choice == 2:
                new_price = input("new Price: ")
                res.execute(f"""UPDATE PRODUCTS
                SET price = '{new_price}'
                WHERE code = {user_input}""")
            elif choice == 3:
                new_count = input("new Count: ")
                res.execute(f"""UPDATE PRODUCTS
                SET count = '{new_count}'
                WHERE code = {user_input}""")
            print("Done!")
            break
    else:
        print("not found!")

def remove():
    user_input = int(input("code of the product: "))
    res=cur.execute("SELECT * FROM PRODUCTS")
    f=res.fetchall()
    for product in f:
        if product[0] == user_input:
            cur.execute(f"""DELETE FROM PRODUCTS WHERE code={user_input}""")
            print("done!")
            break
    else:
        print("not found!")

def search():
    user_input = input("code or name of the product: ")
    res=cur.execute("SELECT * FROM PRODUCTS")
    f=res.fetchall()
    for product in f:
        if product[0] == int(user_input) or product[1] == user_input:
            print(product[0], "\n", product[1], "\n", product[2])
            break
    else:
        print("not found!")                    

def show_list():
    res=cur.execute("SELECT * FROM PRODUCTS")
    f=res.fetchall()
    for line in f:
        print( "code",line[0], "name", line[1], "price", line[2], "count", line[3])
    

def buy():
    total = 0
    cur.execute("CREATE TABLE bill (code, name, price, count)")
    user_input = input("code of the product: ")
    res=cur.execute("SELECT * FROM PRODUCTS")
    f=res.fetchall()  

    while True:
        for product in f:
            if product[0] == int(user_input):
                num = int(input("number: "))
                count = int(product[3])

                if num <= count:
                    count -= num
                    res.execute(f"""UPDATE PRODUCTS
                    SET name = '{count}'
                    WHERE code = {user_input}""")
                    cur.execute(f"INSERT INTO bill VALUES ({product[0]},'{(product[1])}', {product[2]}, {num})")
                    print("done")
                else:
                    print("Insufficient inventory")    
            ans = input("Do you wany to continue? (Y/N)? ")
            if ans == "N":
                a=cur.execute("SELECT * FROM bill")
                final_bill=a.fetchall() 
                for item in final_bill:
                    print(item[0], "\t\t", item[1], "\t\t", item[2], "\t\t", item[3])
                    total += (int(item[2])*int(item[3]))
                sum = {"sum": total}
                bill.append(sum) 
                print("sum=", total )
                break

while True:
    show_menu()
    choice = int(input())

    if choice == 1:
        add()
    elif choice == 2:
        edit()
    elif choice == 3:
        remove()
    elif choice == 4:
        search()
    elif choice == 5:
        show_list()
    elif choice == 6:
        buy()
    elif choice == 7:
        make_qr_code()
    elif choice == 8:
        exit(0)
    else:
        print("invalid")