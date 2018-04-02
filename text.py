import plivo
auth_id = "MAYJNHN2E3YJA0ZTKYMJ"
auth_token = "YTA0ZWFjZjM5NTNlOGJkMzllMzYwN2Y3NzI5M2Zi"
p = plivo.RestAPI(auth_id, auth_token)

numbers = ["15038990975",  # Ryan Scroggin
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
for n in numbers:
    params = {'src': '19712063040', 'dst': n,
              'text': 'Meet at owens at 7:30 for the secret santa'}
    response = p.send_message(params)
    print(response)
