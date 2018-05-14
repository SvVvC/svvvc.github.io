import json
from . import blockchain_file as blockchain
from django.shortcuts import render

# We create the genesis block
"""
# Idea: could it be possible to make a blockchdain where no token is created because relies on time >? Ie one block every x sec ? 
"""
# how to print the blockchain in JSON format
blockchain.block['blockchain'].append(blockchain.New_Block().json_format())

chaine = print('chaine',json.dumps(blockchain.block, indent=2))



def homepage(request):
    return render(request, 'home.html')


def count(request):
    i = request.GET['fulltext']
    try :
        int(i)
        if(int(i)>len(blockchain.block['blockchain'])-1):
            i=len(blockchain.block['blockchain'])-1
    except :
        print('Mauvais type')
        i= len(blockchain.block['blockchain'])-1

    return render(request, 'count.html', {'blockchain': blockchain.block['blockchain'][int(i)], 'i': [int(i)]})
