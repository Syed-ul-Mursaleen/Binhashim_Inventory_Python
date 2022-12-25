from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk
import tkinter
from tkinter import messagebox
import sqlite3

# PRODUCT_NAME = StringVar()
# PRODUCT_PRICE = IntVar()
# PRODUCT_QTY = IntVar()
# SEARCH = StringVar()


class GUI:
    def maingui(self):
        global Entry1 , Entry1_3,top
        top = Tk()
        top.geometry("615x598+370+49")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(1, 1)
        top.title("BinHashim Pharmacy")
        top.configure(background="#ffffff")

        Frame1 = tk.Frame(top)
        Frame1.place(relx=-0.016, rely=0.0, relheight=0.328, relwidth=1.033)

        Frame1.configure(relief='groove')
        photo=PhotoImage(file='logo.png')
        framepic=Label(Frame1,image=photo)
        framepic.pack()
        Frame1.configure(borderwidth="2")
        Frame1.configure(relief="groove")
        Frame1.configure(background="#ffffff")

        Label1 = tk.Label(top)
        Label1.place(relx=0.309, rely=0.355, height=54, width=233)
        Label1.configure(activebackground="#f9f9f9")
        Label1.configure(activeforeground="black")
        Label1.configure(background="#ffffff")
        Label1.configure(disabledforeground="#a3a3a3")
        Label1.configure(font=10)
        Label1.configure(font="-family Rockwell -size 16 -weight bold -slant roman -underline 0 -overstrike 0")
        Label1.configure(foreground="#004080")
        Label1.configure(highlightbackground="#d9d9d9")
        Label1.configure(highlightcolor="black")
        Label1.configure(text='''LOGIN/REGISTER''')


        Label2_1 = tk.Label(top)
        Label2_1.place(relx=0.163, rely=0.619, height=33, width=114)
        Label2_1.configure(activebackground="#f9f9f9")
        Label2_1.configure(activeforeground="black")
        Label2_1.configure(background="#ffffff")
        Label2_1.configure(disabledforeground="#a3a3a3")
        Label2_1.configure(font=10)
        Label2_1.configure(font="-family Rockwell -size 12 -weight bold -slant roman -underline 0 -overstrike 0")
        Label2_1.configure(foreground="#004080")
        Label2_1.configure(highlightbackground="#d9d9d9")
        Label2_1.configure(highlightcolor="black")
        Label2_1.configure(text='''PASSWORD''')

        Label2_2 = tk.Label(top)
        Label2_2.place(relx=0.163, rely=0.532, height=32, width=114)
        Label2_2.configure(activebackground="#f9f9f9")
        Label2_2.configure(activeforeground="black")
        Label2_2.configure(background="#ffffff")
        Label2_2.configure(disabledforeground="#a3a3a3")
        Label2_2.configure(font="-family Rockwell -size 12 -weight bold -slant roman -underline 0 -overstrike 0")
        Label2_2.configure(foreground="#004080")
        Label2_2.configure(highlightbackground="#d9d9d9")
        Label2_2.configure(highlightcolor="black")
        Label2_2.configure(text='''USER''')

        Entry1 = tk.Entry(top)
        Entry1.place(relx=0.374, rely=0.532, height=30, relwidth=0.283)
        Entry1.configure(background="white")
        Entry1.configure(disabledforeground="#a3a3a3")
        Entry1.configure(font="TkFixedFont")
        Entry1.configure(foreground="#000000")
        Entry1.configure(insertbackground="black")

        Entry1_3 = tk.Entry(top)
        Entry1_3.place(relx=0.374, rely=0.619, height=30, relwidth=0.283)
        Entry1_3.configure(background="white")
        Entry1_3.configure(disabledforeground="#a3a3a3")
        Entry1_3.configure(font="TkFixedFont")
        Entry1_3.configure(foreground="#000000")
        Entry1_3.configure(highlightbackground="#d9d9d9")
        Entry1_3.configure(highlightcolor="black")
        Entry1_3.configure(insertbackground="black")
        Entry1_3.configure(selectbackground="#c4c4c4")
        Entry1_3.configure(selectforeground="black")

        Button1 = tk.Button(top, command = login)
        Button1.place(relx=0.374, rely=0.779, height=34, width=67)
        Button1.configure(activebackground="#ececec")
        Button1.configure(activeforeground="#000000")
        Button1.configure(background="#004080")
        Button1.configure(disabledforeground="#a3a3a3")
        Button1.configure(font="-family Rockwell -size 10 -weight bold -slant roman -underline 0 -overstrike 0")
        Button1.configure(foreground="#ffffff")
        Button1.configure(highlightbackground="#d9d9d9")
        Button1.configure(highlightcolor="black")
        Button1.configure(pady="0")
        Button1.configure(text='''LOGIN''')

        Button1_4 = tk.Button(top, command = register)
        Button1_4.place(relx=0.537, rely=0.779, height=34, width=97)
        Button1_4.configure(activebackground="#ececec")
        Button1_4.configure(activeforeground="#000000")
        Button1_4.configure(background="#004080")
        Button1_4.configure(disabledforeground="#a3a3a3")
        Button1_4.configure(font="-family Rockwell -size 10 -weight bold -slant roman -underline 0 -overstrike 0")
        Button1_4.configure(foreground="#ffffff")
        Button1_4.configure(highlightbackground="#d9d9d9")
        Button1_4.configure(highlightcolor="black")
        Button1_4.configure(pady="0")
        Button1_4.configure(text='''REGISTER''')
        top.mainloop()


