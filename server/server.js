const express = require("express")
const cors = require("cors")
const airports = require("../data/airports.json")
const iguazu = require("../data/iguazu.json")
const { exec } = require("child_process")
const path = require("path")

const app = express()

const PORT = process.env.PORT ?? 8080

app.use(cors())

app.disable("x-powered-by")

app.get("/airports", (req, res)=>{
    res.status(200).json(airports)
})

app.get("/scrape", (req, res)=>{

    const origin = req.query["origin"]
    const destination = req.query["destination"]
    
    const scriptDir = path.join(__dirname, "..", "scraping/request.py")
    const envDir = path.join(__dirname, "..", "env/Scripts/activate")
    const command = `${envDir} && python ${scriptDir}`


    exec(`${command} ${origin} ${destination}`, (error, stdout, stderr) => {
      if (error) {
        console.error(`Error al ejecutar el script: ${error.message}`)
        return res.status(500).json({ error: 'Error en el scraping' })
      }
      if(stderr){
        console.log(`error: ${stderr}`)
      }
      console.log("Scraping exitoso")
      const data = JSON.parse(stdout)
      if(data.length > 0){
          res.json(data)
      }
      else{res.json(null)}
    })
})

// endpoint para realizar pruebas cuando me banean la ip
// app.get("/iguazu", (req, res) => {
// 	res.status(200).json(iguazu)
// })

app.listen(PORT, () => {
    console.log(`Servidor iniciado en el puerto ${PORT}`)
})