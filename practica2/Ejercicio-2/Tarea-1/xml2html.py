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


def generarHTML(archivoXML):
    archivoHTML = archivoXML.replace(".xml",".html")
    archivoCSS = archivoXML.replace(".xml",".css")
    f = open(archivoHTML,'w',encoding='utf-8')


    title = '''
    <title>''' +archivoXML.replace(".xml","").capitalize()+'''</title>'''
    
    head = '''\n<head>\n\t<link rel="stylesheet" type="text/css" href=" '''+archivoCSS+''' " >\n\t<!-- Datos que describen el documento -->\n\t<meta charset="UTF-8" >'''+title+'''\n\t<meta name="viewport" content="width=device-width, initial scale=1.0" >\n\t<meta name="author" content="Nuria Inchaurrandieta Fernández">\n</head> '''
    
    header = ''' 
    <header> 
        <h1> '''+archivoXML.replace(".xml","").capitalize()+'''</h1>
    </header>'''

    arbol = abrirXML(archivoXML)

    raiz = arbol.getroot()

    main = '''\n\t<main> '''+generarLista(raiz)+'''\n\t</main>'''

    footer = '''\n\t<footer>\n\t\t<p>Práctica 2: XML</p>\n\t\t<p>Software y Estándares para la Web</p>\n\t\t<p>Escuela de Ingeniería Informática EII</p>\n\t\t<p>Universidad de Oviedo</p>\n\t\t<address>Puedes<a href="mailto:uo277418@uniovi.es"> enviar un correo </a> al autor si encuentras algún error en la página</address>\n\t</footer>'''

    body  = '''\n<body>'''+ header + main + footer + '''\n</body>'''

    html ='''<!DOCTYPE HTML>\n<html lang="es">'''+ head + body +'''\n</html>'''

    f.write(html)
    f.close()


def generarLista(raiz):
    tab="\n"

    string=generarHijos(raiz,tab)
    string+='''\n\t\t</ul>'''
    
    return string


def generarHijos(raiz,tab):
    tab+="\t\t"
    string=tab+'''<ul> '''

    # Recorrido de los elementos del árbol
    for hijo in raiz:
        sTag = tab+'''\t<li>'''+hijo.tag.replace("{http://tempuri.org/arbol}","")
        
        if hijo.text != None:
            tag = hijo.tag.replace("{http://tempuri.org/arbol}","")
            if (tag == 'foto'):
                string+=tab+'''\t<li><img src="'''+hijo.text+'''" alt="'''+hijo.text+'''" />'''
            elif (tag=='video'):
                string+=tab+'''\t<li><video src="'''+hijo.text+'''" controls preload="auto"></video>'''
            else:
                string+=sTag+": "+hijo.text.strip('\n')
        else:
            string+=hijo.text
        
        string+=str(hijo.attrib).replace("{}","").replace("{'nombre': '","").replace("', 'apellidos': '"," ").replace("'}","")
        if len(hijo) > 0:            
            string+=generarHijos(hijo,tab)+tab+'''\t\t</ul>'''
        string+='''</li>'''

    return string




def main():
    """Prueba de la función verXML()"""
        
    miArchivoXML = input('Introduzca un archivo XML = ')
    
    verXML(miArchivoXML)
    generarHTML(miArchivoXML)

if __name__ == "__main__":
    main()