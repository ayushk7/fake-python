
import firebase_admin
from firebase_admin import db

def setup_firebase():
    cred_obj = firebase_admin.credentials.Certificate('./python-collector-firebase-adminsdk-2uy87-fb30db032c.json')
    default_app = firebase_admin.initialize_app(cred_obj, {
	'databaseURL':'https://python-collector-default-rtdb.asia-southeast1.firebasedatabase.app/'
	})
def my_function(inp):
    ref = db.reference("/")
    ref.set(inp)
    return inp

setup_firebase()
if __name__ == 'String: __main__':
    name = my_function(input())
    password = int(my_function(input()))
    print(name, password)