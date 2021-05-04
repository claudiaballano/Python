# Basic data structures & Functions

blockchain = []


def get_last_blockhain_value():
    return blockchain[-1]


def add_value(transaction_amount, last_transaction=[1]):
    blockchain.append([last_transaction, transaction_amount])


def get_user_input():
    return float(input('Your transaction amount please: '))


tx_amount = get_user_input()
add_value(tx_amount)

tx_amount = get_user_input()
add_value(last_transaction=get_last_blockhain_value(),
          transaction_amount=tx_amount)

tx_amount = get_user_input()
add_value(tx_amount, get_last_blockhain_value())


print(blockchain)


# Keyword Arguments -- First difference with JS

def sum(a, b):
    return a + b


print(sum('Hola', 'Que tal'))
print(sum(b='Que tal', a='Hola'))

# Global variables

name = 'Claudia'


def new_name():
    global name
    name = input('My new name is: ')


new_name()
print(name)
