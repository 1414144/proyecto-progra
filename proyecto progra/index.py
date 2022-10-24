from tkinter import *
import mysql.connector
from tkinter import ttk
from tkinter import messagebox

v =Tk()
v.title("Registro")
v.geometry("500x400")
v.config(bg="#D3FFC3")
v.resizable(0,0)

conexion=mysql.connector.connect(host="localhost",port="3306",user="root",password="")
bd=conexion.cursor()
bd.execute("CREATE DATABASE IF NOT EXISTS base_de_datos")
bd.close()

conexion=mysql.connector.connect(host="localhost",port="3306",user="root",password="",database="base_de_datos")
bd=conexion.cursor()
bd.execute("CREATE TABLE IF NOT EXISTS login(usuario VARCHAR(25),contraseña VARCHAR(55))")
bd.execute("CREATE TABLE IF NOT EXISTS registro(identificacion VARCHAR(25),nombre_y_apellidos VARCHAR(55),puesto_de_trabajo VARCHAR(55),usuario VARCHAR(55),contraseña VARCHAR(55))")
bd.close()

def registro():
    def agregar_usuario():
     cur=conexion.cursor()
     ide=txt_identificacion.get()
     nom=txt_nombre.get()
     tra=txt_trabajo.get()
     usu=txt_usuario.get()
     con=txt_contraseña.get()
     cur.execute("insert into registro(identificacion,nombre_y_apellidos,puesto_de_trabajo,usuario,contraseña) values('{}','{}','{}','{}','{}')".format(ide,nom,tra,usu,con))
     conexion.commit()
     cur.close()
     messagebox.showinfo(message="El nuevo usuario se guardo de forma exitosa", title="informacion al guardar")
     txt_identificacion.delete(0,END)
     txt_nombre.delete(0,END)
     txt_trabajo.delete(0,END)
     txt_usuario.delete(0,END)
     txt_contraseña.delete(0,END)
     txt_identificacion.focus()

def buscar_usuario():
    cur=conexion.cursor()
    cur.execute("select * from registro")
    datos=cur.fetchall()
    txt_nombre.delete(0,END)
    txt_trabajo.delete(0,END)
    txt_usuario.delete(0,END)
    txt_contraseña.delete(0,END)
    for columna in datos:
        if columna[0]==txt_identificacion.get():
            txt_nombre.insert(0,columna[1])
            txt_trabajo.insert(0,columna[2])
            txt_usuario.insert(0,columna[3])
            txt_contraseña.insert(0,columna[4])
    #txt_codigo.delete(0,END)
    txt_identificacion.focus()
    cur.close()

def limpiar():
    txt_identificacion.delete(0,END)
    txt_nombre.delete(0,END)
    txt_trabajo.delete(0,END)
    txt_usuario.delete(0,END)
    txt_contraseña.delete(0,END)
    txt_identificacion.focus()

def eliminar_usuario():
    cur=conexion.cursor()
    ide=txt_identificacion.get()
    cur.execute("delete from registro where identificacion='{}'".format(ide))
    conexion.commit()
    limpiar()
    cur.close()
    messagebox.showinfo(message="El usuario se borro con exito", title="informacion al eliminar")

def modificar_usuario():
    cur=conexion.cursor()
    modificar_datos=txt_nombre.get(),txt_trabajo.get(),txt_usuario.get(),txt_contraseña.get(),txt_identificacion.get()
    cur.execute("update registro set nombre_y_apellidos=%s, puesto_de_trabajo=%s, usuario=%s, contraseña=%s where identificacion=%s",modificar_datos)
    conexion.commit()
    cur.close()
    messagebox.showinfo(message="El usuario se modifico con exito", title="informacion al actualizar")
    limpiar()

