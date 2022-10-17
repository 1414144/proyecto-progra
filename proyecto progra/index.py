from tkinter import *

m = 10 
print(m)

#-------------ventana_usuario---------------#
u=Tk()
u.title("agregar usuario")
u.geometry("900x700")
u.config(bg="#B4C7E7")
u.resizable(0,0)

#-------------Label_usuario-----------------------------------#

etiqueta=Label(u,font=("arial",18,"bold"),text="identificacion:",bg="#B4C7E7").place(x=25,y=100)

etiqueta=Label(u,font=("arial",18,"bold"),text="nombre y apellido:",bg="#B4C7E7").place(x=25,y=200)

etiqueta=Label(u,font=("arial",18,"bold"),text="puesto de trabajo:",bg="#B4C7E7").place(x=25,y=300)

etiqueta=Label(u,font=("arial",18,"bold"),text="usuario:",bg="#B4C7E7").place(x=25,y=400)

etiqueta=Label(u,font=("arial",18,"bold"),text="contraseña:",bg="#B4C7E7").place(x=25,y=500)

#-------------txt_usuario------------------------#

txt_identificacion=Entry(u,font=("arial",18,"bold"),bg="#D0CECE")
txt_identificacion.place(x=260,y=100)

txt_nombre=Entry(u,font=("arial",18,"bold"),bg="#D0CECE")
txt_nombre.place(x=260,y=200)

txt_trabajo=Entry(u,font=("arial",18,"bold"),bg="#D0CECE")
txt_trabajo.place(x=260,y=300)

txt_usuario=Entry(u,font=("arial",18,"bold"),bg="#D0CECE")
txt_usuario.place(x=260,y=400)

txt_contraseña=Entry(u,font=("arial",18,"bold"),bg="#D0CECE")
txt_contraseña.place(x=260,y=500)

#-------------botones_usuario------------------------#

boton_u1=Button(u,font=("arial",12,"bold"),text="consultar",width=20,height=2,bg="#0077AC",).place(x=600,y=100)

boton_u1=Button(u,font=("arial",12,"bold"),text="agregar usuario",width=20,height=2,bg="#0077AC").place(x=50,y=600)

boton_u1=Button(u,font=("arial",12,"bold"),text="modificar usuario",width=20,height=2,bg="#0077AC").place(x=300,y=600)

boton_u1=Button(u,font=("arial",12,"bold"),text="eliminar usuario",width=20,height=2,bg="#0077AC").place(x=550,y=600)
