var getData = function(){
    let horas = document.getElementById("horas").value;
    let minutos = document.getElementById("minutos").value;
    let preguntas = document.getElementById("preguntas").value;

    let horas_in_min = (parseFloat(horas)*60);
    let total_time = horas_in_min + parseFloat(minutos);

    tiempo_de_preguntas = total_time/parseFloat(preguntas);
    let entire_minutes = Math.trunc(tiempo_de_preguntas);
    let seconds = Math.round((tiempo_de_preguntas - entire_minutes)*60);

    if(preguntas <= 0 || (horas == 0 && minutos == 0)){
        alert("Datos erroneos, intentalo de nuevo.");
        location.reload()
    }
    else if (seconds > 1){
        if (entire_minutes >= 1){
            alert("Tienes " +entire_minutes+" minutos y " + seconds + " segundos por pregunta.");
        }
        else{
            alert("Tienes "+seconds+ " segundos por preguntas.");
        }        
    }
    else if (entire_minutes > 0){
        alert("Tienes " + entire_minutes + " minutos por pregunta.");
    }
}

var iniciarContador = function(){


}


var restartData = function(){
    document.getElementById("horas").value = "0";
    document.getElementById("preguntas").value = "0";
    document.getElementById("minutos").value = "0";
}