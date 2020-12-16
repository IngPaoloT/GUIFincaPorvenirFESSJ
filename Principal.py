from tkinter import *
import time
import math
import Serial as P

#Se definen variables para guardar temporalmente datos de sensores
c=0
t= DoubleVar()
h=DoubleVar()
la=StringVar()
lo=StringVar()

#Se define la variable pi = 3,141...#
global pi
pi = math.pi

global color
color = 'green'



#Funcion para iniciar la aplicacion

def App():
        global ventana_inicio
        ventana_inicio= Tk()
        ventana_inicio.geometry('430x220')
        ventana_inicio.resizable(0,0)
        cargando = Label(ventana_inicio, text="Cargando Programa ...")
        cargando.pack()
        ventana_inicio.after(100,inicio_programa)
        

#Funcion para mostrar informacion y menu

def inicio_programa():
        global iniciar1,cancelar1
        global ventana_principal
        ventana_inicio.destroy()
        ventana_principal = Tk()
        ventana_principal.geometry('650x300')
        ventana_principal.title("GUI para medición de temperatura y humedad, finca el Porvenir")
        ventana_principal.resizable(0,0)

        Menubar=Menu(ventana_principal)
        
        menu_Opciones=Menu(Menubar,tearoff=0)
        menu_Opciones.add_command(label="Acerca de",font="Helvetica 10",command=acerca)
        menu_Opciones.add_command(label="Salir",font="Helvetica 10",command=quit)
        Menubar.add_cascade(label="Opciones",font="Helvetica 10",menu=menu_Opciones)

        menu_Ayuda=Menu(Menubar,tearoff=0)
        menu_Ayuda.add_command(label="Sensores",font="Helvetica 10",command=sensores)
        menu_Ayuda.add_command(label="Como utilizar",font="Helvetica 10",command=utilizar)
        Menubar.add_cascade(label="Ayuda",font="Helvetica 10",menu=menu_Ayuda)      

        ventana_principal.config(menu=Menubar)

        texto_bienvenida = Label(ventana_principal,text="Proyecto de investigación: Aplicación de un desarrollo IoT con técnica \n de agricultura de precisión para un cultivo de flores. \n. \n Autor : Jhonatan Paolo Tovar Soto \n Institución financiadora: Fundación de Educación Superior San José",font="Helvetica")
        
        iniciar1=Button(ventana_principal,text="Iniciar",font="Helvetica 12",command=iniciar)
        texto_bienvenida.pack(side=TOP,fill=BOTH, expand=True)
        iniciar1.pack()
        
#Ventanas de menú página principal
def menuAcerca():
        global ventana_menu1
        ventana_menu1= Tk()
        ventana_menu1.geometry('430x220')
        ventana_menu1.title("Acerca de...")
        ventana_menu1.resizable(0,0)
        acercaDe = Label(ventana_menu1, text="Este programa está diseñado para llevar a cabo \n el monitoreo en tiempo real de los cultivos de proteas \n en la finca el Porvenir. \n Todos los derechos están reservados por el \n Ing. Jhonatan Paolo Tovar Soto, en cesión a la \n Fundación de Educación Superior San José.")
        acercaDe.pack()

def menuSensores():
        global ventana_menu2
        ventana_menu2= Tk()
        ventana_menu2.geometry('430x220')
        ventana_menu2.title("Sensores...")
        ventana_menu2.resizable(0,0)
        sensores1 = Label(ventana_menu2, text="Temperatura: Los datos son obtenidos en campo por un sensor\n DHT22 a través de la tarjeta TTGO esp32.")
        sensores2 = Label(ventana_menu2, text="Humedad: Los datos son obtenidos en campo por un sensor\n DHT22 a través de la tarjeta TTGO esp32.")
        sensores3 = Label(ventana_menu2, text ="LOs datos son obtenidos mediante protocolo serial \n en la tarjeta raspberry Pi, y son enviados\n a través del protocolo LoRa")
        sensores1.pack()
        sensores2.pack()
        sensores3.pack()
        
def menuUtilizar():
        global ventana_menu3
        ventana_menu3= Tk()
        ventana_menu3.geometry('620x250')
        ventana_menu3.title("Cómo utilizar...")
        ventana_menu3.resizable(0,0)
        texto = Label(ventana_menu3, text="El programa tiene dos modos de funcionamiento: manual y automático. \n El modo manual le permite obtener datos a través de un click,\n por su parte el modo automático actualiza las lecturas \n en pantalla cada cierto tiempo programado por software. \n En cualquier modalidad los datos se guardan en una base de datos. \n Puede obtener gráficos posteriormente con dicha información.")
        texto.pack()
        
