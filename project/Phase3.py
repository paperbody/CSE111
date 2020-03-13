#!/usr/bin/env python
import sqlite3
from Tkinter import *
#from PIL import ImageTk, Image


root = Tk()

#Customer = Label(root, text = 'Customer')

#CustomerFrame = Frame(root, width = 300, height = 600)
#Customer.bind(CustomerFrame)
#Customer.pack()
# im = Image.open("11-7.png")
# photo =ImageTk.PhotoImage(im)

# label = Label(root, image=photo)
# label.image = photo  # keep a reference!
# label.pack()

##### Customer entry boxes and button

c_custkey = Entry(root, width = 20)
c_custkey.grid(row = 1, column = 1, padx = 20)

c_custkey_label = Label(root, text = "CustKey")
c_custkey_label.grid(row = 1, column  = 0)

c_name = Entry(root, width = 20)
c_name.grid(row = 2, column = 1, padx = 20)

c_name_label = Label(root, text = "name")
c_name_label.grid(row = 2, column  = 0)

c_discount = Entry(root, width = 20)
c_discount.grid(row = 3, column = 1, padx = 20)

c_discount_label = Label(root, text = "discount")
c_discount_label.grid(row = 3, column  = 0)

c_rewardpkts = Entry(root, width = 20)
c_rewardpkts.grid(row = 4, column = 1, padx = 20)

c_rewardpkts_label = Label(root, text = "reward")
c_rewardpkts_label.grid(row = 4, column  = 0)



def InsertCustomer():
    conn = sqlite3.connect('7-11.db')
    c = conn.cursor()

    c.execute("Insert Into Customer Values (:c_custkey, :c_name, :c_discount, :c_rewardpkts)",
            {
                'c_custkey': c_custkey.get(),
                'c_name': c_name.get(),
                'c_discount': c_discount.get(),
                'c_rewardpkts': c_rewardpkts.get()
            })
    conn.commit()
    conn.close()

    c_custkey.delete(0,END)
    c_name.delete(0,END)
    c_discount.delete(0,END)
    c_rewardpkts.delete(0,END)



CustomerButton = Button(root, text ='Insert Customer', width = 20, command = InsertCustomer)
CustomerButton.grid(row = 8, columnspan = 2)

############Faculty

f_facultykey = Entry(root, width = 20)
f_facultykey.grid(row = 1, column = 3, padx = 20)

f_facultykey_label = Label(root, text = "Faculty key")
f_facultykey_label.grid(row = 1, column  = 2)

f_name = Entry(root, width = 20)
f_name.grid(row = 2, column = 3, padx = 20)

f_name_label = Label(root, text = "name")
f_name_label.grid(row = 2, column  = 2)

f_age = Entry(root, width = 20)
f_age.grid(row = 3, column = 3, padx = 20)

f_age_label = Label(root, text = "age")
f_age_label.grid(row = 3, column  = 2)

f_hours = Entry(root, width = 20)
f_hours.grid(row = 4, column = 3, padx = 20)

f_hours_label = Label(root, text = "hours")
f_hours_label.grid(row = 4, column  = 2)

f_storekey = Entry(root, width = 20)
f_storekey.grid(row = 5, column = 3, padx = 20)

f_storekey_label = Label(root, text = "storekey")
f_storekey_label.grid(row = 5, column  = 2)

def InsertFaculty(): 
    conn = sqlite3.connect('7-11.db')
    c = conn.cursor()

    c.execute("Insert into Faculty Values (:f_facultykey, :f_name, :f_age, :f_hours, :f_storekey)",
            {
                    'f_facultykey': f_facultykey.get(),
                    'f_name' : f_name.get(),
                    'f_age' : f_age.get(),
                    'f_hours': f_hours.get(),
                    'f_storekey': f_storekey.get()
            } )
    conn.commit()
    conn.close()

    f_facultykey.delete(0,END)
    f_name.delete(0,END)
    f_age.delete(0,END)
    f_hours.delete(0,END)
    f_storekey.delete(0,END)




FacultyButton = Button(root, text ='Insert Faculty', width = 20, command = InsertFaculty)
FacultyButton.grid(row = 8, column = 2, columnspan = 2)


##########Manufacturer
m_mfkey = Entry(root, width = 20)
m_mfkey.grid(row = 1, column = 5, padx = 20)

m_mfkey_label = Label(root, text = "Motherf key")
m_mfkey_label.grid(row = 1, column  = 4)

m_name = Entry(root, width = 20)
m_name.grid(row = 2, column = 5, padx = 20)

