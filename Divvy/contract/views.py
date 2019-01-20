from django.shortcuts import render, HttpResponse
from web3 import Web3, HTTPProvider, IPCProvider, WebsocketProvider

def index(request):
    web3 = Web3(HTTPProvider('http://127.0.0.1:7545'))
    print(web3.eth.getBlock(0))
    return render(request, 'contract/user.html')