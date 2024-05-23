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
ventana.geometry("550x900+0+10")




#contador de pallet
pallet = [0]

#donde escribir
entrada_de_codigo = Entry(ventana,width=30, font=('Arial 18'))
entrada_de_codigo.pack()


tabla = Listbox(ventana,height=30,width=30 , font=('Arial 18'),)
tabla.pack(side='left', padx=10)
tabla2 = Listbox(ventana,height=30,width=5 , font=('Arial 18'),)
tabla2.pack(side='left', padx=10)
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
        tabla2.insert(END,'\n')

    elif codigo.startswith("3600") and len(codigo) == 15:
        tabla.insert(END,codigo) #muestra el codigo de integra
        tabla2.insert(END,'\n')
        
    elif codigo.startswith("G") and len(codigo) == 15:
        tabla.insert(END,codigo) #muestra codigos integra telecom
        tabla2.insert(END,'\n')

    elif len(codigo) == 10 :
        tabla.insert(END,codigo) #muestra si es un code_envio
        tabla2.insert(END,'\n')

    elif len(codigo) == 26 :
        tabla.insert(END,codigo[13:23]) #muestra si es un code_bulto
        tabla2.insert(END,codigo[9:13])
        dato_columna = buscar_numero_en_excel(codigo[9:13])
        tabla.insert(END, f'{dato_columna[1]} {dato_columna[0]}')
        tabla2.insert(END,'\n')


    elif codigo.count('numeroDeEnvio'):
        tabla.insert(END,codigo[18:28]) #muestra si es QR
        tabla2.insert(END,codigo[56:60])
        dato_columna = buscar_numero_en_excel(codigo[56:60])
        tabla.insert(END, f'{dato_columna[1]} {dato_columna[0]}')
        tabla2.insert(END,'\n')


    else:
        tabla.insert(END,codigo)
        tabla.itemconfig(END, bg='red')
        

#para que se returne con enter
entrada_de_codigo.bind('<Return>', envio)


#borrar con suprimir
def borrar(event):
    tabla.delete(0, END)
    tabla2.delete(0, END)


tabla.bind('<Delete>',borrar)

#linea para exportar en .csv
def exportar(event):
    datos =[tabla.get(i) for i in range(tabla.size())]
    sin_duplicar = set(datos)
    df = DataFrame(sin_duplicar, columns = ['envios'])
    escritorio = path.join(path.expanduser("~"))
    df.to_csv(path.join(escritorio, 'psi_envios.csv'),index=False)


def buscar_numero_en_excel(numero_buscado):
    # Obtener la ruta del escritorio
    ruta_escritorio = path.join(path.expanduser("~"))

    # Nombre del archivo Excel en el escritorio
    nombre_archivo = "CP CORREO SUC.xlsx"

    # Ruta completa del archivo Excel en el escritorio
    ruta_excel = path.join(ruta_escritorio, nombre_archivo)

    # Leer solo las columnas H y A del archivo Excel
    df = read_excel(ruta_excel, usecols=["CP", "SUCURSALES","CODIGO"])
    #convertir numero 
    
    try:
        fila = df[df["CP"] == int(numero_buscado)].index[0]
        # Obtener el dato de la columna A en la misma fila
        dato_columna_A = df.iloc[fila, 0]  # El índice 1 corresponde a la columna A
        dato_columna_C = df.iloc[fila, 1]
        return dato_columna_A, dato_columna_C
    except IndexError:
        return None



ventana.bind('<F12>',exportar)

ventana.mainloop()