m_name_label = Label(root, text = "name")
m_name_label.grid(row = 2, column  = 4)

m_type = Entry(root, width = 20)
m_type.grid(row = 3, column = 5, padx = 20)

m_type_label = Label(root, text = "type")
m_type_label.grid(row = 3, column  = 4)

m_shipkey = Entry(root, width = 20)
m_shipkey.grid(row = 4, column = 5, padx = 20)

m_shipkey_label = Label(root, text = "shipkey")
m_shipkey_label.grid(row = 4, column  = 4)


def InsertMf():
    conn = sqlite3.connect('7-11.db')
    c = conn.cursor()

    c.execute("Insert into Manufacturer Values (:m_mfkey, :m_name, :m_type, :m_shipkey)",
            {
                    'm_mfkey': m_mfkey.get(),
                    'm_name': m_name.get(),
                    'm_type': m_type.get(),
                    'm_shipkey': m_shipkey.get()
            })

    conn.commit()
    conn.close()


    m_mfkey.delete(0,END)
    m_name.delete(0,END)
    m_type.delete(0,END)
    m_shipkey.delete(0,END)


mfButton = Button(root, text ='Insert Manufacturer', width = 20, command = InsertMf)
mfButton.grid(row = 8, column = 4, columnspan = 2)

###########Products


p_productkey = Entry(root, width = 20)
p_productkey.grid(row = 1, column = 7, padx = 20)

p_productkey_label = Label(root, text = "Product key ")
p_productkey_label.grid(row = 1, column  = 6)

p_type = Entry(root, width = 20)
p_type.grid(row = 2, column = 7, padx = 20)

p_type_label = Label(root, text = "type")
p_type_label.grid(row = 2, column  = 6)


p_name = Entry(root, width = 20)
p_name.grid(row = 3, column = 7, padx = 20)

p_name_label = Label(root, text = "name")
p_name_label.grid(row = 3, column  = 6)


p_supplier = Entry(root, width = 20)
p_supplier.grid(row = 4, column = 7, padx = 20)

p_supplier_label = Label(root, text = "supplier")
p_supplier_label.grid(row = 4, column  = 6)

p_price = Entry(root, width = 20)
p_price.grid(row = 5, column = 7, padx = 20)

p_price_label = Label(root, text = " price ")
p_price_label.grid(row = 5, column  = 6)

p_shipkey = Entry(root, width = 20)
p_shipkey.grid(row = 6, column = 7, padx = 20)

p_shipkey_label = Label(root, text = "shipkey")
p_shipkey_label.grid(row = 6, column  = 6)

p_mfkey = Entry(root, width = 20)
p_mfkey.grid(row = 7, column = 7, padx = 20)

p_mfkey_label = Label(root, text = "mfkey")
p_mfkey_label.grid(row = 7, column  = 6)

def InsertProduct():
    conn = sqlite3.connect('7-11.db')
    c = conn.cursor()

    c.execute("Insert into Product Values (:p_productkey, :p_type,:p_name,:p_supplier,:p_price, :p_shipkey,:p_mfkey)",
            {
                'p_productkey': p_productkey.get(),
                'p_type': p_type.get(),
                'p_name': p_name.get(),
                'p_supplier': p_supplier.get(),
                'p_price': p_price.get(),
                'p_shipkey': p_shipkey.get(),
                'p_mfkey': p_mfkey.get()
            })
    conn.commit()
    conn.close()

    p_productkey.delete(0,END)
    p_type.delete(0,END)
    p_name.delete(0,END)
    p_supplier.delete(0,END)
    p_price.delete(0,END)
    p_shipkey.delete(0,END)
    p_mfkey.delete(0,END)



ProductButton = Button(root, text ='Insert Manufacturer', width = 20, command = InsertProduct)
ProductButton.grid(row = 8, column = 6, columnspan = 2)



###############Shipments
sp_shipkey = Entry(root, width = 20)
sp_shipkey.grid(row = 1, column = 9, padx = 20)

sp_shipkey_label = Label(root, text = "Shipkey")
sp_shipkey_label.grid(row = 1, column  = 8)

sp_date = Entry(root, width = 20)
sp_date.grid(row = 2, column = 9, padx = 20)

sp_date_label = Label(root, text = "Date ")
sp_date_label.grid(row = 2, column  = 8)

sp_priority = Entry(root, width = 20)
sp_priority.grid(row = 3, column = 9, padx = 20)

sp_priority_label = Label(root, text = "priority")
sp_priority_label.grid(row = 3, column  = 8)