class inventory:
    def invgui(self):
        global tree,searchentry
        top2 = Tk()
        top2.geometry("862x600+162+67")
        top2.minsize(120, 1)
        top2.maxsize(1370, 749)
        top2.resizable(0, 0)
        top2.title("BINHASHIM PHARMACY INVENTORY SYSTEM")
        top2.configure(background="#ffffff")

        Frame1 = tk.Frame(top2)
        Frame1.place(relx=0.0, rely=0.0, relheight=0.225, relwidth=1.002)
        Frame1.configure(relief='groove')
        Frame1.configure(borderwidth="2")
        Frame1.configure(relief="groove")
        Frame1.configure(background="#ffffff")
        photo = PhotoImage(file='logo.png')
        framepic = Label(Frame1, image=photo)
        framepic.pack()

        Label1 = tk.Label(top2)
        Label1.place(relx=0.046, rely=0.3, height=21, width=113)
        Label1.configure(background="#ffffff")
        Label1.configure(disabledforeground="#a3a3a3")
        Label1.configure(font="-family Rockwell -size 13 -weight bold -slant roman -underline 0 -overstrike 0")
        Label1.configure(font=12)
        Label1.configure(foreground="#004080")
        Label1.configure(text='''SEARCH''')

        searchentry = tk.Entry(top2)
        searchentry.place(relx=0.023, rely=0.367, height=30, relwidth=0.179)
        searchentry.configure(background="white")
        searchentry.configure(disabledforeground="#a3a3a3")
        searchentry.configure(font="TkFixedFont")
        searchentry.configure(foreground="#000000")
        searchentry.configure(insertbackground="black")

        Search = tk.Button(top2,command=Searchdata)
        Search.place(relx=0.058, rely=0.45, height=34, width=97)
        Search.configure(activebackground="#ececec")
        Search.configure(activeforeground="#000000")
        Search.configure(background="#004080")
        Search.configure(disabledforeground="#a3a3a3")
        Search.configure(font="-family Rockwell -size 12 -weight bold -slant roman -underline 0 -overstrike 0")
        Search.configure(foreground="#ffffff")
        Search.configure(highlightbackground="#d9d9d9")
        Search.configure(highlightcolor="black")
        Search.configure(pady="0")
        Search.configure(text='''SEARCH''')

        add = tk.Button(top2,command =addobj.addproduct)
        add.place(relx=0.058, rely=0.533, height=34, width=97)
        add.configure(activebackground="#ececec")
        add.configure(activeforeground="#000000")
        add.configure(background="#004080")
        add.configure(disabledforeground="#a3a3a3")
        add.configure(font="-family Rockwell -size 12 -weight bold -slant roman -underline 0 -overstrike 0")
        add.configure(foreground="#ffffff")
        add.configure(highlightbackground="#d9d9d9")
        add.configure(highlightcolor="black")
        add.configure(pady="0")
        add.configure(text='''ADD''')

        delete = tk.Button(top2,command= Delete)
        delete.place(relx=0.058, rely=0.617, height=34, width=97)
        delete.configure(activebackground="#ececec")
        delete.configure(activeforeground="#000000")
        delete.configure(background="#004080")
        delete.configure(disabledforeground="#a3a3a3")
        delete.configure(font="-family Rockwell -size 12 -weight bold -slant roman -underline 0 -overstrike 0")
        delete.configure(foreground="#ffffff")
        delete.configure(highlightbackground="#d9d9d9")
        delete.configure(highlightcolor="black")
        delete.configure(pady="0")
        delete.configure(text='''DELETE''')

        modify = tk.Button(top2,command = modifyproduct)
        modify.place(relx=0.058, rely=0.7, height=34, width=97)
        modify.configure(activebackground="#ececec")
        modify.configure(activeforeground="#000000")
        modify.configure(background="#004080")
        modify.configure(disabledforeground="#a3a3a3")
        modify.configure(font="-family Rockwell -size 12 -weight bold -slant roman -underline 0 -overstrike 0")
        modify.configure(foreground="#ffffff")
        modify.configure(highlightbackground="#d9d9d9")
        modify.configure(highlightcolor="black")
        modify.configure(pady="0")
        modify.configure(text='''MODIFY''')

        Reset = tk.Button(top2,command=resetdata)
        Reset.place(relx=0.058, rely=0.783, height=34, width=97)
        Reset.configure(activebackground="#ececec")
        Reset.configure(activeforeground="#000000")
        Reset.configure(background="#004080")
        Reset.configure(disabledforeground="#a3a3a3")
        Reset.configure(font="-family Rockwell -size 12 -weight bold -slant roman -underline 0 -overstrike 0")
        Reset.configure(foreground="#ffffff")
        Reset.configure(highlightbackground="#d9d9d9")
        Reset.configure(highlightcolor="black")
        Reset.configure(pady="0")
        Reset.configure(text='''RESET''')

        Label1_4 = tk.Label(top2)
        Label1_4.place(relx=0.441, rely=0.25, height=31, width=254)
        Label1_4.configure(activebackground="#f9f9f9")
        Label1_4.configure(activeforeground="black")
        Label1_4.configure(background="#ffffff")
        Label1_4.configure(disabledforeground="#a3a3a3")
        Label1_4.configure(font="-family Rockwell -size 14 -weight bold -slant roman -underline 0 -overstrike 0")
        Label1_4.configure(foreground="#004080")
        Label1_4.configure(highlightbackground="#d9d9d9")
        Label1_4.configure(highlightcolor="black")
        Label1_4.configure(text='''INVENTORY ITEMS''')

        MidViewForm = Frame(top2, width=600)
        MidViewForm.place(x=300, y=200)
        scrollbarx = Scrollbar(MidViewForm, orient=HORIZONTAL)
        scrollbary = Scrollbar(MidViewForm, orient=VERTICAL)
        tree = ttk.Treeview(MidViewForm, columns=("ProductID", "Product Name", "Product Qty", "Product Price"),
                            selectmode="extended", height=17, yscrollcommand=scrollbary.set,
                            xscrollcommand=scrollbarx.set)
        scrollbary.config(command=tree.yview)
        scrollbary.pack(side=RIGHT, fill=Y)
        scrollbarx.config(command=tree.xview)
        scrollbarx.pack(side=BOTTOM, fill=X)
        tree.heading('ProductID', text="ProductID", anchor=W)
        tree.heading('Product Name', text="Product Name", anchor=W)
        tree.heading('Product Qty', text="Product Qty", anchor=W)
        tree.heading('Product Price', text="Product Price", anchor=W)
        tree.column('#0', stretch=NO, minwidth=0, width=0)
        tree.column('#1', stretch=NO, minwidth=0, width=0)
        tree.column('#2', stretch=NO, minwidth=0, width=200)
        tree.column('#3', stretch=NO, minwidth=0, width=120)
        tree.column('#4', stretch=NO, minwidth=0, width=120)
        tree.pack()
        DisplayData()
        top2.mainloop()

