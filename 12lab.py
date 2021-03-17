#!/usr/bin/env python3



users = [
    { 'admin': True, 'active': True, 'name': 'Kevin' },
    { 'admin': True, 'active': False, 'name': 'Elisabeth' },
    { 'admin': False, 'active': True, 'name': 'Josh' },
    { 'admin': False, 'active': False, 'name': 'Kim' },
]

line = 1

for user in users:
    prefix = f"{line} "

    if user['admin'] and user['active']:
        prefix += "ACTIVE - (ADMIN) "
    elif user['admin']:
        prefix += "(ADMIN) "
    elif user['active']:
        prefix += "ACTIVE - "

    print(prefix + user['name'])
    line += 1
    




#user = { 'admin': True, 'active': True, 'name': 'Kevin' }

# users = {
#     'id1':{
#         'admin' : True,
#         'active' : True,
#         'name' : 'Kevin'
#     },
#     'id2':{
#         'admin' : True,
#         'active' : False,
#         'name' : 'Quyet'
#     },
#     'id3':{
#         'admin' : False,
#         'active' : True,
#         'name' : 'Ngo'
#     }
# }
# prefix = ""

# for id in users.keys():
# #    print(users[id]['admin'])
#     if users[id]['admin'] and users[id]['active']:
#         prefix = " ACTIVE - ADMIN "
#     elif users[id]['admin']:
#         prefix = " ADMIN - "
#     elif users[id]['active']:
#         prefix = " ACTIVE - "

#     print(id+ prefix + users[id]['name'])
    
