import xml.etree.ElementTree as ET

def abrirXAML(archivoXAML):
    try:
        
        arbol = ET.parse(archivoXAML)
        
    except IOError:
        print ('No se encuentra el archivo ', archivoXAML)
        exit()
        
    except ET.ParseError:
        print("Error procesando en el archivo XAML = ", archivoXAML)
        exit()
       
    return arbol

def verXAML(archivoXAML):

    arbol = abrirXAML(archivoXAML)

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


def generarHTML(archivoXAML):
    archivoHTML = archivoXAML.replace(".xaml","_explicacion.html")
    archivoCSS = "XAML_explicacion.css"
    f = open(archivoHTML,'w',encoding='utf-8')


    title = '''
    <title>''' +archivoXAML.replace(".XAML","").capitalize()+'''</title>'''
    
    head = '''\n<head>\n\t<link rel="stylesheet" type="text/css" href=" '''+archivoCSS+''' " >\n\t<!-- Datos que describen el documento -->\n\t<meta charset="UTF-8" >'''+title+'''\n\t<meta name="viewport" content="width=device-width, initial scale=1.0" >\n\t<meta name="author" content="Nuria Inchaurrandieta Fernández">\n</head> '''
    
    header = ''' 
    <header> 
        <h1> '''+archivoXAML.replace(".xaml","").capitalize()+'''</h1>
    </header>'''

    arbol = abrirXAML(archivoXAML)

    raiz = arbol.getroot()

    main = '''\n\t<main> '''+recorrerElementos(raiz)+'''\n\t</main>'''

    footer = '''\n\t<footer>\n\t\t<p>Práctica 2: XAML</p>\n\t\t<p>Software y Estándares para la Web</p>\n\t\t<p>Escuela de Ingeniería Informática EII</p>\n\t\t<p>Universidad de Oviedo</p>\n\t\t<address>Puedes<a href="mailto:uo277418@uniovi.es"> enviar un correo </a> al autor si encuentras algún error en la página</address>\n\t</footer>'''

    body  = '''\n<body>'''+ header + main + footer + '''\n</body>'''

    html ='''<!DOCTYPE HTML>\n<html lang="es">'''+ head + body +'''\n</html>'''

    f.write(html)
    f.close()


def recorrerElementos(raiz):
    string=''
    string+=explicarElemento(raiz)
    string+=recorrerElementosRec(raiz)
    return string

def recorrerElementosRec(raiz):
    string=''
    for hijo in raiz:
        string+=explicarElemento(hijo)
        if len(hijo) > 0:
            string+=recorrerElementosRec(hijo)
    return string


def explicarElemento(elemento):
    string=""
    # Recorrido de los elementos del árbol
    
    tag = elemento.tag.replace("{http://xamarin.com/schemas/2014/forms}","").replace("{http://schemas.microsoft.com/winfx/2006/xaml/presentation}","")
    if tag=='Window':
        string+='<h2>Window</h2>'
        string+='<p>Es una ventana</p>'
    elif tag=='Grid':
        string+='<h3>Grid</h3><p>Se encarga de la disposición de los elementos.</p>'
    elif tag == 'ContentPage':
        string+='<h2>Content Page</h2> <p>Establece el contenido de la página</p>'
    elif tag == 'ContentPage.Content':
        string+='<p>'
        string+='ContentPage.Content: Forman parte de la sintaxis única de XAML. Se denominan etiquetas de elemento de propiedad.</p>'
    elif tag == 'StackLayout':
        string+='<h3>StackLayout</h3><p>Diseño del contenido. Es una colección que puede contener varias vistas.</p>'
    elif tag == 'Label': 
        texto=elemento.attrib.get('Text')
        if texto == None:
            txt=''
        else:
            txt = '("'+str(texto)+'")'
        string+='<h3>Label'+txt+'</h3> <p>Es una etiqueta no interactuable para el usuario. Contiene un texto.</p>'
    elif tag == 'Button':
        texto=elemento.attrib.get('Content')
        if texto == None:
            txt=''
        else:
            txt = '("'+str(texto)+'")'
        string+='<h3>Button'+txt+'</h3> <p>Es un botón interactuable para el usuario.</p>'
    elif tag=='Slider':
        string+='<h3>Slider</h3> <p>Muestra un valor modificable para el usuario.</p>'
    elif tag=='Rectangle':
        string+='<p>Rectangle: Esto es un rectángulo</p>'
    else:
        string+='<p>No se encuentra información disponible sobre el elemento "'+tag+'"</p>'
        
    return '\n'+string

def main():
        
    miArchivoXAML = input('Introduzca un archivo XAML = ')
    
    verXAML(miArchivoXAML)
    generarHTML(miArchivoXAML)

if __name__ == "__main__":
    main()