class Addwindow:
    def addproduct(self):
        global Product_ent,priceEnt,quantityent
        top1= Tk()
        top1.geometry("600x450+679+290")
        top1.minsize(148, 1)
        top1.maxsize(1924, 1055)
        top1.resizable(1, 1)
        top1.title("ADD PRODUCT ")
        top1.configure(background="#ffffff")

        Label1 = tk.Label(top1)
        Label1.place(relx=0.333, rely=0.067, height=36, width=212)
        Label1.configure(background="#ffffff")
        Label1.configure(disabledforeground="#a3a3a3")
        Label1.configure(font=10)
        Label1.configure(foreground="#004080")
        Label1.configure(text='''ADD PRODUCT''')

        Product_ent = tk.Entry(top1)
        Product_ent.place(relx=0.383, rely=0.222, height=34, relwidth=0.423)

        Product_ent.configure(background="white")
        Product_ent.configure(disabledforeground="#a3a3a3")
        Product_ent.configure(font=11)
        Product_ent.configure(foreground="#000000")
        Product_ent.configure(insertbackground="black")

        quantityent = tk.Entry(top1)
        quantityent.place(relx=0.383, rely=0.378, height=34, relwidth=0.423)

        quantityent.configure(background="white")
        quantityent.configure(disabledforeground="#a3a3a3")
        quantityent.configure(font=11)
        quantityent.configure(foreground="#000000")
        quantityent.configure(insertbackground="black")

        priceEnt = tk.Entry(top1)
        priceEnt.place(relx=0.383, rely=0.556,height=34, relwidth=0.423)
        priceEnt.configure(background="white")
        priceEnt.configure(disabledforeground="#a3a3a3")
        priceEnt.configure(font=11)
        priceEnt.configure(foreground="#000000")
        priceEnt.configure(insertbackground="black")

        Label2 = tk.Label(top1)
        Label2.place(relx=0.05, rely=0.222, height=36, width=162)
        Label2.configure(background="#ffffff")
        Label2.configure(disabledforeground="#a3a3a3")
        Label2.configure(font=9)
        Label2.configure(foreground="#004080")
        Label2.configure(text='''PRODUCT NAME''')

        Label3 = tk.Label(top1)
        Label3.place(relx=0.1, rely=0.378, height=36, width=112)
        Label3.configure(background="#ffffff")
        Label3.configure(disabledforeground="#a3a3a3")
        Label3.configure(font=9)
        Label3.configure(foreground="#004080")
        Label3.configure(text='''QUANTITY''')

        Label4 = tk.Label(top1)
        Label4.place(relx=0.117, rely=0.533, height=36, width=92)
        Label4.configure(background="#ffffff")
        Label4.configure(disabledforeground="#a3a3a3")
        Label4.configure(font=9)
        Label4.configure(foreground="#004080")
        Label4.configure(text='''PRICE''')

        Add_Btn = tk.Button(top1,command =AddNew)
        Add_Btn.place(relx=0.5, rely=0.711, height=43, width=106)
        Add_Btn.configure(activebackground="#ececec")
        Add_Btn.configure(activeforeground="#000000")
        Add_Btn.configure(background="#004080")
        Add_Btn.configure(disabledforeground="#a3a3a3")
        Add_Btn.configure(font=9)
        Add_Btn.configure(foreground="#ffffff")
        Add_Btn.configure(highlightbackground="#d9d9d9")
        Add_Btn.configure(highlightcolor="black")
        Add_Btn.configure(pady="0")
        Add_Btn.configure(text='''ADD''')

        top1.mainloop()
