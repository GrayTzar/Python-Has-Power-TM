users_by_email = {}

users_by_email['geralt@rivia.com'] = {
    'name': 'Geralt',
    'age': 64,
    'city': 'Rivia'
}

users_by_email['rincewind@ank-mor.dw'] = {
    'name': 'Rincewind',
    'age': 28,
    'city': 'Ankh-Morpork'
}

users_by_email['blade.runner2@dys.topia'] = {
    'name': 'Joe',
    'age': 27,
    'city': 'Los Angeles'
}

for person in users_by_email:
    print('%s is %s and he lives in %s.' % (users_by_email[person]['name'], str(users_by_email[person]['age']), users_by_email[person]['city']))

name = 'Mannoroth'
if name == 'Mannoroth':
    print('yes')
else:
    print('no')

for user in users_by_email:
    print(users_by_email[user]['name'])