#Funciones menú página inicial
def acerca():
        menuAcerca()
        
def sensores():
        menuSensores()
def utilizar():
        menuUtilizar()
#Funcion para escojer que tarea realizar: modo manual o automático
def iniciar():
        global ventana_sec_1
        ventana_sec_1 = Toplevel(ventana_principal)
        ocultar(ventana_principal)
        ventana_sec_1.geometry('400x170')
        ventana_sec_1.title("Menú principal")
        Texto1= Label(ventana_sec_1,text="¿Cual modo quiere trabajar para sus mediciones?",font="Helvetica 12")
        Texto1.pack()
        global item
        item = IntVar()
        Boton1= Radiobutton(ventana_sec_1, text = "Modo manual.",font="Helvetica 12", variable = item, value =1)
        Boton1.pack(anchor=W)
        Boton2=Radiobutton(ventana_sec_1, text = "Modo automático.",font="Helvetica 12", variable = item, value =2)
        Boton2.pack(anchor=W)

        Continuar1=Button(ventana_sec_1, text="Continuar",font="Helvetica 12",command=lambda:elegirUno(item.get()))
        Continuar1.pack()
        Continuar1.place(x=60,y=100,width=100)
        Atras1=Button(ventana_sec_1, text="Atrás",font="Helvetica 12",command=lambda:destruir(ventana_principal,ventana_sec_1))
        Atras1.pack()
        Atras1.place(x=240,y=100,width=100)
        

#Funcion que elije que operacion realizar en el menú principal
def elegirUno(elec):
        if elec==1:
                modoManual()
                print("1")
        else:
                modoAutomatico()
                print("2")


#Funciones de las ventanas de cada modo
def modoManual():
        global ventana_sec_2
        ventana_sec_2 = Toplevel(ventana_principal)
        ocultar(ventana_sec_1)
        ventana_sec_2.geometry('400x170')
        ventana_sec_2.title("Modo Manual")
        Texto1= Label(ventana_sec_2,text="¿Cual medición desea obtener?",font="Helvetica 12")
        Texto1.pack()
        global item
        item = IntVar()
        Boton1= Radiobutton(ventana_sec_2, text = "Temperatura [°C].",font="Helvetica 12", variable = item, value =1)
        Boton1.pack(anchor=W)
        Boton2=Radiobutton(ventana_sec_2, text = "Humedad relativa [%].",font="Helvetica 12", variable = item, value =2)
        Boton2.pack(anchor=W)
        Boton3=Radiobutton(ventana_sec_2, text = "Temperatura [°C] y Humedad relativa [%].",font="Helvetica 12", variable = item, value =3)
        Boton3.pack(anchor=W)

        Continuar2=Button(ventana_sec_2, text="Continuar",font="Helvetica 12",command=lambda:elegirDos(item.get()))
        Continuar2.pack()
        Continuar2.place(x=60,y=100,width=100)
        Atras2=Button(ventana_sec_2, text="Atras",font="Helvetica 12",command=lambda:destruir(ventana_sec_1,ventana_sec_2))
        Atras2.pack()
        Atras2.place(x=240,y=100,width=100)

def modoAutomatico():
        global ventana_sec_3
        ventana_sec_3 = Toplevel(ventana_principal)
        ocultar(ventana_sec_1)
        ventana_sec_3.geometry('400x170')
        ventana_sec_3.title("Modo Automático")
        Texto1= Label(ventana_sec_3,text="¿Cual medición desea obtener?",font="Helvetica 12")
        Texto1.pack()
        global item
        item = IntVar()
        Boton1= Radiobutton(ventana_sec_3, text = "Temperatura [°C].",font="Helvetica 12", variable = item, value =1)
        Boton1.pack(anchor=W)
        Boton2=Radiobutton(ventana_sec_3, text = "Humedad relativa [%].",font="Helvetica 12", variable = item, value =2)
        Boton2.pack(anchor=W)
        Boton3=Radiobutton(ventana_sec_3, text = "Temperatura [°C] y Humedad relativa [%].",font="Helvetica 12", variable = item, value =3)
        Boton3.pack(anchor=W)

        Continuar3=Button(ventana_sec_3, text="Continuar",font="Helvetica 12",command=lambda:elegirTres(item.get()))
        Continuar3.pack()
        Continuar3.place(x=60,y=100,width=100)
        Atras3=Button(ventana_sec_3, text="Atras",font="Helvetica 12",command=lambda:destruir(ventana_sec_1,ventana_sec_3))
        Atras3.pack()
        Atras3.place(x=240,y=100,width=100)


