import pymongo
from passlib.hash import pbkdf2_sha256
import os

uri = os.environ.get('mongo_uri')
client = pymongo.MongoClient(uri)
db = client.orama
usersCollection = db.users

import utils.logger as logger
from models.user import User

def createUser(user):
    data = {
        'email':user.email,
        'passwordHash':pbkdf2_sha256.hash(user.password),
        'faceHash':user.faceHash
    }

    return str(usersCollection.insert_one(data).inserted_id)

def updateUser(user):
    data = {
        'email':user.email,
        'passwordHash':pbkdf2_sha256.hash(user.password),
        'faceHash':user.faceHash
    }

    usersCollection.update_one({
        'email': user.email
        }, {
        '$set': data
    }, upsert=False)

def authenticateUser(user):
    userData = usersCollection.find_one({'email':user.email})
    try:
        userData['_id'] = str(userData['_id'])
    except:
        return False,userData
    return pbkdf2_sha256.verify(user.password, userData.get('passwordHash','')),userData

if __name__ == '__main__':

    print(createUser(User(email='sdfds@gmail.com',password='test',faceHash='123')))