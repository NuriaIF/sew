from os import scandir
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


def generarKML(archivoXML):
    archivoKML = archivoXML.replace(".xml",".kml")
    archivoCSS = archivoXML.replace(".xml",".css")
    f = open(archivoKML,'w',encoding='utf-8')


    title = '''
    <title>''' +archivoXML.replace(".xml","").capitalize()+'''</title>'''
    
    head = '''\n<head>\n\t<link rel="stylesheet" type="text/css" href=" '''+archivoCSS+''' " >\n\t<!-- Datos que describen el documento -->\n\t<meta charset="UTF-8" >'''+title+'''\n\t<meta name="viewport" content="width=device-width, initial scale=1.0" >\n\t<meta name="author" content="Nuria Inchaurrandieta Fernández">\n</head> '''
    
    header = ''' 
    <header> 
        <h1> '''+archivoXML.replace(".xml","").capitalize()+'''</h1>
    </header>'''

    arbol = abrirXML(archivoXML)

    raiz = arbol.getroot()

    #main = '''\n\t<main> '''+generarLista(raiz)+'''\n\t</main>'''

    #footer = '''\n\t<footer>\n\t\t<p>Práctica 2: XML</p>\n\t\t<p>Software y Estándares para la Web</p>\n\t\t<p>Escuela de Ingeniería Informática EII</p>\n\t\t<p>Universidad de Oviedo</p>\n\t\t<address>Puedes<a href="mailto:uo277418@uniovi.es"> enviar un correo </a> al autor si encuentras algún error en la página</address>\n\t</footer>'''

    #body  = '''\n<body>'''+ header + main + footer + '''\n</body>'''

    #html ='''<!DOCTYPE HTML>\n<html lang="es">'''+ head + body +'''\n</html>'''

    kml = '''<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://www.opengis.net/kml/2.2">
<Document>

'''+generarCoords(raiz)+'''

</Document>
</kml>'''

    f.write(kml)
    f.close()


def generarCoords(raiz):
    for hijo in raiz:
        string=generarHijos(hijo,hijo)
    
    return string


def generarHijos(raiz,nodo):
    string="\n"

    # Recorrido de los elementos del árbol

    for hijo in nodo:
        sTag = hijo.tag.replace("{http://tempuri.org/arbol}","")
        if sTag == 'coordsNacimiento':
            string+='<Placemark><name>'+str(raiz.attrib).replace("{'nombre': '","").replace("', 'apellidos': '"," ").replace("'}","")+'</name>'
            string+='<description>Nacimiento</description>'
            string+='''\n<Style><IconStyle>
<color>FF00FF14</color>
<scale>1.4</scale>
</IconStyle></Style>'''
            string+='<Point><coordinates>\n\t'
            for coordenada in hijo:
                string+= coordenada.text
                coordTag = coordenada.tag.replace("{http://tempuri.org/arbol}","")

                if coordTag != 'altitud':
                    string+=','
            string+='</coordinates></Point></Placemark>'

        elif sTag == 'coordsFallecimiento':
            string+='<Placemark><name>'+str(raiz.attrib).replace("{'nombre': '","").replace("', 'apellidos': '"," ").replace("'}","")+'</name>'
            string+='<description>Fallecimiento</description>'
            string+='''\n<Style><IconStyle>
<color>FF1400FF</color>
<scale>1.4</scale>
</IconStyle></Style>'''
            string+='<Point><coordinates>'
            for coordenada in hijo:
                string+= coordenada.text
                coordTag = coordenada.tag.replace("{http://tempuri.org/arbol}","")

                if coordTag != 'altitud':
                    string+=','
            string+='</coordinates></Point></Placemark>'

        if len(hijo) > 0:
            if (sTag=='persona'):            
                string+=generarHijos(hijo,hijo)
            else:
                string+=generarHijos(raiz,hijo)
        

    return string




def main():
    """Prueba de la función verXML()"""
    
    miArchivoXML = input('Introduzca un archivo XML = ')
    
    verXML(miArchivoXML)
    generarKML(miArchivoXML)

if __name__ == "__main__":
    main()