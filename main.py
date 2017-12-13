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
    with open('matches.txt', 'a') as file:
        file.write(str(names) + '\n' + str(secret))
    for i in range(len(names)):
        textResults(names[i], secret[i])


def textResults(name, number):
    params = {'src': '19712063040', 'dst': number,
              'text': "this is baileys robot. You are giving a gift to: " + name}
    response = p.send_message(params)
    print(response)


if __name__ == '__main__':
    names = ["andy craig",
             "jack warz",
             "ryan scrogg",
             "ben cox",
             "ian enger",
             "bailey",
             "maddie Jaztak",
             "Anthony",
             "maddie langan",
             "reece",
             "joey",
             "jonah",
             "Peyton",
             "kylie booth",
             "Ian Stormotn",
             "Ahley peniak",
             "Sailor",
             "Gracie",
             "ethan",
             "tommy",
             "josh",
             "jack murph",
             "Will oakly",
             "Nikki l",
             "Jacob Taylor",
             "Gaven",
             "Owen",
             "Christian Goyer",
             "Kolleen",
             "Miguel "
             ]

    numbers = ["15033329523",  # Andy Craig
               "15037060383",  # Jack Warzlec
               "15038990975",  # Ryan Scroggin
               "15038940386",  # Ben Cox
               "15037079976",  # Ian Enger
               "15039892243",  # Bailey
               "15035775843",  # Maddie Jaztak
               "19712698404",  # Anothy
               "15035399620",  # Maddy langan
               "15032770052",  # Reece Barnard
               "15038583945",  # Joey Price
               "18137676950",  # Jonah
               "19712636560",  # Peyton Carl
               "15037993057",  # Kylie Booth
               "15033888054",  # Ian Stormont
               "15034109522",  # Ashley Peniak
               "19712469563",  # Sailor Benitez
               "19712811638",  # Gracie
               "15033106561",  # Ethan
               "19712698003",  # Tommy
               "15033411872",  # josh
               "15038801915",  # Jack murph
               "15035501155",  # Will oakly
               "15032706978",  # Nikki L
               "15039289575",  # Jacob Taylor
               "15035475215",  # Gaven
               "15039275732",  # Owen
               "15035500562",  # Christian Goyer
               "15037092754",  # Kolleen
               "15032708131"   # Miguel
               ]

    secretSanta(names, numbers)
