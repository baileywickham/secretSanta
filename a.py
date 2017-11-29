import plivo

auth_id = "MAYJNHN2E3YJA0ZTKYMJ"
auth_token = "YTA0ZWFjZjM5NTNlOGJkMzllMzYwN2Y3NzI5M2Zi"
p = plivo.RestAPI(auth_id, auth_token)

params = {
    'src': '9712063040', 
    'dst' : '5039892243', 
    'text' : u"hey andy its baileys computer"
}
response = p.send_message(params)
pram = {'message_uuid' : "6c91b2c4-d544-11e7-9bde-024427e23b8a"}
print(p.get_message(pram))
print(response)