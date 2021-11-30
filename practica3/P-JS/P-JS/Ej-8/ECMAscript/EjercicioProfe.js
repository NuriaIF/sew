    //Versión 1.0 01/03/2011 Juan Manuel Cueva Lovelle. Universidad de Oviedo
	//Versión 1.1 23/10/2021 Revisión HTML y CSS
	//Versión 1.2 07/11/2021 jQuery 3.6.0
    var meteo = new Object();
    meteo.apikey = "47b790fd0fc41878c80c57c9846132cb";
    meteo.ciudad = "Oviedo";
    meteo.unidades = "&units=metric";
    meteo.idioma = "&lang=es";
    meteo.url = "http://api.openweathermap.org/data/2.5/weather?q=" + meteo.ciudad + meteo.unidades + meteo.idioma + "&APPID=" + meteo.apikey;
    meteo.error = "<h2>¡problemas! No puedo obtener información de <a href='http://openweathermap.org'>OpenWeatherMap</a></h2>";
    meteo.cargarDatos = function(){
        $.ajax({
            dataType: "json",
            url: meteo.url,
            method: 'GET',
            success: function(data){
                meteo.datos = data;
                meteo.verJSON();
                meteo.verDatos();            
            },
            error:function(){
                document.write(meteo.error);    
            }
        });
    }
    meteo.verJSON = function(){
        document.write("<h1>Datos en JSON desde <a href='http://openweathermap.org'>OpenWeatherMap</a></h1>");
        document.write("<h2>JSON</h2>")
        var str = JSON.stringify(meteo.datos, null, 2);
        document.write("<pre>" + str + "</pre>");
    }
    meteo.verDatos = function(){
        
        document.write("<h2>Datos</h2>")
        document.write("<p>Ciudad: " + meteo.datos.name + "</p>");
        document.write("<p>País: " + meteo.datos.sys.country + "</p>");
        document.write("<p>Latitud: " + meteo.datos.coord.lat + " grados</p>");
        document.write("<p>Longitud: " + meteo.datos.coord.lon + " grados</p>");
        document.write("<p>Temperatura: " + meteo.datos.main.temp + " grados Celsius</p>");
        document.write("<p>Temperatura máxima: " + meteo.datos.main.temp_max + " grados Celsius</p>");
        document.write("<p>Temperatura mínima: " + meteo.datos.main.temp_min + " grados Celsius</p>");
        document.write("<p>Presión: " + meteo.datos.main.pressure + " milímetros</p>");
        document.write("<p>Humedad: " + meteo.datos.main.humidity + "%</p>"); 
        document.write("<p>Amanece a las: " + new Date(meteo.datos.sys.sunrise *1000).toLocaleTimeString() + "</p>"); 
        document.write("<p>Oscurece a las: " + new Date(meteo.datos.sys.sunset *1000).toLocaleTimeString() + "</p>"); 
        document.write("<p>Dirección del viento: " + meteo.datos.wind.deg + "  grados</p>");
        document.write("<p>Velocidad del viento: " + meteo.datos.wind.speed + " metros/segundo</p>");
        document.write("<p>Hora de la medida: " + new Date(meteo.datos.dt *1000).toLocaleTimeString() + "</p>");
        document.write("<p>Fecha de la medida: " + new Date(meteo.datos.dt *1000).toLocaleDateString() + "</p>");
        document.write("<p>Descripción: " + meteo.datos.weather[0].description + "</p>");
        document.write("<p>Visibilidad: " + meteo.datos.visibility + " metros</p>");
        document.write("<p>Nubosidad: " + meteo.datos.clouds.all + " %</p>");
    };