class Modifywindow:
    def editproduct(self):
        global Product_ent_edit,priceEnt_edit,quantityent_edit
        top3= Tk()
        top3.geometry("600x450+679+290")
        top3.minsize(148, 1)
        top3.maxsize(1924, 1055)
        top3.resizable(1, 1)
        top3.title("ADD PRODUCT ")
        top3.configure(background="#ffffff")

        Label1 = tk.Label(top3)
        Label1.place(relx=0.333, rely=0.067, height=36, width=212)
        Label1.configure(background="#ffffff")
        Label1.configure(disabledforeground="#a3a3a3")
        Label1.configure(font=10)
        Label1.configure(foreground="#004080")
        Label1.configure(text='''MODIFY PRODUCT''')

        Product_ent_edit = tk.Entry(top3)
        Product_ent_edit.place(relx=0.383, rely=0.222, height=34, relwidth=0.423)

        Product_ent_edit.configure(background="white")
        Product_ent_edit.configure(disabledforeground="#a3a3a3")
        Product_ent_edit.configure(font=11)
        Product_ent_edit.configure(foreground="#000000")
        Product_ent_edit.configure(insertbackground="black")
        Product_ent_edit.insert(0,pname_data1)
        Product_ent_edit.configure(state = "disabled")

        quantityent_edit = tk.Entry(top3)
        quantityent_edit.place(relx=0.383, rely=0.378, height=34, relwidth=0.423)

        quantityent_edit.configure(background="white")
        quantityent_edit.configure(disabledforeground="#a3a3a3")
        quantityent_edit.configure(font=11)
        quantityent_edit.configure(foreground="#000000")
        quantityent_edit.configure(insertbackground="black")
        quantityent_edit.insert(0,pquantity_data2)

        priceEnt_edit = tk.Entry(top3)
        priceEnt_edit.place(relx=0.383, rely=0.556,height=34, relwidth=0.423)
        priceEnt_edit.configure(background="white")
        priceEnt_edit.configure(disabledforeground="#a3a3a3")
        priceEnt_edit.configure(font=11)
        priceEnt_edit.configure(foreground="#000000")
        priceEnt_edit.configure(insertbackground="black")
        priceEnt_edit.insert(0,pprice_data3)

        Label2 = tk.Label(top3)
        Label2.place(relx=0.05, rely=0.222, height=36, width=162)
        Label2.configure(background="#ffffff")
        Label2.configure(disabledforeground="#a3a3a3")
        Label2.configure(font=9)
        Label2.configure(foreground="#004080")
        Label2.configure(text='''PRODUCT NAME''')

        Label3 = tk.Label(top3)
        Label3.place(relx=0.1, rely=0.378, height=36, width=112)
        Label3.configure(background="#ffffff")
        Label3.configure(disabledforeground="#a3a3a3")
        Label3.configure(font=9)
        Label3.configure(foreground="#004080")
        Label3.configure(text='''QUANTITY''')

        Label4 = tk.Label(top3)
        Label4.place(relx=0.117, rely=0.533, height=36, width=92)
        Label4.configure(background="#ffffff")
        Label4.configure(disabledforeground="#a3a3a3")
        Label4.configure(font=9)
        Label4.configure(foreground="#004080")
        Label4.configure(text='''PRICE''')

        Edit_Btn = tk.Button(top3,command = edit_product)
        Edit_Btn.place(relx=0.5, rely=0.711, height=43, width=106)
        Edit_Btn.configure(activebackground="#ececec")
        Edit_Btn.configure(activeforeground="#000000")
        Edit_Btn.configure(background="#004080")
        Edit_Btn.configure(disabledforeground="#a3a3a3")
        Edit_Btn.configure(font=9)
        Edit_Btn.configure(foreground="#ffffff")
        Edit_Btn.configure(highlightbackground="#d9d9d9")
        Edit_Btn.configure(highlightcolor="black")
        Edit_Btn.configure(pady="0")
        Edit_Btn.configure(text='''MODIFY''')

        top3.mainloop()

