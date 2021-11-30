"use strict"

class CalculadoraRPN {

    constructor (){
        this.screen=""
        this.stack=[]
        this.activatedShift=false
    }
    digitos(digit) {
        this.screen=this.screen.concat(digit)
        this.escribir(this.screen)
    }
    borrarUnNumero(){
        this.screen=this.screen.substring(0,this.screen.length-1)
        this.escribir(this.screen)
    }
    saveResult(result){
        this.screen=""
        this.stack.push(result+"")
        document.getElementsByName("text")[0].innerHTML=""
        this.drawStack(this.stack.length+1)
    }
    suma(){
        var result = parseFloat(this.stack.pop())+parseFloat(this.stack.pop())
        this.saveResult(result)
        console.log(result)
    }
    resta(){
        var num = parseFloat(this.stack.pop())
        var result = parseFloat(this.stack.pop())-num
        this.saveResult(result)
    }
    multiplicacion(){
        var result = parseFloat(this.stack.pop())*parseFloat(this.stack.pop())
        this.saveResult(result)
    }
    division(){
        var num = parseFloat(this.stack.pop())
        var result = parseFloat(this.stack.pop())/num
        this.saveResult(result)
    }
    punto(){
        this.screen=this.screen.concat('.')
        this.escribir(this.screen)
    }
    sin(){
        var result = Math.sin(this.stack.pop()) //en radianes
        this.saveResult(result)
    }
    cos(){
        var result = Math.cos(this.stack.pop()) //en radianes
        this.saveResult(result)
    }
    tan(){
        var result = Math.tan(this.stack.pop()) //en radianes
        this.saveResult(result)
    }
    asin(){
        var result = Math.asin(this.stack.pop()) //en radianes
        this.saveResult(result)
    }
    acos(){
        var result = Math.acos(this.stack.pop()) //en radianes
        this.saveResult(result)
    }
    atan(){
        var result = Math.atan(this.stack.pop()) //en radianes
        this.saveResult(result)
    }
    root(){
        var result = Math.root(this.stack.pop(),2) //en radianes
        this.saveResult(result)
    }
    powerTwoOf(){
        var result = Math.pow(this.stack.pop(),2) //en radianes
        this.saveResult(result)
    }
    
    enter(){
        this.stack.push(this.screen)
        console.log(this.stack)
        document.getElementsByName("text")[0].innerHTML = "<li>1: </li>"
        this.drawStack(this.stack.length+2)
        this.screen=""
    }

    escribir(content){
        document.getElementsByName("text")[0].innerHTML = "<li>1: "+content+"</li>"

        this.drawStack(this.stack.length+2)
    }

    drawStack(i){
        var s = ""
        this.stack.forEach(function(elemento,indice,array) {
            i=i-1
            s+="<li>"+i+": "+elemento+"</li>"
        })

        document.getElementsByName("text")[0].innerHTML =s+document.getElementsByName("text")[0].innerHTML
    }

    shift(){
        if(!this.activatedShift){
            document.getElementsByName("sin")[0].innerHTML='ASIN'
            document.getElementsByName("sin")[0].setAttribute('onclick',"calculadora.asin()")

            document.getElementsByName("cos")[0].innerHTML='ACOS'
            document.getElementsByName("cos")[0].setAttribute('onclick',"calculadora.acos()")

            document.getElementsByName("tan")[0].innerHTML='ATAN'
            document.getElementsByName("tan")[0].setAttribute('onclick',"calculadora.atan()")
            
            this.activatedShift = true
        } else {
            document.getElementsByName("sin")[0].innerHTML='SIN'
            document.getElementsByName("sin")[0].setAttribute('onclick',"calculadora.sin()")

            document.getElementsByName("cos")[0].innerHTML='COS'
            document.getElementsByName("cos")[0].setAttribute('onclick',"calculadora.cos()")

            document.getElementsByName("tan")[0].innerHTML='TAN'
            document.getElementsByName("tan")[0].setAttribute('onclick',"calculadora.tan()")

            this.activatedShift = false
        }
    }

}





var calculadora = new CalculadoraRPN()