#Funcion que elije que operacion realizar en el menú manual y automático
def elegirDos(elec):
        if elec==1:
                temperaturaManual()
                print("1")
        elif elec==2:
                humedadManual()
                print("2")
        else:
                tempHumedadManual()
                print("3")

def elegirTres(elec):
        if elec==1:
                temperaturaAutomatico()
                print("1")
        elif elec==2:
                humedadAutomatico()
                print("2")
        else:
                tempHumedadAutomatico()
                print("3")

#Funciones para crear ventanas de visualizacion de datos en modo Manual

def temperaturaManual():
        ventana_Temp_Man = Toplevel(ventana_principal)
        ocultar(ventana_sec_2)
        ventana_Temp_Man.geometry('350x150')
        ventana_Temp_Man.title('Medición de temperatura')
        
        texto1=Label(ventana_Temp_Man, text = "Temperatura actual:",font="Helvetica 12")
        texto1.grid(row=0,column=0)

        texto2=Label(ventana_Temp_Man,textvariable= Temp,font="Helvetica 12")
        texto2.grid(row=0,column=1)

        texto3=Label(ventana_Temp_Man,text = "Latitud:",font="Helvetica 12")
        texto3.grid(row=1,column=0)

        texto4=Label(ventana_Temp_Man,textvariable = Lat,font="Helvetica 12")
        texto4.grid(row=1,column=1)

        texto5=Label(ventana_Temp_Man,text = "Longitud:",font="Helvetica 12")
        texto5.grid(row=2,column=0)
        
        texto5=Label(ventana_Temp_Man,textvariable = Long,font="Helvetica 12")
        texto5.grid(row=2,column=1)
        
        Boton1=Button(ventana_Temp_Man,text="Tomar datos",font="Helvetica 12",command=lambda:temperatura())
        Boton1.grid(row=3,column=0)
        Boton2=Button(ventana_Temp_Man,text = "Volver al menú principal",font="Helvetica 12", command=lambda:destruir2(ventana_sec_2,ventana_Temp_Man))
        Boton2.grid(row=4,column=1)
        Boton3=Button(ventana_Temp_Man,text = "Obtener gráfica",font="Helvetica 12", command=graficar())
        Boton3.grid(row=3,column=1)

def humedadManual():
        ventana_Hum_Man = Toplevel(ventana_principal)
        ocultar(ventana_sec_2)
        ventana_Hum_Man.geometry('350x150')
        ventana_Hum_Man.title('Medición de humedad')
        
        texto1=Label(ventana_Hum_Man, text = "Humedad actual:",font="Helvetica 12")
        texto1.grid(row=0,column=0)

        texto2=Label(ventana_Hum_Man,textvariable = h,font="Helvetica 12")
        texto2.grid(row=0,column=1)

        texto3=Label(ventana_Hum_Man,text = "Latitud:",font="Helvetica 12")
        texto3.grid(row=1,column=0)

        texto4=Label(ventana_Hum_Man,textvariable = la,font="Helvetica 12")
        texto4.grid(row=1,column=1)

        texto5=Label(ventana_Hum_Man,text = "Longitud:",font="Helvetica 12")
        texto5.grid(row=2,column=0)
        
        texto5=Label(ventana_Hum_Man,textvariable = lo,font="Helvetica 12")
        texto5.grid(row=2,column=1)
        
        Boton1=Button(ventana_Hum_Man,text="Tomar datos",font="Helvetica 12",command=lambda:humedad())
        Boton1.grid(row=3,column=0)
        Boton2=Button(ventana_Hum_Man,text = "Volver al menú principal",font="Helvetica 12", command=lambda:destruir2(ventana_sec_2,ventana_Hum_Man))
        Boton2.grid(row=4,column=1)
        Boton3=Button(ventana_Hum_Man,text = "Obtener gráfica",font="Helvetica 12", command=graficar())
        Boton3.grid(row=3,column=1)

