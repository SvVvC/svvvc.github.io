__author__ = 'Sebastien Vacher-Coponat'
__version__ = '0.1'
__date__ = '14/05/18'
import datetime as date
import time

from __main__ import *

block = {'blockchain': [{'id': 0,
                          'content': "genesis",
                          'timestamp': str(date.datetime.utcnow()),
                          'hash precedent': 'None'}
                        ]
         }


class New_Block(object):
    Block_number = 0  # Number of the genesis block

    def __init__(self):  # Creating the new block: Content, hash, proof_of_work, Block_number

        New_Block.Block_number += 1  # When the block is created, it adds on top of the block chain
        self.content = []
        self.proof_of_work = ''
        self.id = New_Block.Block_number
        self.hash_block_precedent = block['blockchain'][self.id - 1]['hash precedent'] + str(self.id)
        self.hash_current = hash(str({'id': self.id, 'content': self.content, 'timestamp': str(date.datetime.utcnow()),'hash precedent': self.hash_block_precedent}))

    def block_number(self):
        print("This block's number is :", self.id)
        return self.id

    def content(self, content):
        self.block_content = content

    def proof_of_work_testing(self):  # Testing if the proof of work matches with the hashing algorithm
        try:
            print(self)
            if (True):
                print("The proposed proof of work :", self.proof_of_work, " is correct", )
            else:
                print("The proposed proof of work", self.proof_of_work, ' is not correct')

        except Exception:
            print("The proposed proof of work", self.proof_of_work, ' is not a valid expression')

    def print(self):  # Print all the block's content
        attrs = vars(self)
        return ', '.join("%s: %s" % item for item in attrs.items())

    def hasheur_block(self):
        self.hash_current = hash(str({'id': self.id, 'content': self.content, 'timestamp': str(date.datetime.utcnow()),'hash precedent': self.hash_block_precedent}))

        return self.hash_current

    def json_format(self):
        return {'id': self.id,
                 'content': self.content,
                 'timestamp': str(date.datetime.utcnow()),
                 'hash precedent': self.hash_block_precedent,
                 'current hash': self.hash_current,
                 }


for k in range(1, 10):
    block['blockchain'].append(New_Block().json_format())
    time.sleep(0.1)  # simulating pow for timestamp

#ajouter donnes dans le bloc 2

def Add_data(id, transaction):

        block['blockchain'][id]['content'].append(transaction)

transaction = {'first_name': 'Bobby', 'last_name': 'Smith'}
Add_data(2, transaction)