from tkinter import *
import random
import datetime
from tkinter import filedialog, messagebox

#Aqui se van almacenando los valores que se ingresen en la calculadora
operador = ""

#Listas de precios:
precios_comida = [4.5, 5.2, 7.3, 8, 1.3, 9, 2.5, 12]
precios_bebida = [2, 3, 2, 4, 5, 1.5, 1.5, 2.3]
precios_postres = [5, 4, 4.5, 3, 3.5, 6, 4, 2.5]

def click_boton(numero):
    global operador
    operador = operador + numero
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(END, operador)

def tecla_borrar():
    global operador
    operador = ""
    visor_calculadora.delete(0, END)

def obtener_resultado():
    global operador
    #La funcion eval, evalua el contenido de operador y hace los calculos
    resultado = str(eval(operador))
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(0, resultado)
    operador = ""

def revisar_check():
    x = 0
    for c in cuadros_comida:
        if variables_comida[x].get() == 1:
            cuadros_comida[x].config(state=NORMAL)
            if cuadros_comida[x].get() == 0:
                cuadros_comida[x].delete(0, END) #Para que se quite el 0 cada vez que se selecciona
            cuadros_comida[x].focus() #Para que el cursor titile
        else: 
            cuadros_comida[x].config(state= DISABLED)
            textos_comida[x].set("0")
        x += 1

    x = 0
    for c in cuadros_bebida:
        if variables_bebida[x].get() == 1:
            cuadros_bebida[x].config(state=NORMAL)
            if cuadros_bebida[x].get() == 0:
                cuadros_bebida[x].delete(0, END) #Para que se quite el 0 cada vez que se selecciona
            cuadros_bebida[x].focus() #Para que el cursor titile
        else: 
            cuadros_bebida[x].config(state= DISABLED)
            textos_bebida[x].set("0")
        x += 1

    x = 0
    for c in cuadros_postre:
        if variables_postre[x].get() == 1:
            cuadros_postre[x].config(state=NORMAL)
            if cuadros_postre[x].get() == 0:
                cuadros_postre[x].delete(0, END) #Para que se quite el 0 cada vez que se selecciona
            cuadros_postre[x].focus() #Para que el cursor titile
        else: 
            cuadros_postre[x].config(state= DISABLED)
            textos_postre[x].set("0")
        x += 1
    

def total():
    subtotal_comida = 0
    p = 0
    for cantidad in textos_comida:
        subtotal_comida = subtotal_comida + (float(cantidad.get()) * precios_comida[p])
        p += 1

    subtotal_bebida = 0
    p = 0
    for cantidad in textos_bebida:
        subtotal_bebida = subtotal_bebida + (float(cantidad.get()) * precios_bebida[p])
        p += 1

    subtotal_postre = 0
    p = 0
    for cantidad in textos_postre:
        subtotal_postre = subtotal_postre + (float(cantidad.get()) * precios_postres[p])
        p += 1

    subtotal = subtotal_comida + subtotal_bebida + subtotal_postre
    impuestos = subtotal * 0.07
    total = subtotal + impuestos

    var_costo_comida.set(f"$ {round(subtotal_comida, 2)}")
    var_costo_bebida.set(f"$ {round(subtotal_bebida, 2)}")
    var_costo_postre.set(f"$ {round(subtotal_postre, 2)}")
    var_subtotal.set(f"$ {round(subtotal, 2)}")
    var_impuesto.set(f"$ {round(impuestos, 2)}")
    var_total.set(f"$ {round(total, 2)}")

def recibo():
    texto_recibo.delete(1.0, END)
    numero_recibo = f"N#- {random.randint(1000, 9999)}"
    fecha = datetime.datetime.now()
    fecha_recibo = f"{fecha.day}/{fecha.month}/{fecha.year} - {fecha.hour}:{fecha.minute}"
    texto_recibo.insert(END, f"Datos:\t {numero_recibo} \t\t{fecha_recibo} \n")
    texto_recibo.insert(END, f"*" * 57 + "\n")
    texto_recibo.insert(END, "Items \t\t Cant. \t\t Precio \n")
    texto_recibo.insert(END, f"-" * 68 + "\n")

    x = 0
    for comida in textos_comida:
        if comida.get() != "0":
            texto_recibo.insert(END, f"{lista_comidas[x]}\t\t {comida.get()}\t\t $ {int(comida.get()) * precios_comida[x]}\n")
        x +=1

    x = 0
    for bebida in textos_bebida:
        if bebida.get() != "0":
            texto_recibo.insert(END, f"{lista_bebidas[x]}\t\t {bebida.get()}\t\t $ {int(bebida.get()) * precios_bebida[x]}\n")
        x +=1
    
    x = 0
    for postre in textos_postre:
        if postre.get() != "0":
            texto_recibo.insert(END, f"{lista_postres[x]}\t\t {postre.get()}\t\t $ {int(postre.get()) * precios_postres[x]}\n")
        x +=1

    texto_recibo.insert(END, f"-"*54 + "\n")
    texto_recibo.insert(END, f"Costo Comida: \t\t\t\t{var_costo_comida.get()}\n")
    texto_recibo.insert(END, f"Costo Bebida: \t\t\t\t{var_costo_bebida.get()}\n")
    texto_recibo.insert(END, f"Costo Postre: \t\t\t\t{var_costo_postre.get()}\n")
    texto_recibo.insert(END, f"-"*54 + "\n")
    texto_recibo.insert(END, f"Subtotal: \t\t\t\t{var_subtotal.get()}\n")
    texto_recibo.insert(END, f"IVA: \t\t\t\t{var_impuesto.get()}\n")
    texto_recibo.insert(END, f"Total: \t\t\t\t{var_total.get()}\n")
    texto_recibo.insert(END, f"-" * 68 + "\n")
    texto_recibo.insert(END, f"Gracias por su visita")

