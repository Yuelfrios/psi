# 21507008416211093355397001
# 20407008416215000912225003
# 1090607545
# ¨[numeroDeEnvio[Ñ[5000912194[,[numeroDeBulto[Ñ[20407008416215000912194001[,[cantidadDeBultos[Ñ[1[,[sucursalDeDistribucion[Ñ¨[nomenclatura[Ñ[070[,[descripcion[Ñ [BENAVIDEZ ' C DISTRIBUCION[,[id[Ñ[70[**
# G99999005835070
# 360000593775580
# made in niquillo
from tkinter import *
from tkinter import ttk


#ventana
ventana = Tk()
ventana.title("Psi")
ventana.geometry("450x900+0+10")

#contador de pallet
pallet = [0]

#donde escribir
entrada_de_codigo = Entry(ventana,width=30, font=('Arial 18'))
entrada_de_codigo.pack()


tabla = Listbox(ventana,height=30,width=30 , font=('Arial 18'),)
tabla.pack()
#para que entre el codigo


def envio (event):
    #------------------------front---------------------------
    codigo = entrada_de_codigo.get()
    entrada_de_codigo.bind('<Return>', entrada_de_codigo.delete(0, END))#eliminamos lo escrito al tocar enter
    #ingresar codigo en imagen y borra espacios vacias

    if ' ' in codigo:
        codigo = codigo.replace(' ', '')
    #backend ----------------------Reconocimiento---------------------------------
    if codigo.startswith("215") and len(codigo) == 26:
        tabla.insert(END,codigo) #muestra si es un code_correo
    elif codigo.startswith("3600") and len(codigo) == 15:
        tabla.insert(END,codigo) #muestra el codigo de integra
    elif codigo.startswith("G") and len(codigo) == 15:
        tabla.insert(END,codigo) #muestra codigos integra telecom
    elif len(codigo) == 10 :
        tabla.insert(END,codigo) #muestra si es un code_envio
    elif len(codigo) == 26 :
        tabla.insert(END,codigo[13:23]) #muestra si es un code_bulto
    elif codigo.count('numeroDeEnvio'):
        tabla.insert(END,codigo[18:28]) #muestra si es QR
    elif codigo == '123123123':
        tabla.insert(END,f'Pallet n° {pallet}')
        tabla.itemconfig(END, bg='black',fg="#fff")#-------------------------------------------------------
        pallet[0] += 1
    else:
        tabla.insert(END,codigo)
        tabla.itemconfig(END, bg='red')
        

#para que se returne con enter
entrada_de_codigo.bind('<Return>', envio)


#borrar con suprimir
def borrar(event):
    tabla.delete(0, END)
    pallet[0]= 0

tabla.bind('<Delete>',borrar)



ventana.mainloop()