import streamlit as st
import pymysql
import connectmysql as con
from tabulate import tabulate


st.title("CRUD MySQL App with Database")


# connect to database
# call connection
connection = con.connectdb()
cursor = connection.cursor()

# read data from database


def readperson():
    # call connection
    connection = con.connectdb()
    cursor = connection.cursor()

    # อันนี้ทำงานได้
    cursor.execute("select * from person order by id desc")
    persons = cursor.fetchall()
    return persons


def addperson(fullname, email, age):
    try:
        # call connection
        connection = con.connectdb()
        cursor = connection.cursor()
        cursor.execute(
            "insert into person (fullname,email,age) values (%s,%s,%s)", (fullname, email, age))
        connection.commit()
        st.success("เพิ่มข้อมูลเรียบร้อย")
    except pymysql.Error as e:
        print(f'เกิดข้อผิดพลาด : {e}')


def updatePerson(id, fullname, email, age):
    try:
        # call connection
        connection = con.connectdb()
        cursor = connection.cursor()
        cursor.execute(
            "update person set fullname = %s,email = %s ,age = %s where id = %s", (fullname, email, age, id))
        connection.commit()
        st.success("แก้ไขข้อมูลเรียบร้อย")
    except pymysql.Error as e:
        print(f'เกิดข้อผิดพลาด : {e}')


def deletePerson(id):
    try:
        # call connection
        connection = con.connectdb()
        cursor = connection.cursor()
        cursor.execute("delete from person where id = %s", (id,))
        connection.commit()
        st.success("ลบข้อมูลเรียบร้อย")
    except pymysql.Error as e:
        print(f'เกิดข้อผิดพลาด : {e}')


# สร้างเมนู sidebar
menu = ['Home', 'Insert', 'Update', 'Delete']

# ทำตัวเลือก
choice = st.sidebar.selectbox("Menu", menu)

# ถ้าเลือก Home
if choice == 'Home':
    st.subheader("Home")
    personmenu = readperson()
    # check ว่า object มีค่า
    if personmenu:
        # ประกาศตัวแปรเพื่อเอาค่าไปเก็บ
        table_data_person = []
        for row in personmenu:
            # เอาค่ามาเก็บก่อน
            table_data_person.append(row)
        st.table(table_data_person)
    else:
        st.write("ไม่พบข้อมูล")
# insert menu
elif choice == 'Insert':
    st.subheader("Add New Person")
    # สร้าง form
    fullname = st.text_input("Fullname")
    email = st.text_input("Email")
    age = st.number_input("Age", 1, 100, 1)
    # check ว่าปุ่มโดนกด
    if st.button("Add"):
        # check ว่ากรอกข้อมูลครบไหม
        if fullname and email and age:
            st.write("ข้อมูลครบถ้วน")
            addperson(fullname, email, age)
        else:
            st.write("กรอกข้อมูลให้ครบถ้วน")
elif choice == 'Update':
    st.subheader("Update Person Information")
    id = st.number_input("ID", 1)
    fullname = st.text_input("Fullname")
    email = st.text_input("Email")
    age = st.number_input("Age", 1, 100, 1)

    # check ว่าปุ่มโดนกด
    if st.button("Update"):
        # check ว่ากรอกข้อมูลครบไหม
        if id and fullname and email and age:
            updatePerson(id, fullname, email, age)
        else:
            st.write("กรอกข้อมูลให้ครบถ้วน")
elif choice == 'Delete':
    st.subheader("Delete Person")
    id = st.number_input("ID", 1)
    # check ว่าปุ่มโดนกด
    if st.button("Delete"):
        # check ว่ากรอกข้อมูลครบไหม
        if id:
            deletePerson(id)
        else:
            st.write("กรอกข้อมูลให้ครบถ้วน")
