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
    with open('matches.txt' 'w') as file:
        file.write(names, '\n', secret)
    for i in range(len(names)):
        textResults(names[i], secret[i])



def textResults(name, number):
    params = {'src': '19712063040', 'dst': number,
              'text': "You are giving a gift to: " + name}
    response = p.send_message(params)
    with open('results.txt', 'w') as file:
        file.append('\n' + response)
    print(response)


if __name__ == '__main__':
    names = ["andy craig",
             "jack warz",
             "ryan scrogg",
             "ben cox",
             "ian enger",
             "bailey",
             "maddie Jaztak",
             "Owen",
             "nikki l",
             "reece",
             "joey",
             "jonah",
             "Peyton",
             "kylie booth",
             "Ian Stormotn",
             "Ahley peniak",
             "Sailor",
             "will",
             "ethan"
             ]

    numbers = ["15033329523",  # Andy Craig
               "15037060383",  # Jack Warzlec
               "15038990975",  # Ryan Scroggin
               "15038940386",  # Ben Cox
               "15037079976",  # Ian Enger
               "15039892243",  # Bailey
               "15035775843",  # Maddie Jaztak
               "15039275732",  # Owen Grubbe
               "15032706978",  # Nikki L
               "15032770052",  # Reece Barnard
               "15038583945",  # Joey Price
               "18137676950",  # Jonah
               "19712636560",  # Peyton Carl
               "15037993057",  # Kylie Booth
               "15031888054",  # Ian Stormont
               "15034109522",  # Ashley Peniak
               "19712469563",  # Sailor Benitez
               "15035501155",  # Will Oakly
               "15033106561",  # Ethan
               ]

    secretSanta(names, numbers)