def guardar():
    #Asi guardamos toda la información del archivo en una variable
    info_recibo = texto_recibo.get(1.0, END)
    archivo = filedialog.asksaveasfile(mode="w", defaultextension= ".txt")
    archivo.write(info_recibo)
    archivo.close()
    messagebox.showinfo("Información", "El recibo ha sido guardado")
     
def resetear():
    texto_recibo.delete(0.1, END)

    for texto in textos_comida:
        texto.set("0")
    for texto in textos_bebida:
        texto.set("0")
    for texto in textos_postre:
        texto.set("0")

    for cuadro in cuadros_comida:
        cuadro.config(state = DISABLED)
    for cuadro in cuadros_bebida:
        cuadro.config(state = DISABLED)
    for cuadro in cuadros_postre:
        cuadro.config(state = DISABLED)

    for v in variables_comida:
        v.set(0)
    for v in variables_bebida:
        v.set(0)
    for v in variables_postre:
        v.set(0)

    var_costo_comida.set("")
    var_costo_bebida.set("")
    var_costo_postre.set("")
    var_subtotal.set("")
    var_impuesto.set("")
    var_total.set("")


#Iniciando tkinter
aplicacion = Tk()

#tamaño ventana:
aplicacion.geometry('1050x630+0+0') #-> los 0 es la ubicación en el eje x y el eje y de la pantalla

#Evitar que se maximice la pantalla:
aplicacion.resizable(0, 0) #-> Son los valores de los ejes

#titulo
aplicacion.title("Restaurante")

#Color de fondo de la pantalla
aplicacion.config(bg="gray")

#Panel superior
panel_superior = Frame(aplicacion, bd=1, relief=FLAT)
#para llamar el panel a la pantalla:
panel_superior.pack(side= TOP)

#etiqueta titutlo// Donde se ubica la etiqueta, el texto que contiene, color de letra, tipo de letra y tamaño, color de fondo y ancho
etiqueta_titulo = Label(panel_superior, text="Sistema de facturación", fg="black",
                        font=("Dosis", 30), bg="gray", width=27)
etiqueta_titulo.grid(row=0, column=0)

#Panel izquierdo: 
panel_izquierdo = Frame(aplicacion, bd=1, relief=FLAT)
panel_izquierdo.pack(side=LEFT)

#Panel costos:
panel_costos = Frame(panel_izquierdo, bd= 1, relief=FLAT, bg="Slategray", padx =50)
panel_costos.pack(side=BOTTOM)

#panel comidas: //Labelframe es un cuadro que viene con la etiqueta incorporada
panel_comidas = LabelFrame (panel_izquierdo, text="Comida", font=("Dosis", 16, "bold"), 
                            bd=1, relief=FLAT, fg="black")
panel_comidas.pack(side=LEFT)

#panel bebidas: 
panel_bebidas = LabelFrame (panel_izquierdo, text="Bebidas", font=("Dosis", 16, "bold"), 
                            bd=1, relief=FLAT, fg="black")
panel_bebidas.pack(side=LEFT)

#panel Postres: 
panel_postres = LabelFrame (panel_izquierdo, text="Postres", font=("Dosis", 16, "bold"), 
                            bd=1, relief=FLAT, fg="black")
panel_postres.pack(side=LEFT)

#Panel derecho: 
panel_derecho = Frame(aplicacion, bd=1, relief=FLAT)
panel_derecho.pack(side=RIGHT)

#Panel calculadora:
panel_calculadora = Frame(panel_derecho, bd=1, relief=FLAT, bg="gray")
panel_calculadora.pack()

#Panel recibo:
panel_recibo = Frame(panel_derecho, bd=1, relief=FLAT, bg="gray")
panel_recibo.pack()