inv = Tk()
inv.title("usuario")
inv.geometry("600x400")
inv.config(bg="#D0B7FF")
inv.resizable(0,0)
etiqueta=Label(inv,font=("arial",18,"bold"),text="registro",bg="#D0B7FF",).place(x=125,y=5)
etiqueta=Label(inv,font=("arial",18,"bold"),text="identificacion:",bg="#D0B7FF",).place(x=15,y=50)
txt_identificacion=Entry(inv,font=("arial",18,"bold"),bg="#FFFFFF")
txt_identificacion.place(x=125,y=50)
txt_identificacion.bind("<Return>",(lambda event:buscar_usuario()))
etiqueta=Label(inv,font=("arial",18,"bold"),text="nombre",bg="#D0B7FF",).place(x=15,y=100)
txt_nombre=Entry(inv,font=("arial",18,"bold"),bg="#FFFFFF")
txt_nombre.place(x=125,y=100)
etiqueuta=Label(inv,font=("arial",18,"bold"),text="trabajo",bg="#D0B7FF",).place(x=15,y=150)
txt_trabajo=Entry(inv,font=("arial",18,"bold"),bg="#FFFFFF")
txt_trabajo.place(x=125,y=150)
etiqueta=Label(inv,font=("arial",18,"bold"),text="usuario",bg="#D0B7FF",).place(x=15,y=200)
txt_usuario=Entry(inv,font=("arial",18,"bold"),bg="#FFFFFF",width=13)
txt_usuario.place(x=217,y=200)
etiqueta=Label(inv,font=("arial",18,"bold"),text="contraseña",bg="#D0B7FF",).place(x=15,y=250)
txt_contraseña=Entry(inv,font=("arial",18,"bold"),bg="#FFFFFF")
txt_contraseña.place(x=125,y=250)
boton_inv2=Button(inv,font=("arial",10,"bold"),text="agregar usuario",width=15,bg="#FFFFFF",command=agregar_usuario).place(x=200,y=300)
boton_inv3=Button(inv,font=("arial",10,"bold"),text="modificar usuario",width=15,bg="#FFFFFF",command=modificar_usuario).place(x=50,y=300)
boton_inv4=Button(inv,font=("arial",10,"bold"),text="eliminar usuario",width=15,bg="#FFFFFF",command=eliminar_usuario).place(x=350,y=300)
boton_inv5=Button(inv,font=("arial",10,"bold"),text="buscar",width=15,bg="#FFFFFF",command=buscar_usuario).place(x=400,y=50)
boton_inv6=Button(inv,font=("arial",10,"bold"),text="cancelar",width=15,bg="#FFFFFF",command=limpiar).place(x=400,y=350)
def login():
        def buscar_usuario():
            cur=conexion.cursor()
            cur.execute("select * from registro")
            datos=cur.fetchall()
        for columna in datos:
            if txt_usuario2 == columna[4]:
             if txt_contraseña2 == columna[5]:
              messagebox.showinfo(message="El usuario existe", title="informacion del usuario")
            else:
             messagebox.showinfo(message="El usuario no existe", title="informacion del usuario")
cur.close()

pre = Tk()
pre.title("login")
pre.geometry("600x500")
pre.config(bg="#FFFFC7")
pre.resizable(0,0)
etiqueta=Label(pre,font=("arial",18,"bold"),text="login",bg="#FFFFC7",).place(x=200,y=5)
etiqueta=Label(pre,font=("arial",18,"bold"),text="usuario",bg="#FFFFC7",).place(x=15,y=50)
txt_usuario2=Entry(pre,font=("arial",18,"bold"),bg="#FFFFFF",width=15,).place(x=200,y=50)
etiqueta=Label(pre,font=("arial",18,"bold"),text="contraseña",bg="#FFFFC7",).place(x=15,y=100)
txt_contraseña2=Entry(pre,font=("arial",18,"bold"),bg="#FFFFFF",width=15).place(x=200,y=100)
boton_pre2=Button(pre,font=("arial",10,"bold"),text="buscar",command=buscar_usuario,width=15,bg="#FFFFFF").place(x=450,y=125)
boton_pre3=Button(pre,font=("arial",10,"bold"),text="cancelar",width=15,bg="#FFFFFF").place(x=450,y=350)
etiqueta=Label(v,font=("century",24,"bold"),text="Biblioteca virtual",bg="#D3FFC3").place(x=125,y=25)

boton_inv=Button(v,font=("century",12,"bold"),text="registro", command=registro,width=15,height=5,bg="#FFFFFF").place(x=50,y=100)

boton_cli=Button(v,font=("century",12,"bold"),text="login", command=login,width=15,height=5,bg="#FFFFFF").place(x=300,y=100)


e=mainloop()