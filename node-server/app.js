
var express = require('express')
var app = express()
app.use('/media', express.static(__dirname + '/media'))
const port = 3000

app.get('/', (req, res) => {
    res.sendFile(__dirname + '/test.html')
})

app.post('/create_contract', (req, res) => {
    
})

app.listen(port, () => {
    console.log("Listening on " + port)
})