def modifyproduct():
    global pname_data1, pquantity_data2,pprice_data3
    if not tree.selection():
        print("ERROR")
    else:
        result = tkinter.messagebox.askquestion('BinHashim Inventory System',
                                                'Are you sure you want to Edit this record?',
                                                icon="warning")
        if result == 'yes':

            cursItem = tree.focus()
            contents = (tree.item(cursItem))
            selecteditem = contents['values']
            Database()
            pname = cursor.execute("SELECT product_name FROM `product` WHERE `product_id` = %d" % selecteditem[0])
            pname_data1 = pname.fetchall()
            pquantity = cursor.execute("SELECT product_qty FROM `product` WHERE `product_id` = %d" % selecteditem[0])
            pquantity_data2 = pquantity.fetchall()
            pprice = cursor.execute("SELECT product_price FROM `product` WHERE `product_id` = %d" % selecteditem[0])
            pprice_data3 = pprice.fetchall()
            modifyobj.editproduct()

def edit_product():
    Database()
    cursor.execute('''UPDATE product SET
                    product_qty=:p_q,
                    product_price=:p_p
                    WHERE product_name = :p_n''',
                   {'p_q':quantityent_edit.get(),
                    'p_p':priceEnt_edit.get(),
                    'p_n':Product_ent_edit.get()
                   }
                   )
    connection.commit()
    Product_ent_edit.delete("0", END)
    quantityent_edit.delete("0", END)
    priceEnt_edit.delete("0", END)

    cursor.close()
    connection.close()
    for i in tree.get_children():
        tree.delete(i)
    DisplayData()


