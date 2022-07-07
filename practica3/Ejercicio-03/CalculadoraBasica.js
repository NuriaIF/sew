class Calculadora{
    constructor(){
        this.pantalla = new String();//se acumulan las teclas pulsadas
        this.memoria = new Number();
    }
    digitos(n){
        this.pantalla+=n;
        document.getElementsByName('textarea')[0].value = this.pantalla;
        
    }
    punto(){
        this.pantalla+='.';
        document.getElementsByName('textarea')[0].value = this.pantalla;
    }
    suma(){
        this.pantalla+='+';
        //console.log(this.pantalla);
        document.getElementsByName('textarea')[0].value = this.pantalla;
    }
    resta(){
        this.pantalla+='-';
        document.getElementsByName('textarea')[0].value = this.pantalla;
    }
    multiplicacion(){
        this.pantalla+='*';
        document.getElementsByName('textarea')[0].value = this.pantalla;
    }
    division(){
        this.pantalla+='/';
        document.getElementsByName('textarea')[0].value = this.pantalla;
    }
    mrc(){
        this.pantalla = this.memoria;
        document.getElementsByName('textarea')[0].value = this.pantalla;
    }
    mMenos(){
        this.memoria -= this.pantalla;
    }
    mMas(){
        this.memoria += this.pantalla;
    }
    borrar(){
        this.pantalla = "";
        document.getElementsByName('textarea')[0].value = this.pantalla;
    }
    igual(){
        var numberA=new String();
        var numberB=new String();
        var operacion = new String();
        var pos = 0;
        var resultado = 0;
        while(this.pantalla[pos] != '+' && this.pantalla[pos] != '-'
            &&this.pantalla[pos] != '*' && this.pantalla[pos] != '/') {
                numberA+=this.pantalla[pos];
                pos++;
            }

        operacion = this.pantalla[pos];
        pos++;

        while(this.pantalla[pos] != '+' && this.pantalla[pos] != '-'
            &&this.pantalla[pos] != '*' && this.pantalla[pos] != '/'
            && pos != this.pantalla.length) {
                numberB+=this.pantalla[pos];
                pos++;
            }
        
        var a = parseFloat(numberA);
        var b = parseFloat(numberB);
        switch (operacion){
            case '+':
                resultado = a + b;
                break;
            case '-':
                resultado = a - b;
                break;
            case '*':
                resultado = a * b;
                break;
            case '/':
                resultado = a / b;
        }
        this.pantalla = resultado + "";
        console.log(a+operacion+b+"="+this.pantalla);
        document.getElementsByName('textarea')[0].value = this.pantalla;
    }

    pulsarTecla(evento){
        switch (evento.keyCode() ){
            case 13:
                this.igual();
                break;
        }
        switch (String.valueOf(evento)) {
            case "1":
                this.digitos(1);
                break;
        }

    }

}
c = new Calculadora();
