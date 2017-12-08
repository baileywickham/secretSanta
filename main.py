import random
import plivo

auth_id = "MAYJNHN2E3YJA0ZTKYMJ"
auth_token = "YTA0ZWFjZjM5NTNlOGJkMzllMzYwN2Y3NzI5M2Zi"
p = plivo.RestAPI(auth_id, auth_token)


def secretSanta(names, secret):
    random.shuffle(names)
    secret.append(secret.pop(0))
    printResults(names, secret)


# print the results
def printResults(names, secret):
    for i in range(len(names)):
        print("%10s == is buying a present for ==> %s" % (names[i], secret[i]))
        textResults(names[i], secret[i])


def textResults(name, number):
    params = {'src': '19712063040', 'dst': number, 'text': name}
    response = p.send_message(params)
    print(response)
    if str(response[0]) != 202:
        print("something fucked up")


if __name__ == '__main__':
    names = ["andy", "jack", "christian", "ben", "ian", "bailey"]
    numbers =  ["15033329523", "15037060383", "15034844734", "15038940386", "15037079976", "15039892243"]
    secretSanta(names, numbers)
