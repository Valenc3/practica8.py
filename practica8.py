from queue import LifoQueue as pila
import random

#EJERCICIO 1 
#1---------------------------------- 
def contar_lineas(nombre:str) -> int:
    archivo = open(nombre,"r")
    lineas = archivo.readlines()
    return len(lineas)

def contar_linea(nombre:str) -> int:
    texto = open(nombre,"r")
    n = 0
    for linea in texto:
        n += 1
    return n 
#2-----------------------------------
def existe_palabra(palabra:str,nombre:str) -> bool:
    texto = open(nombre,"r")
    for linea in texto:
        lista = linea.split()
        for elemento in lista:
            if elemento == palabra:
                return True 
    else:
        return False
#3----------------------------------
def cantidad_apariciones(nombre:str,palabra:str) -> int:
    texto = open(nombre,"r")
    n = 0 
    for linea in texto:
        lista = linea.split()
        n += lista.count(palabra)
    return n 


#EJERCICIO 2
def clonar_sin_comentarios(nombre_archivo : str):
    archivo = open(nombre_archivo, "r")
    arch_sin_comentarios = open("clonadoSinComentarios.py", "w")
    lineas = archivo.readlines()
    for linea in lineas:
        if not linea.strip()[0] == "#":
            arch_sin_comentarios.write(linea)
    archivo.close()
    arch_sin_comentarios.close()


#EJERCICIO 3
def reverso(nombre:str):
     archivo = open(nombre, "r")
     reverso = open("reverso.py", "w")
     lineas = archivo.readlines()
     for i in range(1,len(lineas)+1):
        reverso.write(lineas[-i])
     archivo.close()
     reverso.close()


#EJERCICIO 4
def frase(nombre:str,frase:str):
    texto = open(nombre,"a")
    texto.write(frase)
    texto.close()


#EJERCICIO 5 
def principio(nombre:str,frase:str):
    texto = open(nombre,"r")
    lineas = texto.readlines()
    texto = open(nombre,"w")
    texto.write(frase)
    for i in range(len(lineas)):
        texto.write(lineas[i])
    texto.close()

    
#EJERCICIO 7
def chau_comas(lista:list)->list:
    for i in range(len(lista)):
        if lista[i] == ",":
            lista.remove(lista[i])
    return lista

def promedio(lu:str) -> int:
    texto = open("promedio.csv","r")
    n = []
    for linea in texto:
        linea = chau_comas(linea.split())
        if lu == linea[0]:
            n.append(int(linea[3]))
    return (sum(n)/len(n))
#PILAS

#EJERCICIO 8
def generar_nros_azar(n: int,desde:int,hasta:int) -> pila:
    i = 0
    p = pila() 
    while i != n:
        p.put(random.randint(desde,hasta))
        i += 1
    return p


#EJERCICIO 9
def cantidad(p:pila) -> int:
    t = p
    n = 0
    while not(p.empty()):
        t.get()
        n += 1
    return n 


#EJERCICIO 10
def maximo(p:pila) -> int:
    t = p
    n = 0
    while not(t.empty()):
        l = t.get()
        if n < l:
            n = l
    return n 


#EJERCICIO 11
def balanceada(s:str) -> bool:
    p = pila()
    for i in range(len(s)):
        if s[i] == "(":
            p.put(1)
        if s[i] == ")":
            if p.empty():
                return False 
            else:
                p.get()
    if p.empty():
        return True 
    else:
        return False 


#EJERCICIO 12 


#DICCIONARIOS 

#EJERCICIO 19 
def agrupar_longitud(archivo:str) -> dict:
    texto = open(archivo,"r")
    lineas = texto.read()
    lista = lineas.split()
    resultado = {}
    for palabra in lista:
            longitud = len(palabra)
            if longitud in resultado:
                resultado[longitud] += 1
            else:
                resultado[longitud] = 1
    print(resultado)

#EJERCICIO 20
def libretas(nombre:str) -> list:
    texto = open(nombre,"r")
    n = []
    for linea in texto:
        linea = chau_comas(linea.split())
        n.append(linea[0])
    return n 
def promedioD(nombre:str)->dict:
    libretas = libretas(nombre)
    diccionario = {}
    for i in range(0,len(libretas)):
        diccionario[libretas[i]] = promedio(libretas[i])
    return diccionario


#EJERCICIO 22
p = pila()
def visitar_sitio(historial:dict,usuario:str,pagina:str):
    try:
        nuevo = historial[usuario]
        nuevo.put(pagina)
        historial[usuario] = nuevo
    except:
        historial[usuario] = pila()
        nuevo = historial[usuario]
        nuevo.put(pagina)
        historial[usuario] = nuevo

def navegar_atras(historial:dict, usuario:str):
    nuevo = historial[usuario]
    p.put(nuevo.get())
    historial[usuario] = nuevo

def navegar_adelante(historial:dict, usuario:str):
    nuevo = historial[usuario]
    nuevo.put(p.get())
    historial[usuario] = nuevo
historiales = {}
visitar_sitio(historiales, "Usuario1", "google.com")
visitar_sitio(historiales, "Usuario1", "facebook.com")
navegar_atras(historiales, "Usuario1")
visitar_sitio(historiales, "Usuario2", "youtube.com")
navegar_adelante(historiales, "Usuario1")
print(historiales["Usuario1"].queue)

#23 
def agregar_producto(inventario:dict,nombre:str,precio:float,cantidad:int):
    for llaves in inventario:
        if llaves == nombre:
            print("El producto ya esta en el inventario!!!")
    else:
        info = {}
        info["precio"] = precio
        info["cantidad"] = cantidad
        inventario[nombre] = info

def actualizar_stock(inventario:dict,nombre:str,cantidad:int):
    info = inventario[nombre]
    info["cantidad"] = cantidad

def calcular_valor_inventario(inventario:dict) -> float:
    n = 0
    for llaves in inventario:
        info = inventario[llaves]
        n += info["cantidad"]*info["precio"] 
    return n







        

    