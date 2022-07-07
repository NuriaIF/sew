import xml.etree.ElementTree as ET

def abrirXML(archivoXML):
    try:
        
        arbol = ET.parse(archivoXML)
        
    except IOError:
        print ('No se encuentra el archivo ', archivoXML)
        exit()
        
    except ET.ParseError:
        print("Error procesando en el archivo XML = ", archivoXML)
        exit()
       
    return arbol

def verXML(archivoXML):

    arbol = abrirXML(archivoXML)

    raiz = arbol.getroot()

    print("\nElemento raiz = ", raiz.tag)

    if raiz.text != None:
        print("Contenido = "    , raiz.text.strip('\n')) #strip() elimina los '\n' del string
    else:
        print("Contenido = "    , raiz.text)
        
    print("Atributos = "    , raiz.attrib)

    # Recorrido de los elementos del árbol
    for hijo in raiz.findall('.//'): # Expresión Path
        print("\nElemento = " , hijo.tag)
        if hijo.text != None:
            print("Contenido = ", hijo.text.strip('\n')) #strip() elimina los '\n' del string
        else:
            print("Contenido = ", hijo.text)    
        print("Atributos = ", hijo.attrib)


def generarSVG(archivoXML):
    archivoSVG = archivoXML.replace(".xml",".svg")
    f = open(archivoSVG,'w',encoding='utf-8')



    arbol = abrirXML(archivoXML)

    raiz = arbol.getroot()

    startDocument='<?xml version="1.0" standalone="no"?>'
    svgHeader = startDocument+'\n<svg xmlns="http://www.w3.org/2000/svg" width="10000" height="10000" style="overflow:visible" version="1.1">'

    svgEnd='</svg>'

    svg=svgHeader+generarArbol(raiz)+svgEnd
    

    f.write(svg)
    f.close()


def generarArbol(raiz):
    string=""

    for hijo in raiz:
        string+=generarHijos(hijo,1500,20,800)
    
    return string


def generarHijos(persona,x,y, distanciaX):
    string=""
    width=200
    height=40
    # Recorrido de los elementos del árbol
    tagRaiz =persona.tag.replace("{http://tempuri.org/arbol}","")
    
    #for hijo in raiz:
     #   tag = hijo.tag.replace("{http://tempuri.org/arbol}","")
    #escribir atributos
    atributo=str(persona.attrib).replace("{}","").replace("{'nombre': '","").replace("', 'apellidos': '"," ").replace("'}","")
    string+=escribirElemento(atributo,x,y,height,width)
    #escribir datos
    string+=escribirDatos(persona[0],x+10,y+50,height,width-20)
    string+=dibujarPath(x+width/2,y+height,x+width/2,y+50)
    
    if len(persona) > 1:
        #escribir padre
        string+=dibujarPath(x+width/2,y+height,x-distanciaX+width/2,y+height*5)
        string+=generarHijos(persona[1],x-distanciaX,y+height*5,distanciaX-500)
        #escribir madre
        string+=dibujarPath(x+width/2,y+height,x+distanciaX+width/2,y+height*5)
        string+=generarHijos(persona[2],x+distanciaX,y+height*5,distanciaX-500)

    
    return string


def escribirElemento(text,x,y,height,width):
    s = '\n<rect x="'+str(x)+'" y="'+str(y)+'" width="'+str(width)+'" height="'+str(height)+'" style="fill:indigo;stroke:plum;stroke-width:1"/>'
    s += '\n<text x="'+str(x+20)+'" y="'+str(y+height/2)+'" font-size="10" style="fill:plum">'+text+'</text>'
    return s

def escribirDatos(datos,x,y,height,width):
    s = '\n<rect x="'+str(x)+'" y="'+str(y)+'" width="'+str(width)+'" height="'+str(height+130)+'" style="fill:transparent;stroke:rebeccapurple;stroke-width:1"/>'
    
    incrementoY = 0
    s+='\n<text x="'+str(x+20)+'" y="'+str(y+height/2+incrementoY)+'" font-size="10" font-weight="bold" style="fill:rebeccapurple">'+'Nacimiento: '+'</text>'
    incrementoY+=10
    for elem in datos:
        tagElem = elem.tag.replace("{http://tempuri.org/arbol}","")
        if tagElem=='fechaFallecimiento':
            s+='\n<text x="'+str(x+20)+'" y="'+str(y+height/2+incrementoY)+'" font-size="10" font-weight="bold" style="fill:rebeccapurple">'+'Fallecimiento: '+'</text>'
            incrementoY+=10
            s += '\n<text x="'+str(x+20)+'" y="'+str(y+height/2+incrementoY)+'" font-size="10" style="fill:rebeccapurple">'+elem.text+'</text>'
            incrementoY+=10
        elif tagElem=='coordsNacimiento' or tagElem == 'coordsFallecimiento':
            s+='\n'
            for coord in elem:
                s += '<text x="'+str(x+20)+'" y="'+str(y+height/2+incrementoY)+'" font-size="10" style="fill:rebeccapurple">'+coord.text+' </text>'
                incrementoY+=10
        elif tagElem=='comentario' and len(elem.text) > 40:
            texto1 = elem.text[0:40]
            s += '\n<text x="'+str(x+20)+'" y="'+str(y+height/2+incrementoY)+'" font-size="10" style="fill:rebeccapurple">'+texto1+'</text>'
            incrementoY+=10
            texto2 = elem.text[40:len(elem.text)]
            s += '\n<text x="'+str(x+20)+'" y="'+str(y+height/2+incrementoY)+'" font-size="10" style="fill:rebeccapurple">'+texto2+'</text>'
            incrementoY+=10
        else:
            s += '\n<text x="'+str(x+20)+'" y="'+str(y+height/2+incrementoY)+'" font-size="10" style="fill:rebeccapurple">'+elem.text+'</text>'
            incrementoY+=10
    return s

def dibujarPath(xIni,yIni,xFin,yFin):
    s1 = "M" + str(xIni) + " " + str(yIni) + " C" + str(xFin) + " " + str(yIni) + " " + str(xIni) + " " + str(yFin) + " " + str(xFin) + " " + str(yFin)
    s = '<path d="'+s1+'" style="fill:transparent;stroke:black"/>'
    return s

def main():
    
    miArchivoXML = input('Introduzca un archivo XML = ')
    
    verXML(miArchivoXML)
    generarSVG(miArchivoXML)

if __name__ == "__main__":
    main()