def tempHumedadManual():
        ventana_Temp_Hum_Man = Toplevel(ventana_principal)
        ocultar(ventana_sec_2)
        ventana_Temp_Hum_Man.geometry('400x180')
        ventana_Temp_Hum_Man.title('Medición de temperatura y humedad')
        
        texto1=Label(ventana_Temp_Hum_Man, text = "Temperatura actual:",font="Helvetica 12")
        texto1.grid(row=0,column=0)

        texto2=Label(ventana_Temp_Hum_Man,textvariable = t,font="Helvetica 12")
        texto2.grid(row=0,column=1)

        texto12=Label(ventana_Temp_Hum_Man, text = "Humedad actual:",font="Helvetica 12")
        texto12.grid(row=1,column=0)

        texto22=Label(ventana_Temp_Hum_Man,textvariable = h,font="Helvetica 12")
        texto22.grid(row=1,column=1)

        texto3=Label(ventana_Temp_Hum_Man,text = "Latitud:",font="Helvetica 12")
        texto3.grid(row=2,column=0)

        texto4=Label(ventana_Temp_Hum_Man,textvariable = la,font="Helvetica 12")
        texto4.grid(row=2,column=1)

        texto5=Label(ventana_Temp_Hum_Man,text = "Longitud:",font="Helvetica 12")
        texto5.grid(row=3,column=0)
        
        texto5=Label(ventana_Temp_Hum_Man,textvariable = lo,font="Helvetica 12")
        texto5.grid(row=3,column=1)
        
        Boton1=Button(ventana_Temp_Hum_Man,text="Tomar datos",font="Helvetica 12",command=lambda:temperaturaHumedad())
        Boton1.grid(row=4,column=0)
        Boton2=Button(ventana_Temp_Hum_Man,text = "Volver al menu principal",font="Helvetica 12", command=lambda:destruir2(ventana_sec_2,ventana_Temp_Hum_Man))
        Boton2.grid(row=5,column=1)
        Boton3=Button(ventana_Temp_Hum_Man,text = "Obtener grafica",font="Helvetica 12", command=graficar())
        Boton3.grid(row=4,column=1)

#Funciones para crear ventanas de visualizacion de datos en modo Automático

def temperaturaAutomatico():
        ventana_Temp_Aut = Toplevel(ventana_principal)
        ocultar(ventana_sec_3)
        ventana_Temp_Aut.geometry('350x150')
        ventana_Temp_Aut.title('Medición de temperatura')
        
        texto1=Label(ventana_Temp_Aut, text = "Temperatura actual:",font="Helvetica 12")
        texto1.grid(row=0,column=0)

        texto2=Label(ventana_Temp_Aut,textvariable = t,font="Helvetica 12")
        texto2.grid(row=0,column=1)

        texto3=Label(ventana_Temp_Aut,text = "Latitud:",font="Helvetica 12")
        texto3.grid(row=1,column=0)

        texto4=Label(ventana_Temp_Aut,textvariable = la,font="Helvetica 12")
        texto4.grid(row=1,column=1)

        texto5=Label(ventana_Temp_Aut,text = "Longitud:",font="Helvetica 12")
        texto5.grid(row=2,column=0)
        
        texto5=Label(ventana_Temp_Aut,textvariable = lo,font="Helvetica 12")
        texto5.grid(row=2,column=1)
        
        Boton2=Button(ventana_Temp_Aut,text = "Volver al menú principal",font="Helvetica 12", command=lambda:destruir2(ventana_sec_3,ventana_Temp_Aut))
        Boton2.grid(row=3,column=1)
        Boton3=Button(ventana_Temp_Aut,text = "Obtener gráfica",font="Helvetica 12", command=graficar())
        Boton3.grid(row=3,column=0)

