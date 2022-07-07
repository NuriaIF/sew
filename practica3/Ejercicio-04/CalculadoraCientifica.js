class CalculadoraCientifica extends Calculadora {
    constructor(){
        super();
    }

    mc(){
        this.memoria ="";
    }
    ms(){
        this.memoria = this.pantalla;
    }
    nd(){
        //Al activar se pone tecla azul
        //Cambia x2->x3 2raiz->3raiz
        //x^y->yraizx
        //10^x->2^x
        //log->log basey x
        //ln->e^x
    }
    pi(){
        this.pantalla+=Math.PI;
        document.getElementsByName('textarea')[0].value = this.pantalla;
    }
    e(){
        //
    }
    borrarUltimo(){
        this.pantalla = this.pantalla.replace(/.$/,'');
        document.getElementsByName('textarea')[0].value = this.pantalla;
    }
    cuadrado(){
        //coge el numero escrito y lo eleva al cuadrado
        //var a = this.obtenerUltimoNumero()[0];
        //var pos = this.obtenerUltimoNumero()[1];
        var numberA=new String();
        var pos = this.pantalla.length-1;
        while(this.pantalla[pos] != '+' && this.pantalla[pos] != '-'
            &&this.pantalla[pos] != '*' && this.pantalla[pos] != '/'
            && pos!=-1) {
                numberA=this.pantalla[pos]+numberA;
                pos--;
            }
        var a = parseFloat(numberA);
        var resultado = Math.pow(a,2);
        console.log(a);
        //this.pantalla=resultado;
        this.pantalla = this.pantalla.toString().substring(0,pos+1)+resultado;
        document.getElementsByName('textarea')[0].value = this.pantalla;
    }
    fraccion(){

    }
    absoluto(){

    }
    exp(){

    }
    mod(){

    }
    raiz(){
        //var a = this.obtenerUltimoNumero()[0];
        //var pos = this.obtenerUltimoNumero()[1];
        var numberA=new String();
        var pos = this.pantalla.length-1;
        while(this.pantalla[pos] != '+' && this.pantalla[pos] != '-'
            &&this.pantalla[pos] != '*' && this.pantalla[pos] != '/'
            && pos!=-1) {
                numberA=this.pantalla[pos]+numberA;
                pos--;
            }
        var a = parseFloat(numberA);
        var resultado = Math.sqrt(a);
        this.pantalla = this.pantalla.toString().replace(a,resultado);
        document.getElementsByName('textarea')[0].value = this.pantalla;
    }

    obtenerUltimoNumero(){
        var numberA=new String();
        var pos = this.pantalla.length-1;
        while(this.pantalla[pos] != '+' && this.pantalla[pos] != '-'
            &&this.pantalla[pos] != '*' && this.pantalla[pos] != '/'
            && pos!=-1) {
                numberA=this.pantalla[pos]+numberA;
                pos--;
            }
        var a = parseFloat(numberA);
        return a, pos;
    }



}

var c = new CalculadoraCientifica();
