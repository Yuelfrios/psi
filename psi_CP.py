# 21507008416211093355397001
# 20407008416215000912225003
# 1090607545
# ¨[numeroDeEnvio[Ñ[5000912194[,[numeroDeBulto[Ñ[20407008416215000912194001[,[cantidadDeBultos[Ñ[1[,[sucursalDeDistribucion[Ñ¨[nomenclatura[Ñ[070[,[descripcion[Ñ [BENAVIDEZ ' C DISTRIBUCION[,[id[Ñ[70[**
# G99999005835070
# 360000593775580
# made in niquillo
from tkinter import Tk,Entry,Listbox,END
from pandas import DataFrame,read_excel
from os import path
#ventana
ventana = Tk()
ventana.title("Psi by nlara")
ventana.geometry("430x900+0+10")

contador_de_letras = 0
abecedario = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

#contador de pallet
pallet = [0]

#donde escribir
entrada_de_codigo = Entry(ventana,width=30, font=('Arial 18'))
entrada_de_codigo.pack()


tabla = Listbox(ventana,height=30,width=20 , font=('Arial 18'),)
tabla.pack(side='left', padx=10)
tabla2 = Listbox(ventana,height=30,width=5 , font=('Arial 18'),)
tabla2.pack(side='left', padx=10)
tabla3 = Listbox(ventana,height=30,width=2 , font=('Arial 18'),bg='lightblue')
tabla3.pack(side='left', padx=10)
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
        tabla2.insert(END,codigo[23:26])



    elif codigo.startswith("3600") and len(codigo) == 15:
        repeticion(codigo)
        tabla.insert(END,codigo) #muestra el codigo de integra
        tabla2.insert(END,'\n')


        
    elif codigo.startswith("G") and len(codigo) == 15:
        repeticion(codigo)
        tabla.insert(END,codigo) #muestra codigos integra telecom
        tabla2.insert(END,'\n')



    elif len(codigo) == 10 :
        repeticion(codigo)
        tabla.insert(END,codigo) #muestra si es un code_envio
        tabla2.insert(END,'\n')


    elif len(codigo) == 26 :
        repeticion(codigo[13:23])
        tabla.insert(END,codigo[13:23]) #muestra si es un code_bulto
        tabla2.insert(END,codigo[23:26])


    elif codigo.count('numeroDeEnvio'):
        tabla.insert(END,codigo[18:28]) #muestra si es QR
        tabla2.insert(END,codigo[70:73])


    elif codigo == '123123123':
        tabla.insert(END,f'Pallet n° {pallet}')
        tabla2.insert(END,'\n')
        tabla.itemconfig(END, bg='black',fg="#fff")#-------------------------------------------------------
        pallet[0] += 1
    else:#ERROR-----------------------------------
        tabla.insert(END,codigo)
        tabla.itemconfig(END, bg='red')
        tabla2.insert(END,'\n')

        

#para que se returne con enter
entrada_de_codigo.bind('<Return>', envio)


def repeticion (repeticion): #control de la tabla3
    if entrada_de_codigo.get() == '123123123':
        tabla3.insert(END, '\n')
    else:
        items = tabla.get(0, END)
        for item in items:
            if item == repeticion:
                tabla3.insert(END,abecedario[0])
                contador_de_letras =+1
                return tabla.itemconfig(END, bg='yellow')


#borrar con suprimir
def borrar(event):
    tabla.delete(0, END)
    tabla2.delete(0, END)
    tabla3.insert(0, END)
    contador_de_letras = 0
    pallet[0]= 0

tabla.bind('<Delete>',borrar)

#linea para exportar en .csv
def exportar(event):
    datos =[tabla.get(i) for i in range(tabla.size())]
    sin_duplicar = set(datos)
    df = DataFrame(sin_duplicar, columns = ['envios'])
    escritorio = path.join(path.expanduser("~"), "Desktop")
    df.to_csv(path.join(escritorio, 'psi_envios.csv'),index=False)





ventana.bind('<F12>',exportar)

ventana.mainloop()

