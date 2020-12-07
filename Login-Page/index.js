//INTENTAR ENTENDER MAÑANA
const express = require('express');

const app = express();

app.use(express.json()); //Para que express pueda entender objetos JS

app.get('/', (req, res) =>{
    res.send("PETICIÓN GET RECIVIDA");
    res.end();
})


app.post('/user/:id',(req,res)=>{
    console.log(req.body);
    console.log(req.params);
    res.send("Post request recieved");
})

app.put('/put',(req, res)=>{
    res.send('Put request')
})

app.delete('/delete/:id',(req,res)=>{
    res.send('Delete request ${req.params.userId} deleted.');
})

app.listen(5000, ()=>{
    console.log("Server on port 5000");
})