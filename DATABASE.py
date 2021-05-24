from tkinter import *
from typing import Collection
from PIL import Image,ImageTk
import sqlite3

root =Tk()
root.geometry("400x600")

#crate a database or connect to one
conn = sqlite3.connect('address_book.db')
  
#create a cursor
c = conn.cursor()

#create table
#c.execute("""CREATE TABLE addresses (
      #  first_name text,
       # last_name text,
        #address text,
        #city text,
        #state text,
       # zipcode integer
       # )""")

def update():
        conn = sqlite3.connect('address_book.db')
        #create a cursor
        
        
        c = conn.cursor()
        record_id = delete_box.get()

        c.execute("""UPDATE addresses SET 
                first_name = :first,
                last_name = :last,
                address = :address,
                city = :city,
                state = :state,
                zipcode = :zipcode

                WHERE oid = :oid""",
                {'first':f_name_editor.get(),
                'last':l_name_editor.get(),
                'address':address_editor.get(),
                'city':city_editor.get(),
                'state':state_editor.get(),
                'zipcode':zipcode_editor.get(),
                'oid':record_id
                })   
        

        conn.commit() 
        #close connections
        conn.close()
        editor.destroy()


def edit():
        global editor
        editor =Tk()
        editor.title('Update a record')
        editor.geometry("400x400")

        conn = sqlite3.connect('address_book.db')
        #create a cursor
        c = conn.cursor()
        record_id =delete_box.get()
        c.execute("SELECT * FROM addresses WHERE oid = "+ record_id)
        records = c.fetchall()

        #Create global variables for text boxes
        global f_name_editor
        global l_name_editor
        global address_editor
        global city_editor
        global state_editor
        global zipcode_editor

        #create text boxes
        f_name_editor= Entry(editor, width = 30)
        f_name_editor.grid(row = 0, column =1, padx = 20, pady=(10,0))
        l_name_editor= Entry(editor, width = 30)
        l_name_editor.grid(row = 1, column =1, padx = 20)
        address_editor = Entry(editor, width = 30)
        address_editor.grid(row =2, column =1, padx = 20)
        city_editor = Entry(editor, width = 30)
        city_editor.grid(row = 3, column =1, padx = 20)
        state_editor = Entry(editor, width = 30)
        state_editor.grid(row = 4 ,column =1, padx = 20)
        zipcode_editor = Entry(editor, width = 30)
        zipcode_editor.grid(row = 5, column =1, padx = 20)
        
        #create Text Box Labels

        f_name_lbl = Label(editor, text = "First Name")
        f_name_lbl.grid(row = 0, column=0, pady = 10)
        l_name_lbl = Label(editor, text = "Last Name")
        l_name_lbl.grid(row = 1, column=0)
        address_lbl = Label(editor, text = "Address")
        address_lbl .grid(row =2, column=0)
        city_lbl = Label(editor, text = "city")
        city_lbl.grid(row = 3, column=0)
        state_lbl = Label(editor, text = "State")
        state_lbl.grid(row = 4, column=0)
        zipcode_lbl = Label(editor, text = "Zipcode")
        zipcode_lbl.grid(row =5, column=0)
        

        for record in records: 

                f_name_editor.insert(0,record[0])
                l_name_editor.insert(0,record[1])
                address_editor.insert(0,record[2])
                city_editor.insert(0,record[3])
                state_editor.insert(0,record[4])
                zipcode_editor.insert(0,record[5])

        save_btn = Button(editor, text = "Save Record",command=update)
        save_btn.grid(row = 6, column = 0, columnspan =2,padx =10, pady = 10, ipadx =145)

#create function to delte a record
def delete():
        conn = sqlite3.connect('address_book.db')

        #create a cursor
        c = conn.cursor()
        c.execute("DELETE FROM addresses WHERE oid= " + delete_box.get())
        delete_box.delete(0,END)

        conn.commit()

        #close connections
        conn.close()

#submit Function for database
def submit():
        conn = sqlite3.connect('address_book.db')

        #create a cursor
        c = conn.cursor()

        #insert into tabe
        c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city,:state,:zipcode)",

                {
                'f_name': f_name.get(),
                'l_name': l_name.get(),
                'address': address.get(),
                'city': city.get(),
                'state': state.get(),
                'zipcode': zipcode.get()
                })

        #commit changes
        conn.commit()
        #close connections
        conn.close()

         #clear the textboxes
        f_name.delete(0,END)
        l_name.delete(0,END)
        address.delete(0,END)
        city.delete(0,END)
        state.delete(0,END)
        zipcode.delete(0,END)

def query():
        conn = sqlite3.connect('address_book.db')
        #create a cursor
        c = conn.cursor()
        c.execute("SELECT *,oid FROM addresses")
        records = c.fetchall()
        #Loop through results
        print_records = ''

        for record in records:
                #print_records+= str(record) + "\n"
                print_records+= str(record[0]) + " " + str(record[1]) + " " + "\t" + str(record[6])+ "\n"
        lbl=Label(root, text=print_records)
        lbl.grid(row=12, column = 0,columnspan=3)
        #commit changes
        conn.commit()
        #close connections
        conn.close()

#create text boxes
f_name = Entry(root, width = 30)
f_name.grid(row = 0, column =1, padx = 20, pady=(10,0))
l_name = Entry(root, width = 30)
l_name.grid(row = 1, column =1, padx = 20)
address = Entry(root, width = 30)
address.grid(row =2, column =1, padx = 20)
city = Entry(root, width = 30)
city.grid(row = 3, column =1, padx = 20)
state = Entry(root, width = 30)
state.grid(row = 4 ,column =1, padx = 20)
zipcode = Entry(root, width = 30)
zipcode.grid(row = 5, column =1, padx = 20)
delete_box = Entry(root, width = 30)
delete_box.grid(row = 9, column =1)

#create Text Box Labels

f_name_lbl = Label(root, text = "First Name")
f_name_lbl.grid(row = 0, column=0, pady = 10)
l_name_lbl = Label(root, text = "Last Name")
l_name_lbl.grid(row = 1, column=0)
address_lbl = Label(root, text = "Address")
address_lbl .grid(row =2, column=0)
city_lbl = Label(root, text = "city")
city_lbl.grid(row = 3, column=0)
state_lbl = Label(root, text = "State")
state_lbl.grid(row = 4, column=0)
zipcode_lbl = Label(root, text = "Zipcode")
zipcode_lbl.grid(row =5, column=0)
delete_box_lbl = Label(root, text = "Select Id")
delete_box_lbl.grid(row =9, column=0,pady=5)

#create submit button
btn = Button(root,text = "Add record to Database",command=submit)
btn.grid(row=6, column = 0, columnspan=2, padx = 10, pady = 10, ipadx=100)

#create a query button
query_btn = Button(root, text = "Show Record",command=query)
query_btn.grid(row = 7, column = 0, columnspan =2,padx =10, pady = 10, ipadx =137)

#CREATE A DELETE BUTTON
del_btn = Button(root, text = "DELETE Record",command=delete)
del_btn.grid(row = 10, column = 0, columnspan =2,padx =10, pady = 10, ipadx =136)

#create an update button
edit_btn = Button(root, text = "Edit Record",command=edit)
edit_btn.grid(row = 11, column = 0, columnspan =2,padx =10, pady = 10, ipadx =143)

#commit changes
conn.commit()
#close connections
conn.close()

root.mainloop()