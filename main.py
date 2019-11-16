import random
import sys
import plivo

with open("secret", 'r') as f:
    auth_id = f.readline().strip('\n')
    auth_token = f.readline().strip('\n')

plv = plivo.RestClient(auth_id, auth_token)


class Person:
    def __init__(self, name, number):
        self.name = name
        self.number = number


def printResults(peoples):
    outstr = ''
    random.shuffle(peoples)
    f = open(f'output/{file}.output', 'w')
    for num in range(len(peoples)):
        outstr += peoples[num % len(peoples)].name + ' >> ' + \
            peoples[(num+1) % len(peoples)].name + '\n'
        textResults(peoples[(num+1) % len(peoples)].name,
                    peoples[num % len(peoples)].number)
    f.write(outstr)


def textResults(name, number):
    textm = f'this is baileys robot, you are giving a gift to {name}'
    response = plv.messages.create(src='19712063040', dst=number, text=textm)
    print(response)


def reads():
    peoples = []
    with open(f'{file}') as f:
        for line in f.readlines():
            line = line.split(",")
            peoples.append(Person(line[0], line[1].strip('\n')))
    printResults(peoples)


file = str(sys.argv[1])
reads()
