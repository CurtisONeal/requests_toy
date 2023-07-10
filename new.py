
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
import json

r = requests.get('http://httpbin.org/get')
print(f' status code= {r.status_code}')
print(f' ok? {r.ok}')
print(f' headers {r.headers} are a dictionary')
print(f' headers-keys {r.headers.keys} ')
print('ABOVE WAS KEYS')
print(f' The URL was {r.url}')


print( f" headers['Content-Length']  ={ r.headers['Content-Length'] } ")
print()


# from  https://requests.readthedocs.io/en/latest/user/quickstart/
r2 = requests.post('https://httpbin.org/post', data={'key': 'value'})
print(f' status code= {r2.status_code}')
print(f' ok? {r2.ok}')
print(f' headers {r2.headers} are a dictionary')
print(f' headers-keys {r2.headers.keys} ')
print('ABOVE WAS KEYS')

r3 = requests.put('https://httpbin.org/put', data={'key': 'value'})
r4 = requests.delete('https://httpbin.org/delete')
r5 = requests.head('https://httpbin.org/get')
r6 = requests.options('https://httpbin.org/get')
payload = {'key1': 'value1', 'key2': 'value2'}
r7 = requests.get('https://httpbin.org/get', params=payload)
#Note that any dictionary key whose value is None will not be added to the URL’s query string.
print(r.url)

payload = {'key1': 'value1', 'key2': ['value2', 'value3']}

r8 = requests.get('https://httpbin.org/get', params=payload)
print(r.url)
#https://httpbin.org/get?key1=value1&key2=value2&key2=value3

print('******** SECOND API **********' )
#most of the API responses are JSON and we can't get interesting json from httpbin.
r = requests.get('https://api.github.com/events')
print(f' status code= {r.status_code}')
print(f' text {r.text}')
print()
print(f' headers {r.headers} are a dictionary')
print(f' headers-keys {r.headers.keys} ')
# print( f" headers['Content-Length']  ={ r.headers['Content-Length'] } ")
print()
print(' ************** THIS IS THE JSON RESPONSE ************** ')
print( r.json() )
timeline = r.json()
print(timeline)
print()
print('new')
#Requests will automatically decode content from the server. Most unicode 
# charsets are seamlessly decoded.

# url_n = 'http://httpbin.org/get'
# response = requests.get(url_n)
# if response.status_code == 200:
#     rp = response.json()
#     print(rp)
# else:
#     print("Error from server: " + str(response.content))

# print('Try again')
# print( json.loads(r) )
