var express = require('express')
var app = express()
const port = 3000

var Web3 = require('web3')
var web3 = new Web3()

if (typeof web3 !== 'undefined') {
    web3 = new Web3(web3.currentProvider)
} else {
    web3 = new Web3(new Web3.providers.HttpProvider('http://localhost:8545'))
}

app.get('/', (req, res) => {
    console.log(web3)
    res.sendFile(__dirname + '/test.html')
})

app.listen(port, () => {
    console.log("Listening on " + port)
})