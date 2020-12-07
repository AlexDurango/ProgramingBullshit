function getRandomNumber(size){
    return Math.floor(Math.random() * size);
}

let getDistance = (e, target) => {
    let diffx = e.offsetX - target.x;
    let diffy = e.offsetY - target.y;

    return Math.sqrt((diffx*diffx)+(diffy+diffy));
}

let getDistanceHint = distance => {
    if (distance < 30){
        return "Muy pero que muy caliente";
    }
    else if (distance < 50){
        return "Caliente";
    }
    else if (distance < 70){
        return "Un poco caliente";
    }
    else if (distance < 100){
        return "Un poquitito caliente";
    }
    else if (distance < 150){
        return "Frio";
    }
    else if (distance < 200){
        return "Bastante frio";
    }
    else if (distance < 250){
        return "Muy frio";
    }
    else if (distance < 300){
        return "Más frio que un helado :v";
    }
    else{
        return "Más frio que Balto";
    }
}