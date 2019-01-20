var Web3;

var abi = [
	{
		"constant": false,
		"inputs": [],
		"name": "stopContract",
		"outputs": [],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": false,
		"inputs": [],
		"name": "decCounter",
		"outputs": [],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": false,
		"inputs": [],
		"name": "incCounter",
		"outputs": [],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [],
		"name": "getCount",
		"outputs": [
			{
				"name": "",
				"type": "int256"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "constructor"
	},
	{
		"anonymous": false,
		"inputs": [
			{
			    "indexed": false,
				"name": "count",
				"type": "int256"
			}
		],
		"name": "counterIncEvent",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": false,
				"name": "count",
				"type": "int256"
			}
		],
		"name": "counterDecEvent",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": false,
				"name": "result",
				"type": "bool"
			}
		],
		"name": "contractErasedEvent",
		"type": "event"
	}
];

var byteCode = "0x60806040526000805560018060146101000a81548160ff02191690831515021790555034801561002e57600080fd5b5033600160006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff1602179055506102928061007f6000396000f3fe608060405234801561001057600080fd5b5060043610610069576000357c01000000000000000000000000000000000000000000000000000000009004806312253a6c1461006e578063206fd5af1461007857806322aacad514610082578063a87d942c1461008c575b600080fd5b6100766100aa565b005b61008061019b565b005b61008a6101fc565b005b61009461025d565b6040518082815260200191505060405180910390f35b600160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff16141561015c576000600160146101000a81548160ff0219169083151502179055507fc8d1e95a715e287f2f929227db854b9c98c3b5e82d21be43dd1cd3da0d94a3e76001604051808215151515815260200191505060405180910390a1610199565b7fc8d1e95a715e287f2f929227db854b9c98c3b5e82d21be43dd1cd3da0d94a3e76000604051808215151515815260200191505060405180910390a15b565b600160149054906101000a900460ff16156101c157600160008082825403925050819055505b7f74b1d21d3925551be58f2c3937d9d7939ef13854117b3c77391391d1ec2c209d6000546040518082815260200191505060405180910390a1565b600160149054906101000a900460ff161561022257600160008082825401925050819055505b7f6269e3482d4669e0adf4e4622035e39c7b92ff4ba4d87291f6016e94f95915e06000546040518082815260200191505060405180910390a1565b6000805490509056fea165627a7a7230582030943cd0362154d8df48571d52a7403c7842ae46c66cf317fb3014e6b11ec60c0029";

var accountAddr = "0x084976Cd86b079215d2e20a3b593AFEB6D049a2A";
var contractAddress = "0xEC8c57384B45e6067A81508bA436e966de894178";
var web3;
var counter;

requirejs(['/static/web3.min.js'], function(util) {
    Web3 = require('/static/web3.min.js');
    web3 = new Web3(new Web3.providers.HttpProvider("http://127.0.0.1:7545"));
    // import Web3 from 'web3';
    // create an instance of web3 using the HTTP provider.
    // NOTE in mist web3 is already available, so check first if it's available before instantiating
    console.log(web3); // {eth: .., shh: ...} // It's here!
    var result = web3.eth.personal.unlockAccount(accountAddr,"d37b03f478ac8d2b7b14987784f9467cc5a7c3812574153300615101165d2982", 600)
                                    .then((response) => {console.log(response);})
                                    .catch((error) => {console.log(error);});

    web3.eth.getBalance(accountAddr).then(console.log);
});

async function getMainAccount() {
  let accounts = await web3.eth.getAccounts();
  return accounts[0];
}

function create_contract() {
	counter = new web3.eth.Contract(abi, '0xde0B295669a9FD93d5F28D9Ec85E40f4cb697BAe')
	counter.deploy({
		data : byteCode
	}).send ({
		from: accountAddr,
		gas: 1500000,
		gasPrice: '300000000'
	}, function(error) { 
		console.log(error)
	}).on('error', function(error) {
		console.log(error)
	}).on('transactionHash', function(transactionHash) {
		console.log(transactionHash)
	}).on('receipt', function(receipt) {
		console.log(receipt.contractAddress)
		counter.options.address = receipt.contractAddress
		
	}).then(function (newContractInstance) {
		console.log(newContractInstance.options.address)
	})
}