sp_mfkey = Entry(root, width = 20)
sp_mfkey.grid(row = 4, column = 9, padx = 20)

sp_mfkey_label = Label(root, text = "mfkey")
sp_mfkey_label.grid(row = 4, column  = 8)

sp_storekey = Entry(root, width = 20)
sp_storekey.grid(row = 5, column = 9, padx = 20)

sp_storekey_label = Label(root, text = "storekey")
sp_storekey_label.grid(row = 5, column  = 8)


def InsertShipment():
    conn = sqlite3.connect('7-11.db')
    c = conn.cursor()

    c.execute("Insert into Shipments Values (:sp_shipkey, :sp_date, :sp_priority, :sp_mfkey, :sp_storekey)",
            {
                'sp_shipkey': sp_shipkey.get(),
                'sp_date': sp_date.get(),
                'sp_priority': sp_priority.get(),
                'sp_mfkey': sp_mfkey.get(),
                'sp_storekey': sp_storekey.get()
            })
    conn.commit()
    conn.close()

    sp_shipkey.delete(0,END)
    sp_date.delete(0,END)
    sp_priority.delete(0,END)
    sp_mfkey.delete(0,END)
    sp_storekey.delete(0,END)


ShipmentButton = Button(root, text ='Insert Shipments', width = 20, command = InsertShipment)
ShipmentButton.grid(row = 8, column = 8, columnspan = 2)



#################Stores


s_storekey = Entry(root, width = 20)
s_storekey.grid(row = 1, column = 11, padx = 20)

s_storekey_label = Label(root, text = "storekey")
s_storekey_label.grid(row = 1, column  = 10)

s_productionkey = Entry(root, width = 20)
s_productionkey.grid(row = 2, column = 11, padx = 20)

s_productionkey_label = Label(root, text = "productionkey")
s_productionkey_label.grid(row = 2, column  = 10)

s_name = Entry(root, width = 20)
s_name.grid(row = 3, column = 11, padx = 20)

s_name_label = Label(root, text = "name")
s_name_label.grid(row = 3, column  = 10)


s_location = Entry(root, width = 20)
s_location.grid(row = 4, column = 11, padx = 20)

s_location_label = Label(root, text = "location")
s_location_label.grid(row = 4, column  = 10)


s_custkey = Entry(root, width = 20)
s_custkey.grid(row = 5, column = 11, padx = 20)

s_custkey_label = Label(root, text = "custkey")
s_custkey_label.grid(row = 5, column  = 10)

s_facultykey = Entry(root, width = 20)
s_facultykey.grid(row = 6, column = 11, padx = 20)

s_facultykey_label = Label(root, text = "facultykey")
s_facultykey_label.grid(row = 6, column  = 10)


def InsertStore():
    conn = sqlite3.connect('7-11.db')
    c = conn.cursor()

    c.execute("Insert Into Stores Values (:s_storekey, :s_productionkey, :s_name, :s_location, :s_custkey, :s_facultykey)",
            {
                's_storekey': s_storekey.get(),
                's_productionkey': s_productionkey.get(),
                's_name': s_name.get(),
                's_location': s_location.get(),
                's_custkey': s_custkey.get(),
                's_facultykey':s_facultykey.get()

            })
    conn.commit()
    conn.close()

    s_storekey.delete(0,END)
    s_productionkey.delete(0,END)
    s_name.delete(0,END)
    s_location.delete(0,END)
    s_custkey.delete(0,END)
    s_facultykey.delete(0,END)

ShipmentButton = Button(root, text ='Insert Stores', width = 20, command = InsertStore)
ShipmentButton.grid(row = 8, column = 10, columnspan = 2)


############################ Starting Queries

UpdateCustomer = Label(root, text = "Update Customer")
UpdateCustomer.grid(row = 15, column = 0, pady = 20)

clicked = StringVar()
clicked.set("attribute")

customerdrop = OptionMenu(root, clicked, "c_name", "c_discount", "c_rewardpkts" )
customerdrop.grid( row = 15, column = 1)
#customerdrop.add_cascade(label = "choose", menu = customerdrop )

From = Label(root, text = "From" )
From.grid(row = 15, column = 2)

CustomerEntry1 = Entry(root, width = 20)
CustomerEntry1.grid(row = 15, column = 3)

To = Label(root, text = "to")
To.grid(row = 15, column = 4 )

CustomerEntry2 = Entry(root, width = 20)
CustomerEntry2.grid(row = 15, column = 5)

