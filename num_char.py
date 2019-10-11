"""
ANTECEDENTES 
-------------
La primera version de numeros a letras se construyó en 1993 en clipper para ayudar a mi amigo Paulino para transferir las notas de los alumnos de la Escuela de Enseñanza de Automoción del EA a la Direccion de Enseñanza que pedia las mismas, aparte de en su valor numerico, como cadena de caracteres. Se desarrollo en Clipper (summer 87) en una función que gestionaba enteros del 1 al 10 y decimales de .01 al .99  

La siguiente versión fue como diversión en 2006. Se desarrollo en Alaska-SW, una adaptacion de Clipper con Orientación a Objetos. La función solo gestionaba enteros hasta Quintillones (36 cifras).

En 2019 estudiando Python (3) la he adaptado para este lenguaje, que es la que presento.

@ JuanPi
1993-2019

IDEAS PARA SU CONSTRUCCIÓN
-------------------------
Dentro del leguaje (español de España) cuando expresamos numeros, lo primero que he intentado es agrupar las expresiones comunes y encontrar excepciones lo que revierte complejidad a las funciones.

Algunas excepciones:
- El cero, como unico valor (no lo he querido tratar, saldrá un blanco, es facil tratarlo si se desea)
- El uno, puede expresarse como (un / uno) ej.: un millon..., trescientos treinta y uno
- Hay otras mas ...

He agrupado las expresiones comunes en FUNCIONES:
Vereis que todas tienen un diccionario local para devolver expresiones.

1º d0a9(...) representa los valores de 0 a 9 (ojo: el cero no como unico valor, 1001)

2º d10a20(...) representa los valores de 10 a 20 . Porqué el 20 y no hasta el 19, otra excepción: Hay una diferencia en el lenguaje con las decenas que en el caso del 20 es veinte y  2? venti..., que no pasa con el resto de decenas, 30:treinta, 32: treinta y dos. Observad también que se contruyen de manera diferente hay una "y" por medio.
22 -> ventidos
42 -> cuarenta y dos

3º d21a99(...) representa las decenas que son constantes excepto el caso de las veintenas como que comentó anteriormente

4º d100a999(...) representan a las centenas, que presenta una excepción 100:cien y 10?:ciento.. (similar a lo comentado con el 20), la excepción 100 se trata en la propia función.

5º miles(...) Representa a los miles y a los ...illones (millones, billones,...), fijaros que en lenguaje hasta que no se alcanza 7 cifras, 13 cifras, 19 cifras ... no pasamos a los ...illones, esta función es algo mas compleja de entender que las anteriores. Solo llego hasta los Quintillones, pero a partir de esta función podemos llegar hasta donde queramos. 

EXTRATEGIA DE RESOLUCIÓN:
Recibida cualquier cadena, hay al principio algunas expresiones que validan la cadena para convertirla en una cadena numerica. Quitar comas, puntos, caracteres alfabeticos ...

Validada la cadena numerica se trata de pasarla a una lista de la siguiene forma:
1235698733 -> ["1","235","698","733"] 

Entraremos en un FOR analizando cada uno de los elemenos de la lista, discriminaremos si nos llego una cadena de 3,2 ó 1 caracteres, pues tienen analisis diferentes.

Caso 3 caracteres: Se va analizando (> 100, mayor de 20, entre 10 y 20 ...) definido donde entra, dentro del mismo se va partiendo y analizando. Construyendo su expresión con las funciones.

"""
#*****************************
# FUNCIONES BASICAS DE APOYO
#*****************************
###############
def d0a9(pipo,lfin):
###############
    """
    Función para los valores comprendidos entre 0 y 9

    Argumentos:
    - pipo : un caracter numerico
    - lfin : un boleano.

    La función devuelve la expresión que representa dicho caracter numerico. El caso del caracter numerico 1 es especial
    NOTA: El tratamiento del valor '0' no representa la expresión: 'cero'

    ej:
    231.000 -> el 1 en esta cadena numerica es "un" (doscientos treinta y un mil)
    321     -> el 1 en esta cadena numerica es "uno" (trescientos ventiuno)

    """
    d0_9 = {'0':'',
            '1':['un ','uno'],
            '2':'dos ',
            '3':'tres ',
            '4':'cuatro ',
            '5':'cinco ',
            '6':'seis ',
            '7':'siete ',
            '8':'ocho ',
            '9':'nueve '}


    if pipo in  d0_9:
        if  pipo == "1":
            if lfin:
                return d0_9[pipo][0]
            else:
                return d0_9[pipo][1]
        
        else:    
                return d0_9[pipo]
    else:
        return  None

