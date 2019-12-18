import requests

headers = {}
headers['Authorization'] = 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTc2NjUyMjc4LCJqdGkiOiJlMWE5OWIyNDIyNDM0OWQ1YTY5YTRlOTE3MjY1NTc5MyIsInVzZXJfaWQiOjF9.kA6uDa1BzgpSQHqMdVMyhjue5N4zbxKSflWtn6DALww'

r = requests.get('http://127.0.0.1:8000/',headers=headers)

print(r.text)