def Database():
    global connection, cursor
    connection = sqlite3.connect("pythontut.db")
    cursor = connection.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS `admin` (admin_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, username TEXT, password TEXT)")
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS `product` (product_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, product_name TEXT, product_qty TEXT, product_price TEXT)")
    cursor.execute("SELECT * FROM `admin` WHERE `username` = 'admin' AND `password` = 'admin'")
    if cursor.fetchone() is None:
        cursor.execute("INSERT INTO `admin` (username, password) VALUES('admin', 'admin')")
        connection.commit()


def Searchdata():
    if searchentry.get() != "":
        tree.delete(*tree.get_children())
        Database()
        cursor.execute("SELECT * FROM `product` WHERE `product_name` LIKE ?", ('%' + str(searchentry.get()) + '%',))
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        connection.close()

def DisplayData():
    Database()
    cursor.execute("SELECT * FROM `product`")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    connection.close()

def Delete():
    if not tree.selection():
        print("ERROR")
    else:
        result = tkinter.messagebox.askquestion('BinHashim Inventory System', 'Are you sure you want to delete this record?',
                                          icon="warning")
        if result == 'yes':
            curItem = tree.focus()
            contents = (tree.item(curItem))
            selecteditem = contents['values']
            tree.delete(curItem)
            Database()
            cursor.execute("DELETE FROM `product` WHERE `product_id` = %d" % selecteditem[0])
            connection.commit()
            cursor.close()
            connection.close()



def AddNew():
    Database()

    cursor.execute("INSERT INTO `product` (product_name, product_qty, product_price) VALUES(?, ?, ?)",
                   (str(Product_ent.get()), int(quantityent.get()), int(priceEnt.get())))
    connection.commit()
    Product_ent.delete("0",END)
    quantityent.delete("0",END)
    priceEnt.delete("0",END)
    cursor.close()
    connection.close()
    for i in tree.get_children():
        tree.delete(i)
    DisplayData()
def resetdata():
    for i in tree.get_children():
        tree.delete(i)
    DisplayData()
def login():
    ID = Entry1.get()
    Pass = Entry1_3.get()
    global User
    for i in range(3000):
        infile = open("login.txt", 'r+')
        content = infile.read()
        listofidpass = content.split()
        if ID not in listofidpass:
            tkinter.messagebox.showinfo("Error", "Access denied, Invalid Username")
            break
        else:
            pwindex = listofidpass.index(ID) + 1

        if listofidpass[pwindex] == Pass:
            User = ID
            tkinter.messagebox.showinfo("Login", "Logged In Successfully")
            top.destroy()
            objinv.invgui()

            break
        else:
            tkinter.messagebox.showinfo("Error", "Access denied, Invalid Password")
            break

def register():
    Username = Entry1.get()
    Pass = Entry1_3.get()
    infile = open("login.txt", 'r+')
    content = infile.read()
    listofidpass = content.split()
    if Username in listofidpass:
        tkinter.messagebox.showinfo("Error", "User Already Exist")
    elif (Username == "") or (Pass == ""):
        tkinter.messagebox.showinfo("Error", "InValid Data Entered")
    else:
        infile = open('login.txt', 'r+')
        content = infile.read()
        infile.write(" {0} {1}".format(Username, Pass))
        tkinter.messagebox.showinfo("Success", "Customer Registered Successfully")
        infile.close()
modifyobj = Modifywindow()
objinv = inventory()
addobj = Addwindow()
obj = GUI()
obj.maingui()