#################
def d10a20(pipo):
#################
    """
    Función para los valores comprendidos entre 10 y 20

    Argumentos:
    - pipo : un caracter numerico

    La función devuelve la expresión que representa dicho caracter numerico.

    """

    d10_20 = {'10':'diez ',
              '11':'once ',
              '12':'doce ',
              '13':'trece ',
              '14':'catorce ',
              '15':'quince ',
              '16':'dieciseis ',
              '17':'diecisiete ',
              '18':'dieciocho ',
              '19':'diecinueve ',
              '20':'veinte '}
    
    if pipo in  d10_20:
        return d10_20[pipo]
    else:
        return  None

##################
def d21a99(pipo):
##################
    """
    Función para los valores comprendidos entre  21 y 99

    Argumentos:
    - pipo : un caracter numerico

    La función devuelve la expresión que representa dicho caracter numerico.

    """

    d21_99 = {'2':'venti',
              '3':'treinta ',
              '4':'cuarenta ',
              '5':'cincuenta ',
              '6':'sesenta ',
              '7':'setenta ',
              '8':'ochenta ',
              '9':'noventa '}

    if pipo in  d21_99:
        return d21_99[pipo]
    else:
        return  None

###################
def d100a999(pipo):
####################
    """
    Función para los valores comprendidos entre  100 y 999

    Argumentos:
    - pipo : un caracter numerico

    La función devuelve la primera expresión que representa dicho caracter numerico.
    Nota: la cadena mumerica "100", presenta la excepción (cien/ciento)

    """

    d100_999 = {'1':'ciento ',
                '2':'doscientos ',
                '3':'trescientos ',
                '4':'cuatrocientos ',
                '5':'quinientos ',
                '6':'seiscientos ',
                '7':'setecientos ',
                '8':'ochocientos ',
                '9':'novecientos '}
 
    # excepcion un "cien" por "ciento"
    if pipo == '100':
        return  'cien '
    else:  
        pipo = pipo[0]
        if pipo in d100_999:
            return  d100_999[pipo]
        else:
            return None

###################
def miles(lista, n,clt):
# NOTA: No olvidar que las lista empiezan en cero    
####################
    """
    Función para los miles y ...illones(millones, billones, trillones, ...)

    Argumentos:
    - lista : Lista de cadenas
    - n     : Un numeros
    - clt   : Una cadena

    La función devuelve uno de los valores del diccionario

    """

    npos = 0
    pipo = len(lista) - n
    
    # bloque de trabajo
    nbl1 = lista[n-1]
   
    #cadena de 2 grupos el suyo y el anterior si procede, se analizan en el caso de ...illones
        
    if n > 1:
        nbl2 = lista[n-2] + lista [n-1]
    else:
        nbl2 = lista[n-1]
    
    aval = { 0:'',                                 # 1  npos
             1:'mil ',                             # 2
             2:['millones, ','millón, '],            # 3
             3:'mil ',                             # 4
             4:['billones, ','billón, '],            # 5
             5:'mil ',                             # 6
             6:['trillones, ','trillón, '],          # 7
             7:'mil ',                             # 8
             8:['cuatrillones, ','cuatrillón, '],    # 9
             9:'mil ',                             # 10
             10:['quintillones, ','quintillón, '],   # 11
             11:'mil ' }                           # 12
    
    if pipo in aval:
        npos = pipo + 1
    
    if npos == 2 or npos== 4 or npos == 6 or npos== 8 or npos == 10 or npos == 12:
        
        #grupo de miles
        if int(nbl1) == 0:
            return aval[0] # en nuestro caso una cadena vacia
        
        elif int(nbl1) == 1:
            return aval[pipo]
        else:
            return clt + aval[pipo]
  
    elif npos == 3 or npos== 5 or npos == 7 or npos== 9 or npos == 11:
        
        # grupo de ..illones
        if int(nbl2) == 0:
            return aval[0] # en nuestro caso una cadena vacia
    
        elif int(nbl2) == 1:
            return clt + aval[pipo][1]
        
        else:
            return clt + aval[pipo][0]
            
    elif npos == 1:
        return clt + aval[pipo]
    else:
        return "SUPERADO MAXIMO PERMITIDO ..."

