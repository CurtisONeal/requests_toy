# notes on the venv and start up
# mac:
#     python3 -m venv env
#     source ./env/bin/activate
    
# Windows: python -m venv env
# .\env\Scripts\activate

# Both:
#     pip install requests
#     pip freeze > requirements.txt

# reminders
# git init 
# git add .  
# git commit -m 'Initial commit'
# git branch -M main
# git remote add origin https://github.com/CurtisONeal/<name>.git
# git push -u origin main

# reminder for second commit.... if you just tried git push
# git push --set-upstream origin main
# starting up the app reminder to test for typos:
# python3 app.py # to see the db created

# https://teamtreehouse.com/library/using-the-requests-library/using-the-requests-library
# httpbin.org
import requests
from requests.auth import HTTPBasicAuth, HTTPDigestAuth
import json

r = requests.get('https://api.github.com/events')

print('Types of requests class data coptions are:\n')

print(f' status code= {r.status_code}')
print()
print(f' ok? {r.ok}')
print()
print(f' headers {r.headers} are a dictionary')
print()
print(f' headers-keys {r.headers.keys} ')
print()
print(f' The URL was {r.url}')
print()
print('************** RESPONSE AS TON OF TEXT **************')
# print(f' text {r.text}')
print()
print('\n************** ACCESSING JSON RESPONSE **************')
timeline = r.json() 

# We could import json library and convert this from json to 
# a python list of dictionaries but requests gave us a mthod for it.
print(timeline[0]['id'])

content = r.content # basically the same thing...

print('\n************** ACCESSING CONTENT **************')
print('''Content comes across as bytes not text
      so you can take those bytes and turn them into your pdf or SCG image or whatever
      working with images in python is in another workshop''')
# print(content )

print('\n************** POST DATA TO SERVER CONTENT **************')
#payloads are usually dictionaries for posting

# payload = {'key1': 'value1', 'key2': 'value2'}
payload = {'content': 'I really like requests', 'user': 152}
#r2 = requests.post('https://httpbin.org/post', data={'key': 'value'})
r2 = requests.post('https://httpbin.org/post', params = payload)
print( f'The post url sent with the payload looks like {r2.url}.')
print()
print(f'The headers of the r object in response to the post are {r2.headers}.')
print() #Spacer

print( f'The attributes of the r object are {dir(r2)} .' )
# https://www.programiz.com/python-programming/methods/built-in/dir
#   dir() method returns the list of valid attributes of the passed object.
#print( r2.text) # from the post... we have these args...
print() #Spacer
#easier to see with r.json
print( f' R2 Json repsonse is {r2.json()}.')
print() #Spacer

print('\n************** DELETE DATA TO SERVER CONTENT **************')
# Sometimes you send data to the API where your KEY represents a list... not the value
# This is a bit tricky so points it out
payload3 = {'posts[]': [123, 456]}
r3 = requests.delete('https://httpbin.org/delete', params = payload3)

print( f"The r3 delete response with our args is {r3.json()['args'] } ." ) # note this is a list square braket?
print() #Spacer

#Sometimes your endpoint, has moved.... 
print('\n************** REDIRECT CONTENT **************')

payload4 = {'posts[]': [123, 456]}
r4 = requests.get('http://httpbin.org/redirect/3')
print( r4.status_code)

print(r4.headers.keys)
print(r4.is_redirect)
print(r4.history)
print(f'In theory this should be three responses from three steps. Video 8:28. With status 200 at the end. ')

r4 = requests.get('http://httpbin.org/redirect/3', allow_redirects=False)
print( r4.status_code)
print(r4.is_redirect)
print(r4.history)

# other API operations (more than CRUD)
# r3 = requests.get('https://httpbin.org/put', data={'key': 'value'})
# r3 = requests.put('https://httpbin.org/put', data={'key': 'value'})
# r4 = requests.delete('https://httpbin.org/delete')
# r5 = requests.head('https://httpbin.org/get')
# r6 = requests.options('https://httpbin.org/get')
# payload2 = {'key1': 'value1', 'key2': 'value2'}
# payload2 = {'key1': 'value1', 'key2': ['value2', 'value3']}
# payload3 = {'posts[]': [ 123, 456 ]}
# r7 = requests.get('https://httpbin.org/get', params=payload2)


print('\n************** Basic Authentication CONTENT **************')
# APIs generally do authentication through public and private keys.
#  webpage may be behind http basic or http digest authentication. Which are similar.
# Basic sends your password in plaintext, and http digest hashes it beffore it sends it out.


r6 = requests.get('http://httpbin.org/basic-auth/user/password', auth=HTTPBasicAuth('user', 'password'))
print(r6.status_code)

print(f'Purposful failure example')
r6 = requests.get('http://httpbin.org/basic-auth/user/password', auth=HTTPBasicAuth('user', 'password2'))
print(r6.status_code)
printf('401 means forbidden.')

print('\n************** Digest Authentication CONTENT **************')
# APIs generally do authentication through public and private keys.
#  webpage may be behind http basic or http digest authentication. Which are similar.
# Basic sends your password in plaintext, and http digest hashes it beffore it sends it out.


r6 = requests.get('http://httpbin.org/digest-auth/auth/user/password', auth=HTTPDigestAuth('user', 'password'))
print(r6.status_code)

print(f'Purposful failure example')
r6 = requests.get('http://httpbin.org/digest-auth/auth/user/password', auth=HTTPDigestAuth('user', 'password2'))
print(r6.status_code)
print(f'401 means forbidden.')

print('Request has support for authentication through OAuth there are packages for Kerberos, NTLM and others.')