def humedadAutomatico():
        ventana_Hum_Aut = Toplevel(ventana_principal)
        ocultar(ventana_sec_3)
        ventana_Hum_Aut.geometry('350x150')
        ventana_Hum_Aut.title('Medición de humedad')
        
        texto1=Label(ventana_Hum_Aut, text = "Humedad actual:",font="Helvetica 12")
        texto1.grid(row=0,column=0)

        texto2=Label(ventana_Hum_Aut,textvariable = h,font="Helvetica 12")
        texto2.grid(row=0,column=1)

        texto3=Label(ventana_Hum_Aut,text = "Latitud:",font="Helvetica 12")
        texto3.grid(row=1,column=0)

        texto4=Label(ventana_Hum_Aut,textvariable = la,font="Helvetica 12")
        texto4.grid(row=1,column=1)

        texto5=Label(ventana_Hum_Aut,text = "Longitud:",font="Helvetica 12")
        texto5.grid(row=2,column=0)
        
        texto5=Label(ventana_Hum_Aut,textvariable = lo,font="Helvetica 12")
        texto5.grid(row=2,column=1)
        
        Boton2=Button(ventana_Hum_Aut,text = "Volver al menú principal",font="Helvetica 12", command=lambda:destruir2(ventana_sec_3,ventana_Hum_Aut))
        Boton2.grid(row=3,column=1)
        Boton3=Button(ventana_Hum_Aut,text = "Obtener gráfica",font="Helvetica 12", command=graficar())
        Boton3.grid(row=3,column=0)

def tempHumedadAutomatico():
        ventana_Temp_Hum_Aut = Toplevel(ventana_principal)
        ocultar(ventana_sec_3)
        ventana_Temp_Hum_Aut.geometry('400x180')
        ventana_Temp_Hum_Aut.title('Medición de temperatura y humedad')
        
        texto1=Label(ventana_Temp_Hum_Aut, text = "Temperatura actual:",font="Helvetica 12")
        texto1.grid(row=0,column=0)

        texto2=Label(ventana_Temp_Hum_Aut,textvariable = t,font="Helvetica 12")
        texto2.grid(row=0,column=1)

        texto12=Label(ventana_Temp_Hum_Aut, text = "Humedad actual:",font="Helvetica 12")
        texto12.grid(row=1,column=0)

        texto22=Label(ventana_Temp_Hum_Aut,textvariable = h, font="Helvetica 12")
        texto22.grid(row=1,column=1)

        texto3=Label(ventana_Temp_Hum_Aut,text = "Latitud:",font="Helvetica 12")
        texto3.grid(row=2,column=0)

        texto4=Label(ventana_Temp_Hum_Aut,textvariable= la,font="Helvetica 12")
        texto4.grid(row=2,column=1)

        texto5=Label(ventana_Temp_Hum_Aut,text = "Longitud:",font="Helvetica 12")
        texto5.grid(row=3,column=0)
        
        texto5=Label(ventana_Temp_Hum_Aut,textvariable = lo,font="Helvetica 12")
        texto5.grid(row=3,column=1)
        
        Boton2=Button(ventana_Temp_Hum_Aut,text = "Volver al menu principal",font="Helvetica 12", command=lambda:destruir2(ventana_sec_3,ventana_Temp_Hum_Aut))
        Boton2.grid(row=4,column=1)
        Boton3=Button(ventana_Temp_Hum_Aut,text = "Obtener grafica",font="Helvetica 12", command=graficar())
        Boton3.grid(row=4,column=0)
        
#Funciones para tomar datos

#Se descompone el texto que se lee de los sensores para cada variable
def datos():
  try:
    cadena = P.lectura()
  except TypeError:
    print("Error de Byte")
  else:
    temporal=cadena.split('V')
    T=temporal[1]
    H=temporal[2]
    Lo=temporal[3]
    La=temporal[4]
    
  return (T,H,Lo,La)

#Función de excepción para valores que no se pueden convertir
def adjuntar():
  t1,h1,lo1,la1 = datos()
  try:
    c=0
    t.set(t1)
    c=1
    h.set(h1)
    c=2
    lo.set(lo1)
    c=3
    la.set(la1)
  except ValueError:
    if c==0:
      adjuntar()
    elif c==1:
      adjuntar()
    elif c==2:
      adjuntar()
    else:
      adjuntar()
  else:
      print("Todo Bien")

        
#Funcion pra graficarlos datos
def graficar():
        return 
#Funcion para mostrar ventana
def mostrar(v1):
        v1.deiconify()

#Funcion para ocultar ventana
def ocultar(v2):
        v2.iconify()

#Funcion para destruir ventana y mostrar la anterior
def destruir(v3,v4):
        v3.deiconify()
        v4.destroy()

def destruir2(v3,v4):
        v3.deiconify()
        v4.destroy()

App()
mainloop()

    