def UpdateCust():
    conn = sqlite3.connect('7-11.db')
    c = conn.cursor()

  #  print(clicked.get())
    # print(clicked.get(), CustomerEntry2.get(), clicked.get(), CustomerEntry1.get())

    if clicked.get() == "c_name":
        sql = "Update Customer set c_name = ? where c_name = ?"
        c.execute(sql,[CustomerEntry2.get(), (CustomerEntry1.get())])

    if clicked.get() == "c_discount":
        sql = "Update Customer set c_discount  = ? where c_discount = ?"
        c.execute(sql,[  int(CustomerEntry2.get()),  int(CustomerEntry1.get())])

    if clicked.get() == "c_rewardpkts":
        sql = "Update Customer set c_rewardpkts  = ? where c_rewardpkts = ?"
        c.execute(sql,[  int(CustomerEntry2.get()),  int(CustomerEntry1.get())])
    

    conn.commit()
    conn.close()

    CustomerEntry1.delete(0, END)
    CustomerEntry2.delete(0, END)

UpdateCustomerbut = Button(root, text = "Update", command = UpdateCust)
UpdateCustomerbut.grid(row = 15, column = 6)


UpdateFaculty = Label(root, text = "Update Faculty")
UpdateFaculty.grid(row = 16, column = 0, pady = 20)

clicked1 = StringVar()
clicked1.set("attribute")

Facultydrop = OptionMenu(root, clicked1, "f_name", "f_age", "f_hours" )
Facultydrop.grid( row = 16, column = 1)


From = Label(root, text = "From" )
From.grid(row = 16, column = 2)

FacultyEntry1 = Entry(root, width = 20)
FacultyEntry1.grid(row = 16, column = 3)

To = Label(root, text = "to")
To.grid(row = 16, column = 4 )

FacultyEntry2 = Entry(root, width = 20)
FacultyEntry2.grid(row = 16, column = 5)

def UpdateFac():
    conn = sqlite3.connect('7-11.db')
    c = conn.cursor()

    if clicked1.get() == "f_name":
        sql = "Update Faculty set f_name = ? where f_name = ?"
        c.execute(sql,[FacultyEntry2.get(), (FacultyEntry1.get())])

    if clicked1.get() == "f_age":
        sql = "Update Faculty set f_age  = ? where f_age = ?"
        c.execute(sql,[  int(CustomerEntry2.get()),  int(CustomerEntry1.get())])

    if clicked1.get() == "f_hours":
        sql = "Update Faculty set f_hours  = ? where f_hours = ?"
        c.execute(sql,[  int(CustomerEntry2.get()),  int(CustomerEntry1.get())])

    conn.commit()
    conn.close()

    FacultyEntry1.delete(0,END)
    FacultyEntry2.delete(0,END)

UpdateFacultybut = Button(root, text = "Update", command = UpdateFac)
UpdateFacultybut.grid(row = 16, column = 6)



UpdateMf = Label(root, text = "Update Manufacturer")
UpdateMf.grid(row = 17, column = 0, pady = 20)

clicked2 = StringVar()
clicked2.set("attribute")

Facultydrop = OptionMenu(root, clicked2, "mf_name", "mf_type", "mf_shipkey" )
Facultydrop.grid( row = 17, column = 1)

From = Label(root, text = "From" )
From.grid(row = 17, column = 2)

MfEntry1 = Entry(root, width = 20)
MfEntry1.grid(row = 17, column = 3)

To = Label(root, text = "to")
To.grid(row = 17, column = 4 )

MfEntry2 = Entry(root, width = 20)
MfEntry2.grid(row = 17, column = 5)

def UpdateMaf():
    conn = sqlite3.connect('7-11.db')
    c = conn.cursor()

    if clicked2.get() == "mf_name":
        sql = "Update Manufacturer set m_name = ? where m_name = ?"
        c.execute(sql,[MfEntry2.get(), (MfEntry1.get())])

    if clicked2.get() == "mf_type":
        sql = "Update Manufacturer set m_type = ? where m_type = ?"
        c.execute(sql,[MfEntry2.get(), (MfEntry1.get())])
    if clicked2.get() == "mf_shipkey":
        sql = "Update Manufacturer set m_shipkey  = ? where m_shipkey = ?"
        c.execute(sql,[(MfEntry2.get()),(MfEntry1.get())])

    conn.commit()
    conn.close()

    MfEntry1.delete(0,END)
    MfEntry2.delete(0,END)

UpdateMfbut = Button(root, text = "Update", command = UpdateMaf)
UpdateMfbut.grid(row = 17, column = 6)


UpdateProduct = Label(root, text = "Update Product")
UpdateProduct.grid(row = 18, column = 0, pady = 20)

