import plivo

auth_id = "MAYJNHN2E3YJA0ZTKYMJ"
auth_token = "YTA0ZWFjZjM5NTNlOGJkMzllMzYwN2Y3NzI5M2Zi"
p = plivo.RestAPI(auth_id, auth_token)

params = {
    'src': '19712063040',
    'dst': '15033329523',
    'text': u"hey andy its baileys computer"
}
response = p.send_message(params)
print(response)
