function imagenAleatoria(){
    let num = Math.random();

    if (num<0.5){
        document.getElementById("No").style.display = "block";
    }
    else if (num > 0.5){
        document.getElementById("YES").style.display ="block";
    }
    else{
        document.getElementById("RUSIA").style.display ="block"
    }

}