clicked3 = StringVar()
clicked3.set("attribute")

Productdrop = OptionMenu(root, clicked3, "p_type", "p_name", "p_supplier", "p_price", "p_shipkey", "p_mfkey")
Productdrop.grid( row = 18, column = 1)

From = Label(root, text = "From" )
From.grid(row = 18, column = 2)

pEntry1 = Entry(root, width = 20)
pEntry1.grid(row = 18, column = 3)

To = Label(root, text = "to")
To.grid(row = 18, column = 4 )

pEntry2 = Entry(root, width = 20)
pEntry2.grid(row = 18, column = 5)

def Updatep():
    conn = sqlite3.connect('7-11.db')
    c = conn.cursor()

    if clicked3.get() == "p_type":
        sql = "Update Product set p_type = ? where p_type = ?"
        c.execute(sql,[pEntry2.get(), (pEntry1.get())])

    if clicked3.get() == "p_name":
        sql = "Update Product set p_name = ? where p_name = ?"
        c.execute(sql,[pEntry2.get(), (pEntry1.get())])

    if clicked3.get() == "p_supplier":
        sql = "Update Product set p_supplier = ? where p_supplier = ?"
        c.execute(sql,[pEntry2.get(), (pEntry1.get())])

    if clicked3.get() == "p_price":
        sql = "Update Product set p_price = ? where p_price = ?"
        c.execute(sql,[pEntry2.get(),(pEntry1.get())])

    if clicked3.get() == "p_shipkey":
        sql = "Update Product set p_shipkey = ? where p_shipkey = ?"
        c.execute(sql,[int(pEntry2.get()), int(pEntry1.get())])

    if clicked3.get() == "p_mfkey":
        sql = "Update Product set p_mfkey = ? where p_mfkey = ?"
        c.execute(sql,[int(pEntry2.get()), int(pEntry1.get())])

    conn.commit()
    conn.close()

    pEntry1.delete(0,END)
    pEntry2.delete(0,END)





Updatepbut = Button(root, text = "Update", command = Updatep)
Updatepbut.grid(row = 18, column = 6)


UpdateShipments = Label(root, text = "Update Shipments")
UpdateShipments.grid(row = 19, column = 0, pady = 20)

clicked4 = StringVar()
clicked4.set("attribute")

Shipmentdrop = OptionMenu(root, clicked4, "sp_date", "sp_priority", "sp_storekey", "sp_mfkey")
Shipmentdrop.grid( row = 19, column = 1)


From = Label(root, text = "From" )
From.grid(row = 19, column = 2)

spEntry1 = Entry(root, width = 20)
spEntry1.grid(row = 19, column = 3)

To = Label(root, text = "to")
To.grid(row = 19, column = 4 )

spEntry2 = Entry(root, width = 20)
spEntry2.grid(row = 19, column = 5)


def Updatesp():
    conn = sqlite3.connect('7-11.db')
    c = conn.cursor()

    if clicked4.get() == "sp_priority":
        sql = "Update Shipments set sp_priority = ? where sp_priority = ?"
        c.execute(sql,[spEntry2.get(), (spEntry1.get())])

    if clicked4.get() == "sp_mfkey":
        sql = "Update Shipments set sp_mfkey = ? where sp_mfkey = ?"
        c.execute(sql,[int(spEntry2.get()), int(spEntry1.get())])

    if clicked4.get() == "sp_date":
        sql = "Update Shipments set sp_date = ? where sp_date = ?"
        c.execute(sql,[int(spEntry2.get()), int(spEntry1.get())])

    if clicked4.get() == "sp_storekey":
        sql = "Update Shipments set sp_storekey = ? where sp_storekey = ?"
        c.execute(sql,[int(spEntry2.get()), int(spEntry1.get())])

    conn.commit()
    conn.close()

    spEntry1.delete(0,END)
    spEntry2.delete(0,END)

Updatespbut = Button(root, text = "Update", command = Updatesp)
Updatespbut.grid(row = 19, column = 6)

UpdateStores = Label(root, text = "Update Stores")
UpdateStores.grid(row = 20, column = 0, pady = 20)

clicked5 = StringVar()
clicked5.set("attribute")

Storedrop = OptionMenu(root, clicked5, "s_productionkey", "s_name", "s_location", "s_custkey", "s_facultykey")
Storedrop.grid( row = 20, column = 1)


From = Label(root, text = "From" )
From.grid(row = 20, column = 2)

sEntry1 = Entry(root, width = 20)
sEntry1.grid(row = 20, column = 3)

