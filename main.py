import random
# import plivo

# auth_id = "MAYJNHN2E3YJA0ZTKYMJ"
# auth_token = "YTA0ZWFjZjM5NTNlOGJkMzllMzYwN2Y3NzI5M2Zi"
# p = plivo.RestAPI(auth_id, auth_token)

shuffledNames = []
names = ["andy", "jack", "christian", "ben", "ian", "bailey"]
numbers =  ["5033329523", "5037060383", "5034844734", "5038940386", "5037079976", "5039892243"]

counter = 0


def rand():
    tmpNames = list(names)
    # random.shuffle(tmpNames)
    for index, n in enumerate(tmpNames):
        randomNum = random.randrange(0, len(tmpNames))
        print(randomNum)
        shuffledNames.append(tmpNames[randomNum])

    return shuffledNames


def main():
    tmpNames = rand()
    while True:
        for idx, name in enumerate(names):
            if name == tmpNames[idx]:
                counter = 0
                rand()
                print('reseting...')
            else:
                counter += 1
                print(counter)
                if counter == 5:
                    break
    print(l)


def text(phoneNumber, receiver):
    pass
    # params = {'src': '9712063040', 'dst': phoneNumber, 'text': receiver}
    # response = p.send_message(params)
    # print(response)


if __name__ == '__main__':
    main()