#*******************
# FUNCION PRINCIPAL
#*******************
def dnumachar(pipo):
    """
    Función principal de este módulos

    Argumentos:
    - pipo : una cadena de numeros de cadenas

    La función devuelve una cadena con la expresion en español de la cadena de numeros recibida.

    """   
    
    # VALIDACIONES
    
    # quitar cualquier blanco
    pipo = pipo.replace(" ", "")
    
    # partir parte entera y parte decimal si la hubiera
    npos = pipo.find(".") 

    if npos > 0: # hay parte entera y parte decimal
        int_pipo = pipo[:npos]
        dec_pipo = pipo[npos+1:]
    else: # solo hay parte entera
        int_pipo = pipo
        dec_pipo = ""
        
    # quitamos en lo obtenido las comas separadoras de miles si las hubiera 
    int_pipo = int_pipo.replace(",", "")
    dec_pipo = dec_pipo.replace(",", "")

    # verificar que no nos han colado cualquier otro carater diferente de numeros
    if not int_pipo.isdigit(): 
        print("no valen ni letras, ni caracteres especiales")
        return None


    # SOLO trabajaremos con la parte entera.
    # crearemos una lista en grupos de 3  ejemplo: 1234568 -> ["1","234","568"]

    npos = len(int_pipo)
    ctmp = ""
    l_int_pipo = []

    for i in range(1,npos+1) :
        # voy agrupando los ultimos caracteres y quitandolos de int_pipo
        ctmp = int_pipo[-1] + ctmp 
        int_pipo = int_pipo[:-1]

        # Si recorrido 3 posiciones la añado a la lista
        if i%3 == 0:
            l_int_pipo = [ctmp] + l_int_pipo
            ctmp = "" 
            
    # Si no llegue a 3 posiciones, me sobraron, y los añado a continuación
    if len(ctmp) > 0:
        l_int_pipo = [ctmp] + l_int_pipo
        
    # print("Lista de trabajo:",l_int_pipo)

    clet = ""  # variable que contendrá la expresion de la cadena numerica.
    npos = 0   # variable que determina posicion en la lista

    # ANALISIS DE LA LISTA (se analizan los bloques en nuestro ejemplo: "12" ,"234" ... )
    for i in l_int_pipo:
        
        clettmp = ""
        npos += 1
        
        # Saber si estamos en el ultimo bloque de la lista (excepción del  "1" (uno ó un)) 
        if (len(l_int_pipo) - npos) == 0 :
            lkey = False
        else:
            lkey = True
        
        # Tenemos 3 caracteres numericos en la cadena
        
        if len(i) == 3:  
                          
            """ grupo de 3 elementos completo
                se repasa la casuistica de grupo completa:
                (a,b,c)>=100  -> d100a999
                (b,c)>20    -> d21a99+d9a0
                (b,c)>=10 y (b,c)>=10 ->  d10a20
                (c) resto -> d1a9 
            """
            
            if int(i) >= 100:
                clettmp += d100a999(i)
                
            if int(i[1:]) > 20:
                clettmp += d21a99(i[1:2])  #Paso de la cadena numerica la 2º posicion
                
                # No poner 'y' entre 21..29 y si en el resto de decenas (30,40,...)
                if int(i[1:]) < 30 or int(i[1:])%10 == 0 :
                    clettmp += ""
                else:         
                    clettmp += "y "
                    
                clettmp += d0a9(i[-1], lkey)  #Paso de la cadena numerica la ultima posición 
        
            elif int(i[1:]) >= 10 and int(i[1:]) <= 20:
                clettmp += d10a20(i[1:]) #Paso de la cadena numerica las dos ultima posiciones 
                
            else: 
                clettmp += d0a9(i[-1], lkey)  
                
                
        # tenemos 2 caracteres numericos en la cadena        
        elif  len(i) == 2: 
            
            # De manera similar a cuando teniamos 3 caracteres numericos lo analizamos con 2
            
            if int(i) > 20:
                clettmp += d21a99(i[0])  # paso primera posición   
                
                # salvar 'y' en 21..29 y multiplos de 10
                if int(i) < 30 or int(i)%10 == 0 :
                    clettmp += ""
                else: 
                    clettmp += "y "
                    
                clettmp += d0a9(i[-1], lkey)   
        
            elif int(i) >= 10 and int(i) <= 20:
                clettmp += d10a20(i)
                
            else: 
                clettmp += d0a9(i, lkey) 
    
        # tenemos 1 solo caracter numerico en la cadena   
        elif  len(i) == 1: 
            clettmp += d0a9(i, lkey)
            
        # Analisis de miles y millones
        clet += miles(l_int_pipo,npos,clettmp)
            
    # Recreo el numero añadiendo separadores comas de miles para verificar 
    csal = ""
    npos = 0
    for i in l_int_pipo:
        npos += 1
        if npos > 1:
            csal += (","+i) 
        else:
            csal += i 

    # lo que veras en pantalla
    print(csal)
    return clet.capitalize()