To = Label(root, text = "to")
To.grid(row = 20, column = 4 )

sEntry2 = Entry(root, width = 20)
sEntry2.grid(row = 20, column = 5)

def Updates():
    conn = sqlite3.connect('7-11.db')
    c = conn.cursor()

    if clicked5.get() == "s_name":
        sql = "Update Stores set s_name = ? where s_name = ?"
        c.execute(sql,[sEntry2.get(), (sEntry1.get())])

    if clicked5.get() == "s_location":
        sql = "Update Stores set s_location = ? where s_location = ?"
        c.execute(sql,[sEntry2.get(), (sEntry1.get())])

    if clicked5.get() == "s_productionkey":
        sql = "Update Stores set s_productionkey = ? where s_productionkey = ?"
        c.execute(sql,[int(sEntry2.get()), int(sEntry1.get())])

    if clicked5.get() == "s_custkey":
        sql = "Update Stores set s_custkey = ? where s_custkey = ?"
        c.execute(sql,[int(sEntry2.get()), int(sEntry1.get())])

    if clicked5.get() == "s_facultykey":
        sql = "Update Stores set s_facultykey = ? where s_facultykey = ?"
        c.execute(sql,[int(sEntry2.get()), int(sEntry1.get())])

    conn.commit()
    conn.close()

    sEntry1.delete(0,END)
    sEntry2.delete(0,END)

Updatespbut = Button(root, text = "Update", command = Updates)
Updatespbut.grid(row = 20, column = 6)

query_label = Label(root, text = '')
query_label.grid(row = 15,rowspan = 10, column = 9, columnspan = 2)

def query1(): 
    
    conn = sqlite3.connect('7-11.db')
    c = conn.cursor()

    c.execute("select p_name from Product where (p_type = 'meat' or p_type = 'seafood') and p_price <50")
    records = c.fetchall()
    #records.strip("(u'")
    #records.strip(")")
    print_cheapmeats = ''
    for record in records:
        record = str(record).strip("(u'") 
        print_cheapmeats += str(record).strip("',)")+"\n"


    query_label.config(text = print_cheapmeats)
   

    conn.commit()
    conn.close()

def query2():
  
    conn = sqlite3.connect('7-11.db')
    c = conn.cursor()
    #print("select f_name from Faculty, Stores where f_storekey = s_storekey and s_storekey = ?", int(SelectEntry1.get()))
    c.execute("select f_name from Faculty, Stores where f_storekey = s_storekey and s_storekey = ?", SelectEntry1.get())
    recordss= c.fetchall()
    #records.strip("(u'")
    #records.strip(")")
    print_cheapmeats = ''
    for record in recordss:
        record = str(record).strip("(u'") 
        print_cheapmeats += str(record).strip("',)")+"\n"


    query_label = Label(root, text = print_cheapmeats)
    query_label.grid(row = 15,rowspan = 10, column = 9, columnspan = 2)

    conn.commit()
    conn.close()

    SelectEntry1.delete(0, END)




Selectquery = Button(root, text ="Finding cheap meat and seafood products", command = query1)
Selectquery.grid( row = 15, column = 7)




Selectquery2 = Button(root, text ="Find all employees of Store %", command = query2)
Selectquery2.grid( row = 16, column = 7)


SelectEntry1 = Entry(root, width = 20)
SelectEntry1.grid(row = 16, column = 8, padx = 20)

def query3():
    
    conn = sqlite3.connect('7-11.db')
    c = conn.cursor()
   
    c.execute("select  distinct m_name from Product, Manufacturer, Shipments where p_mfkey = m_mfkey and p_type = 'beverage' and sp_priority like 'Low%'")
    recordsss= c.fetchall()
    #records.strip("(u'")
    #records.strip(")")
    print_cheapmeats = ''
    for record in recordsss:
        record = str(record).strip("(u'") 
        print_cheapmeats += str(record).strip("',)")+"\n"


    query_label.config(text = print_cheapmeats)
    

    conn.commit()
    conn.close()
    



Selectquery3 = Button(root, text = "Manufacturer with low priority beverages", command = query3)
Selectquery3.grid(row = 17, column = 7)


def query4():
    
    conn = sqlite3.connect('7-11.db')
    c = conn.cursor()
   
    c.execute("select sp_shipkey from Shipments where sp_priority like 'Low%'")
    recordssss= c.fetchall()
    #records.strip("(u'")
    #records.strip(")")
    print_cheapmeats = ''
    for record in recordssss:
        record = str(record).strip("(u'") 
        print_cheapmeats += str(record).strip("',)")+"\n"


    query_label.config(text =print_cheapmeats)
    

    conn.commit()
    conn.close()



