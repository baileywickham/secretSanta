import random
# import plivo

# auth_id = "MAYJNHN2E3YJA0ZTKYMJ"
# auth_token = "YTA0ZWFjZjM5NTNlOGJkMzllMzYwN2Y3NzI5M2Zi"
# p = plivo.RestAPI(auth_id, auth_token)

switch = []
names = ["andy", "jack", "christian", "ben", "ian", "bailey"]
numbers =  ["5033329523", "5037060383", "5034844734", "5038940386", "5037079976", "5039892243"]


def rand():
    tmpNames = list(names)
    random.shuffle(tmpNames)
    return tmpNames


def main():
    tmpNames = rand()

    for idx, name in enumerate(names):
        if name == tmpNames[idx]:
            if idx != 0 and tmpNames[idx] != 
    print(switch)
    print(l)


def text(phoneNumber, receiver):
    pass
    # params = {'src': '9712063040', 'dst': phoneNumber, 'text': receiver}
    # response = p.send_message(params)
    # print(response)


if __name__ == '__main__':
    main()
