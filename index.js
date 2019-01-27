const express = require('express')
const app = express()
const PORT = process.env.PORT || 3000
const data = require('./scripts/parsed')

app.set('json spaces',4)

app.listen(PORT,()=>{
    console.log("Live at "+PORT)
})

app.get('/',(request,response)=>{
    response.json(data)
})