Selectquery4 = Button(root, text = "Selecting Low Priority Shipments", command = query4)
Selectquery4.grid(row = 18, column = 7)


# photo = ImageTK.PhotoImage(file = '11-7.png')
# labbel = Label(root)
# labbel.grid(row = 19, column = 7, columnspan = 3)
# img = ImageTK.PhotoImage(file = '11-7.png')
# img = ImageTk.PhotoImage(Image.open("11-7.png"))  
# l=Label(image=img)
# l.pack()


# canv = Canvas(root, width=80, height=80, bg='white')
# canv.grid(row=2, column=3)

# img = PhotoImage(file="small.png")
# canv.create_image(20,20, anchor=NW, image=img)


# image = Image.open("smaller.png")
# photo = ImageTk.PhotoImage(image)
# llabel = Label(root, image=photo)
# llabel.img = photo # this line is not always needed, but include it anyway to prevent bugs
# llabel.pack()


One = Button(root, bg = 'green', width = 4, height = 10)
One.place(x = 900, y= 400)

two = Button(root, bg = 'green', width = 4, height = 10)
two.place(x = 1000, y= 400)

three= Button(root, bg = 'black', width = 10, height = 1)
three.place(x = 1100, y= 450)

four = Button(root, bg = 'red', width = 15, height = 1)
four.place(x = 1200, y= 400)

five = Button(root, bg = 'orange', width = 3, height = 10)
five.place(x = 1300, y= 400)














































root.mainloop()




# def query1():
#     #updating c_discount in table Customer
#     newdiscount = input("Set discount to ")
#     olddiscount = input("From discount ")
#     sql = "update Customer set c_discount = ? where c_discount = ?"
#     c.execute(sql, [newdiscount,olddiscount])
#     conn.commit();

# def query2():
#     c.execute("select max(c_custkey) from Customer")
#     custkey = c.fetchone()[0]
#     custkey = int(custkey)+1
#     #insert Customer
#     name = raw_input("Name of the customer :")
#     discount = input("Discount he/she has :")
#     rewardpkts = input ("Reward points he/ she has ") 
#     sql = "insert into Customer (c_custkey, c_name, c_discount,c_rewardpkts ) values (?,?,?,?)"
#     c.execute(sql,[custkey,name,discount,rewardpkts])
#     conn.commit()

# def query3():
#     #insert faculty
#     c.execute("select max(f_facultykey) from faculty")
#     facultykey = c.fetchone()[0]
#     facultykey  = int(facultykey) +1
#     #insert Customer
#     name = raw_input("Name of the  faculty: ")
#     age = input("how old is the employee: ")
#     hours = input ("How many hours do they work ") 
#     sql = "insert into Faculty (f_facultykey, f_name, f_age, f_hours ) values (?,?,?,?)"
#     c.execute(sql,[facultykey,name,age,hours])
#     conn.commit()

# def query4():
#     #Updating Faculty hour
#     newhour = input("New Hours")
#     oldhour = input("Old Hours")
#     c.execute("update Faculty set f_hours = ? where f_hours = ?", [newhour,oldhour])
#     conn.commit();

# def query5():
#     #updating manufaturer shipkey
#     newshipkey = input("New shipkey")
#     oldshipkey = input("Old shipkey")
#     c.execute("update Manufacturer set m_shipkey = ? where m_shipkey = ?",[newshipkey,oldshipkey]);    
#     conn.commit();

# def query6():
#     #Product prices
#     newprice = input("New Prices")
#     oldprice = input("Old Prices")
#     c.execute("update Product set p_price = ? where p_price = ?", [newprice,oldprice])
#     conn.commit();

# def query7():
#     #Shipments storekey
#     newstore = input("New store")
#     oldstore = input("Old store")
#     c.execute("update Shipments set sp_storekey = ? where sp_storekey = ?", [newstore,oldstore])
#     conn.commit();

# def query8():
#     #Store
#     newfaculty = input("New faculty")
#     oldfaculty = input("Old faculty")
#     c.execute("update Stores set s_facultykey = ? where s_facultykey = ?", [newfaculty,oldfaculty])
#     conn.commit();

# def query9():
#     #delete customer
#     name = raw_input("customer name for deletion ")
#     c.execute("delete from Customer where c_name = ?;", [name])
#     conn.commit();
# def query10():
#     #delete stores
#     name = raw_input("Store name for deletion ")
#     c.execute("delete from Stores where s_name = ?;", [name])
#     conn.commit()

