import os
from random import choice, randint
from time import sleep

from pyrogram import Client
from pyrogram.api import functions
from requests import get

import config

app = Client(
    config.session_name,
    config.api_id,
    config.api_hash
)

sep = os.path
scriptFold = os.getcwd()
timeout = config.timeout

peoplesFold = sep.join(scriptFold, 'peoples')
dictonariesFold = sep.join(scriptFold, 'dictonaries')

if not os.path.exists(peoplesFold): os.makedirs(peoplesFold)
if not os.path.exists(dictonariesFold): os.makedirs(dictonariesFold)

forenameFile = sep.join(dictonariesFold, 'forename.txt')
surnameFile = sep.join(dictonariesFold, 'surname.txt')

if not os.path.exists(forenameFile):
    with open(forenameFile, 'w') as f:
        f.write('\n'.join(config.forenamesList))

if not os.path.exists(surnameFile):
    with open(surnameFile, 'w') as f:
        f.write('\n'.join(config.surnamesList))


def createPeople():
    with open(forenameFile, 'r') as f:
        forename = choice(list(f)).strip()
    with open(surnameFile, 'r') as f:
        surname = choice(list(f)).strip()
    return {'forename': forename,
            'surname': surname,
            'photo': getPhoto()}


def saveImg(folder, imgData):
    path = sep.join(peoplesFold, str(randint(1000000, 9999999)) + '.png')
    if not os.path.exists(folder): os.makedirs(folder)
    with open(path, 'wb') as img:
        img.write(imgData)
    return path


def getPhoto():
    r = get('https://thispersondoesnotexist.com/image',
            headers={'User-agent': 'Googlebot-Image/1.0'})
    return saveImg(peoplesFold, r.content)


def updateProfile():
    people = createPeople()
    with app:
        app.set_profile_photo(people['photo'])
        app.send(
            functions.account.UpdateProfile(
                first_name=people['forename'],
                last_name=people['surname']
            )
        )
        for i in list(app.iter_profile_photos(app.get_me()['id']))[1:]:
            app.delete_profile_photos(i['file_id'])


while True:
    updateProfile()
    sleep(timeout)
