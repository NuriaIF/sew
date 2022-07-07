
"use strict"
class Tiempo {
    constructor() {
        this.meteo = new Object()
        this.meteo.apikey = "52f3a6700c325fd0fd964e14704ee5c4"
        this.meteo.ciudad = "Oviedo"
        this.meteo.unidades = "&units=metric"
        this.meteo.idioma = "&lang=es"
        this.meteo.url = "http://api.openweathermap.org/data/2.5/weather?q=" + this.meteo.ciudad + this.meteo.unidades + this.meteo.idioma + "&APPID=" + this.meteo.apikey
        this.meteo.error = "<h2>¡problemas! No puedo obtener información de <a href='http://openweathermap.org'>OpenWeatherMap</a></h2>"
        this.infoRelevanteMeteo=new Object()
        this.cargarDatos()
        
    }

    cargarDatos() {
        var self=this
        this.meteo.datos=$.ajax({
            dataType: "json",
            url: self.meteo.url,
            method: 'GET',
            success: function (data) {
                self.seleccionarDatos(data)
                self.mostrarInfo()
            },
            error: function () {
                document.write(this.meteo.error);
            }
        });
    }
    seleccionarDatos(datos) {
        this.infoRelevanteMeteo.ciudad = datos.name
        this.infoRelevanteMeteo.pais =datos.sys.country
        this.infoRelevanteMeteo.latitud = datos.coord.lat
        this.infoRelevanteMeteo.longitud = datos.coord.lon
        this.infoRelevanteMeteo.tempActual = datos.main.temp
        this.infoRelevanteMeteo.tempSensacion = datos.main.feels_like
        this.infoRelevanteMeteo.tempMax = datos.main.temp_max
        this.infoRelevanteMeteo.tempMin = datos.main.temp_min
        this.infoRelevanteMeteo.presion = datos.main.pressure
        this.infoRelevanteMeteo.humedad = datos.main.humidity
        this.infoRelevanteMeteo.horaAmanecer = new Date(datos.sys.sunrise * 1000).toLocaleTimeString()
        this.infoRelevanteMeteo.horaOscurecer = new Date(datos.sys.sunset * 1000).toLocaleTimeString()
        this.infoRelevanteMeteo.direccionViento = datos.wind.deg
        this.infoRelevanteMeteo.velocidadVinto = datos.wind.speed
        this.infoRelevanteMeteo.tiempoMedida=new Object()
        this.infoRelevanteMeteo.tiempoMedida.hora = new Date(datos.dt * 1000).toLocaleTimeString()
        this.infoRelevanteMeteo.tiempoMedida.fecha = new Date(datos.dt * 1000).toLocaleDateString()
        this.infoRelevanteMeteo.visibilidad = datos.visibility
        this.infoRelevanteMeteo.descripcionTiempo = datos.weather[0].description
        this.infoRelevanteMeteo.nubosidad =datos.clouds.all
        this.infoRelevanteMeteo.icono = datos.weather[0].icon

    }
    mostrarInfo(){
        this.cabecera()
        this.infoGeneral()
        this.footer()
    }
    cabecera() {
        $("body>section header").html("<h1>El tiempo en " + this.infoRelevanteMeteo.ciudad +", "+ this.infoRelevanteMeteo.pais+"</h1>")
        console.log(JSON.stringify(this.infoRelevanteMeteo,null,1))
    }
    infoGeneral(){
        var inicial="<h2> Datos sobre el Tiempo de hoy</h2>"
        inicial+="<p><h3> Tiempo: </h3>"
        inicial+=this.infoRelevanteMeteo.descripcionTiempo
        inicial+="<img src=https://openweathermap.org/img/w/"+this.infoRelevanteMeteo.icono+".png alt=\"foto de "+this.infoRelevanteMeteo.descripcionTiempo+"\">"+"</p>"
        inicial+="<p><h3> Coordenadas: </h3>"+this.infoRelevanteMeteo.latitud+" "+this.infoRelevanteMeteo.longitud+"</p>"
        inicial+="<p><h3> Temperatura:</h3> Actual: "+this.infoRelevanteMeteo.tempActual+"º Sensacion Termica: "+this.infoRelevanteMeteo.tempSensacion+"º Maxima: "+this.infoRelevanteMeteo.tempMax+"º Minima: "+this.infoRelevanteMeteo.tempMin+"º</p>"
        inicial+="<p><h3> Presion: </h3>"+this.infoRelevanteMeteo.presion+"hPa</p>"
        inicial+="<p><h3> Humedad: </h3>"+this.infoRelevanteMeteo.humedad+"%</p>"
        inicial+="<p><h3> Viento: </h3> Velocidad: "+this.infoRelevanteMeteo.velocidadVinto+"m/s Direccion: "+this.infoRelevanteMeteo.direccionViento+"º</p>"
        inicial+="<p><h3> Visibilidad </h3> Metros de visibilidad: "+this.infoRelevanteMeteo.visibilidad
        inicial+="<p><h3> Horario: </h3> Hora de Amanecer: "+this.infoRelevanteMeteo.horaAmanecer+" Hora Anochecer: "+this.infoRelevanteMeteo.horaOscurecer+"</p>"
        inicial+="<p><h3> Nubes: </h3> Porcentaje de Nubosidad: "+this.infoRelevanteMeteo.nubosidad+"%</p>"
        console.log(inicial)
        $("body>section section[name=infogeneral]").html(inicial)
    }
    footer(){
        $("body footer").html("<p><h3> Hora de la Medida: </h3>" + this.infoRelevanteMeteo.tiempoMedida.fecha +", "+ this.infoRelevanteMeteo.tiempoMedida.hora+"</p>")
    }

}
var tiempo = new Tiempo()
function ciudad() {
    tiempo.ciudad()
}
function infoGeneral() {
    tiempo.infoGeneral()
}