# def query11():
#     #finding cheap product type
#     print 'finding cheap meat and seafood products'
#     c.execute("select p_name from Product where (p_type = 'meat' or p_type = 'seafood') and p_price <50")
#     for row in c.fetchall():
#         print(row[0].encode("utf-8"))

# def query12():
#     print 'finding customers with low discount < 2'
#     c.execute("select c_name from Customer where c_discount < 2")
#     for row in c.fetchall():
#         print(row[0].encode("utf-8"))

# def query13():
#     print "select low priority shipments"
#     c.execute("select sp_shipkey from Shipments where sp_priority like 'Low%'")
#     for row in c.fetchall():
#         print(row[0].encode("utf-8"))

# def query14():
#     print "manufacturers that have beverage products and have a low priority shipment"
#     c.execute("select  distinct m_name from Product, Manufacturer, Shipments where p_mfkey = m_mfkey and p_type = 'beverage' and sp_priority like 'Low%'")
#     for row in c.fetchall():
#         print(row[0].encode("utf-8"))
        
# def query15(): 
#     print "selecting customers that go to Los Angeles store"
#     c.execute("select distinct c_name from Manufacturer, Shipments, Stores, Customer, Product where  s_location = 'Los Angeles'  and  s_custkey = c_custkey")
#     for row in c.fetchall():
#         print(row[0].encode("utf-8"))
        
# def query16():
#     print "Finding seafood products name and location"
#     c.execute("select distinct p_name ,s_location from  Stores,  Product where  s_productionkey = p_productkey and p_type = 'seafood'")
#     for row in c.fetchall():
#         print(row[0].encode("utf-8"))
        
# def query17():
#     print "Selecting faculty members and where they work if they are under 30"
#     c.execute("select f_name, f_age, s_location from Faculty, Stores where s_facultykey = f_facultykey  and f_age < 30")
#     for row in c.fetchall():
#         print(row[0].encode("utf-8"))

# def query18():
#     print "order in ascending order the manufactures that product meat"
#     c.execute("select distinct m_type, m_name from Manufacturer, Stores, Product where p_mfkey = m_mfkey and s_productionkey = p_productkey and m_type ='meat' order by m_mfkey asc")
#     for row in c.fetchall():
#         print(row[0].encode("utf-8"))
        
# def query19():
#     print "Finding urgent shipments with product names and their shipment number"
#     c.execute("select p_name, sp_shipkey, m_name  from Product, Shipments, Manufacturer where p_shipkey = sp_shipkey and sp_priority like 'Urgent%' and m_mfkey = p_mfkey")
#     for row in c.fetchall():
#         print(row[0].encode("utf-8"))

# def query20():
#     print "finding the type of products that are produced by the most manufacturer, and their manufacturer names "
#     c.execute("select m_name, m_type from Manufacturer, (select count(m_type) as max from Manufacturer group by m_type order by count(m_type) desc Limit 1 ) h group by m_type having count(m_type) = h.max")
#     for row in c.fetchall():
#         print(row[0].encode("utf-8"))
        

# def disconnect():
#     print "Closed database successfully?"
#     c.close()
#     conn.close()
#     print "Closed database successfully"

# key = 1

# while (key != "0"):

#   #  key = input("Enter1-10 for Queries, 21 to connect db and 22 to close db: ")
#     print(key)
#     if (key == 1):
#         query1();
#     elif key == 2:
#         query2();
#     elif key == 3:
#         query3();
#     elif key == 4:
#         query4();
#     elif key == 5:
#         query5();
#     elif key == 6:
#         query6();
#     elif key == 7:
#        query7();
#     elif key == 8:
#         query8();
#     elif key == 9:
#         query9();
#     elif key == 10:
#         query10();
#     elif key == 11:
#         query11();
#     elif key == 12:
#         query12();
#     elif key == 13:
#         query13(); 
#     elif key == 14:
#         query14();
#     elif key == 15:
#         query15();  
#     elif key == 16:
#         query16();  
#     elif key == 17:
#         query17(); 
#     elif key == 18:
#         query18(); 
#     elif key == 19:
#         query19(); 
#     elif key == 20:
#         query20();   
#     elif key == 21:
#         print "Opened database successfully?"
#         conn = sqlite3.connect('7-11.db')
#         c = conn.cursor()
#         print "Opened database successfully"
#         null = True
#         x = 0
#     elif key == 22:
#         key = '0';
#         disconnect()
#     else:
#         print "HI?"
#         key = '0';


#c.close();
#conn.close();