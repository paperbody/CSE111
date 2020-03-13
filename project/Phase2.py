#!/usr/bin/env python
import sqlite3

def query1():
    #updating c_discount in table Customer
    newdiscount = input("Set discount to ")
    olddiscount = input("From discount ")
    sql = "update Customer set c_discount = ? where c_discount = ?"
    c.execute(sql, [newdiscount,olddiscount])
    conn.commit();

def query2():
    c.execute("select max(c_custkey) from Customer")
    custkey = c.fetchone()[0]
    custkey = int(custkey)+1
    #insert Customer
    name = raw_input("Name of the customer :")
    discount = input("Discount he/she has :")
    rewardpkts = input ("Reward points he/ she has ") 
    sql = "insert into Customer (c_custkey, c_name, c_discount,c_rewardpkts ) values (?,?,?,?)"
    c.execute(sql,[custkey,name,discount,rewardpkts])
    conn.commit()

def query3():
    #insert faculty
    c.execute("select max(f_facultykey) from faculty")
    facultykey = c.fetchone()[0]
    facultykey  = int(facultykey) +1
    #insert Customer
    name = raw_input("Name of the  faculty: ")
    age = input("how old is the employee: ")
    hours = input ("How many hours do they work ") 
    sql = "insert into Faculty (f_facultykey, f_name, f_age, f_hours ) values (?,?,?,?)"
    c.execute(sql,[facultykey,name,age,hours])
    conn.commit()

def query4():
    #Updating Faculty hour
    newhour = input("New Hours")
    oldhour = input("Old Hours")
    c.execute("update Faculty set f_hours = ? where f_hours = ?", [newhour,oldhour])
    conn.commit();

def query5():
    #updating manufaturer shipkey
    newshipkey = input("New shipkey")
    oldshipkey = input("Old shipkey")
    c.execute("update Manufacturer set m_shipkey = ? where m_shipkey = ?",[newshipkey,oldshipkey]);    
    conn.commit();

def query6():
    #Product prices
    newprice = input("New Prices")
    oldprice = input("Old Prices")
    c.execute("update Product set p_price = ? where p_price = ?", [newprice,oldprice])
    conn.commit();

def query7():
    #Shipments storekey
    newstore = input("New store")
    oldstore = input("Old store")
    c.execute("update Shipments set sp_storekey = ? where sp_storekey = ?", [newstore,oldstore])
    conn.commit();

def query8():
    #Store
    newfaculty = input("New faculty")
    oldfaculty = input("Old faculty")
    c.execute("update Stores set s_facultykey = ? where s_facultykey = ?", [newfaculty,oldfaculty])
    conn.commit();

def query9():
    #delete customer
    name = raw_input("customer name for deletion ")
    c.execute("delete from Customer where c_name = ?;", [name])
    conn.commit();
def query10():
    #delete stores
    name = raw_input("Store name for deletion ")
    c.execute("delete from Stores where s_name = ?;", [name])
    conn.commit()

def query11():
    #finding cheap product type
    print 'finding cheap meat and seafood products'
    c.execute("select p_name from Product where (p_type = 'meat' or p_type = 'seafood') and p_price <50")
    for row in c.fetchall():
        print(row[0].encode("utf-8"))

def query12():
    print 'finding customers with low discount < 2'
    c.execute("select c_name from Customer where c_discount < 2")
    for row in c.fetchall():
        print(row[0].encode("utf-8"))

def query13():
    print "select low priority shipments"
    c.execute("select sp_shipkey from Shipments where sp_priority like 'Low%'")
    for row in c.fetchall():
        print(row[0].encode("utf-8"))

def query14():
    print "manufacturers that have beverage products and have a low priority shipment"
    c.execute("select  distinct m_name from Product, Manufacturer, Shipments where p_mfkey = m_mfkey and p_type = 'beverage' and sp_priority like 'Low%'")
    for row in c.fetchall():
        print(row[0].encode("utf-8"))
        
def query15(): 
    print "selecting customers that go to Los Angeles store"
    c.execute("select distinct c_name from Manufacturer, Shipments, Stores, Customer, Product where  s_location = 'Los Angeles'  and  s_custkey = c_custkey")
    for row in c.fetchall():
        print(row[0].encode("utf-8"))
        
def query16():
    print "Finding seafood products name and location"
    c.execute("select distinct p_name ,s_location from  Stores,  Product where  s_productionkey = p_productkey and p_type = 'seafood'")
    for row in c.fetchall():
        print(row[0].encode("utf-8"))
        
def query17():
    print "Selecting faculty members and where they work if they are under 30"
    c.execute("select f_name, f_age, s_location from Faculty, Stores where s_facultykey = f_facultykey  and f_age < 30")
    for row in c.fetchall():
        print(row[0].encode("utf-8"))

def query18():
    print "order in ascending order the manufactures that product meat"
    c.execute("select distinct m_type, m_name from Manufacturer, Stores, Product where p_mfkey = m_mfkey and s_productionkey = p_productkey and m_type ='meat' order by m_mfkey asc")
    for row in c.fetchall():
        print(row[0].encode("utf-8"))
        
def query19():
    print "Finding urgent shipments with product names and their shipment number"
    c.execute("select p_name, sp_shipkey, m_name  from Product, Shipments, Manufacturer where p_shipkey = sp_shipkey and sp_priority like 'Urgent%' and m_mfkey = p_mfkey")
    for row in c.fetchall():
        print(row[0].encode("utf-8"))

def query20():
    print "finding the type of products that are produced by the most manufacturer, and their manufacturer names "
    c.execute("select m_name, m_type from Manufacturer, (select count(m_type) as max from Manufacturer group by m_type order by count(m_type) desc Limit 1 ) h group by m_type having count(m_type) = h.max")
    for row in c.fetchall():
        print(row[0].encode("utf-8"))
        

def disconnect():
    print "Closed database successfully?"
    c.close()
    conn.close()
    print "Closed database successfully"

key = 1

while (key != "0"):

    key = input("Enter1-10 for Queries, 21 to connect db and 22 to close db: ")
    print(key)
    if (key == 1):
        query1();
    elif key == 2:
        query2();
    elif key == 3:
        query3();
    elif key == 4:
        query4();
    elif key == 5:
        query5();
    elif key == 6:
        query6();
    elif key == 7:
       query7();
    elif key == 8:
        query8();
    elif key == 9:
        query9();
    elif key == 10:
        query10();
    elif key == 11:
        query11();
    elif key == 12:
        query12();
    elif key == 13:
        query13(); 
    elif key == 14:
        query14();
    elif key == 15:
        query15();  
    elif key == 16:
        query16();  
    elif key == 17:
        query17(); 
    elif key == 18:
        query18(); 
    elif key == 19:
        query19(); 
    elif key == 20:
        query20();   
    elif key == 21:
        print "Opened database successfully?"
        conn = sqlite3.connect('7-11.db')
        print "Opened database successfully"
        c = conn.cursor()
        null = True
        x = 0
    elif key == 22:
        key = '0';
        disconnect()
    else:
        print "HI?"
        key = '0';


#c.close();
#conn.close();