#Panel botones:
panel_botones = Frame(panel_derecho, bd=1, relief=FLAT, bg="gray")
panel_botones.pack()

#Lista de productos:
lista_comidas = ["Pollo", "Carne", "Pescado", "Pas Boloña", "Pas Pesto", "Piz Napoli", "Piz Hawai", "Piz Mgta"]
lista_bebidas = ["Cocacola", "Sprite", "Agua", "Jugo Melón", "Jugo Patilla", "Malta", "Solera", "Zulia"]
lista_postres = ["3 Leches", "Quesillo", "Helado", "Waffle", "Panqueca", "Torta", "Fruta", "Tiramisú"]

#Generando Items comida
variables_comida = []
cuadros_comida = []
textos_comida = []
contador = 0
for comidas in lista_comidas:
    #Crear checkbutton
    variables_comida.append("")
    variables_comida[contador] = IntVar()
    comidas = Checkbutton(panel_comidas, text=comidas.title(), font=("Dosis", 14, "bold"),
                          onvalue=1, offvalue=0, variable=variables_comida[contador], command=revisar_check) 
    #onvalue, es el valor que tendrá cuando estpa activada la casilla y offvalue cuando esta desactivada
    comidas.grid(row=contador, column=0, sticky=W)

    #Crear cuadros de entrada comida
    cuadros_comida.append("")
    textos_comida.append("")
    textos_comida[contador] = StringVar()
    textos_comida[contador].set("0")
    cuadros_comida[contador] = Entry(panel_comidas, font=("Dosis", 14, "bold"), bd=1, width=6, state= DISABLED, textvariable=textos_comida[contador])
    cuadros_comida[contador].grid(row = contador, column = 1)
    contador +=1

#Generando Items bebida
variables_bebida = []
cuadros_bebida = []
textos_bebida = []
contador = 0
for bebidas in lista_bebidas:
    variables_bebida.append("")
    variables_bebida[contador] = IntVar()
    bebidas = Checkbutton(panel_bebidas, text=bebidas.title(), font=("Dosis", 14, "bold"),
                          onvalue=1, offvalue=0, variable=variables_bebida[contador], command=revisar_check) 
    #onvalue, es el valor que tendrá cuando estpa activada la casilla y offvalue cuando esta desactivada
    bebidas.grid(row=contador, column=0, sticky=W)

    #Crear cuadros de entrada bebidas
    cuadros_bebida.append("")
    textos_bebida.append("")
    textos_bebida[contador] = StringVar()
    textos_bebida[contador].set("0")
    cuadros_bebida[contador] = Entry(panel_bebidas, font=("Dosis", 14, "bold"), bd=1, width=6, state= DISABLED, textvariable=textos_bebida[contador])
    cuadros_bebida[contador].grid(row = contador, column = 1)
    contador +=1

#Generando Items postre
variables_postre = []
cuadros_postre = []
textos_postre = []
contador = 0
for postres in lista_postres:
    variables_postre.append("")
    variables_postre[contador] = IntVar()
    postres = Checkbutton(panel_postres, text=postres.title(), font=("Dosis", 14, "bold"),
                          onvalue=1, offvalue=0, variable=variables_postre[contador], command=revisar_check) 
    #onvalue, es el valor que tendrá cuando estpa activada la casilla y offvalue cuando esta desactivada
    postres.grid(row=contador, column=0, sticky=W)

    #Crear cuadros de entrada postres
    cuadros_postre.append("")
    textos_postre.append("")
    textos_postre[contador] = StringVar()
    textos_postre[contador].set("0")
    cuadros_postre[contador] = Entry(panel_postres, font=("Dosis", 14, "bold"), bd=1, width=6, state= DISABLED, textvariable=textos_postre[contador])
    cuadros_postre[contador].grid(row = contador, column = 1)
    contador +=1

#Variables:
var_costo_comida = StringVar()
var_costo_bebida = StringVar()
var_costo_postre = StringVar()
var_subtotal = StringVar()
var_impuesto = StringVar()
var_total = StringVar()


#Etiquetas de costos y campos de entrada comida
etiqueta_costo_comida = Label(panel_costos, text="Costo Comida", font=("Dosis", 12, "bold"), bg="Slategray", fg="white")
etiqueta_costo_comida.grid(row=0, column=0)

texto_costo_comida = Entry(panel_costos, font = ("Dosis", 12, "bold"), bd=1, width=10, state="readonly", textvariable=var_costo_comida)
texto_costo_comida.grid(row=0, column=1, padx = 41)

#Etiquetas de costos y campos de entrada bebida
etiqueta_costo_bebida = Label(panel_costos, text="Costo bebida", font=("Dosis", 12, "bold"), bg="Slategray", fg="white")
etiqueta_costo_bebida.grid(row=1, column=0)

