import sqlite3 #esto es para agragar la libreria que no spermite acceder a sqlite
#conn = sqlite3.connect("data1.db") # esto es hace porque el archivo esta contenido en la misma carpeta 
#cur= conn.cursor() #variable cursor
#sql= """insert into person(name,age,contac) values(?,?,?)"""#esto nos permite ingresar los archivos a la base de datos por parametro
#cur.execute(sql,(name,age,contac))

def agregardata(): 
    name = input("ingrese el nombre de usuario: ")
    age = int(input("ingrese su edad: "))
    contac = input("ingrese su correo de contacto: ")
    conn=sqlite3.connect("data1.db")
    cur= conn.cursor()
    sql= """insert into person (name,age,contac) values(?,?,?)"""
    cur.execute(sql,(name,age,contac))
    conn.commit()
    conn.close
    return

agregardata()