texto_costo_bebida = Entry(panel_costos, font = ("Dosis", 12, "bold"), bd=1, width=10, state="readonly", textvariable=var_costo_bebida)
texto_costo_bebida.grid(row=1, column=1, padx = 41)

#Etiquetas de costos y campos de entrada postres
etiqueta_costo_postre = Label(panel_costos, text="Costo postre", font=("Dosis", 12, "bold"), bg="Slategray", fg="white")
etiqueta_costo_postre.grid(row=2, column=0)

texto_costo_postre = Entry(panel_costos, font = ("Dosis", 12, "bold"), bd=1, width=10, state="readonly", textvariable=var_costo_postre)
texto_costo_postre.grid(row=2, column=1, padx = 41)

#Etiquetas subtotal
etiqueta_subtotal = Label(panel_costos, text="Subtotal", font=("Dosis", 12, "bold"), bg="Slategray", fg="white")
etiqueta_subtotal.grid(row=0, column=2)

texto_subtotal = Entry(panel_costos, font = ("Dosis", 12, "bold"), bd=1, width=10, state="readonly", textvariable=var_subtotal)
texto_subtotal.grid(row=0, column=3, padx = 41)

#Etiquetas impuestos
etiqueta_impuesto = Label(panel_costos, text="Impuestos", font=("Dosis", 12, "bold"), bg="Slategray", fg="white")
etiqueta_impuesto.grid(row=1, column=2)

texto_impuesto = Entry(panel_costos, font = ("Dosis", 12, "bold"), bd=1, width=10, state="readonly", textvariable=var_impuesto)
texto_impuesto.grid(row=1, column=3)

#Etiquetas total
etiqueta_total = Label(panel_costos, text="Total", font=("Dosis", 12, "bold"), bg="Slategray", fg="white")
etiqueta_total.grid(row=2, column=2)

texto_total = Entry(panel_costos, font = ("Dosis", 12, "bold"), bd=1, width=10, state="readonly", textvariable=var_total)
texto_total.grid(row=2, column=3, padx = 41)


#botones
botones = ["Total", "Recibo", "Guardar", "Resetear"]
botones_creados = []

columnas = 0
#Con este loop creamos todos los botones
for boton in botones:
    boton = Button(panel_botones, text=boton.title(), font=("Dosis", 12, "bold"), fg="white", bg="Slategray", bd=1, width=9)

    botones_creados.append(boton)

    boton.grid(row=0, column=columnas)
    columnas +=1

botones_creados[0].config(command = total)
botones_creados[1].config(command = recibo)
botones_creados[2].config(command = guardar)
botones_creados[3].config(command = resetear)

#area de recibo
texto_recibo = Text(panel_recibo, font=("Dosis", 12, "bold"),bd=1, width= 38, height=10)
texto_recibo.grid(row=0, column=0)
    
#Calculadora
visor_calculadora = Entry(panel_calculadora, font=("Dosis", 12, "bold"), width= 38, bd=1)
visor_calculadora.grid(row=0, column=0, columnspan=4)

botones_calculadora = ["7", "8", "9", "+", "4", "5", "6", "-", "1", "2", "3", "x", "=", "CE", "0", "/"]

botones_guardados = []

fila = 1
columnas = 0
for boton in botones_calculadora:
    boton = Button(panel_calculadora, text=boton.title(), font=("Dosis", 16, "bold"), fg="black", bg="Slategray", bd=1, width=6)

    botones_guardados.append(boton)

    boton.grid(row=fila, column=columnas)
    if columnas == 3:
        fila +=1
    columnas +=1

    if columnas ==4:
        columnas = 0

botones_guardados[0].config(command= lambda: click_boton("7"))
botones_guardados[1].config(command= lambda: click_boton("8"))
botones_guardados[2].config(command= lambda: click_boton("9"))
botones_guardados[3].config(command= lambda: click_boton("+"))
botones_guardados[4].config(command= lambda: click_boton("4"))
botones_guardados[5].config(command= lambda: click_boton("5"))
botones_guardados[6].config(command= lambda: click_boton("6"))
botones_guardados[7].config(command= lambda: click_boton("-"))
botones_guardados[8].config(command= lambda: click_boton("1"))
botones_guardados[9].config(command= lambda: click_boton("2"))
botones_guardados[10].config(command= lambda: click_boton("3"))
botones_guardados[11].config(command= lambda: click_boton("*"))
botones_guardados[12].config(command= obtener_resultado)
botones_guardados[13].config(command= tecla_borrar)
botones_guardados[14].config(command= lambda: click_boton("0"))
botones_guardados[15].config(command= lambda: click_boton("/"))



#Evitar que la pantalla se cierre
aplicacion.mainloop() # -> Establece una especie de loop que se ejecuta constantemente evitando que el programa finalice.

