import requests

def get_username(username):
    url=f'https://api.github.com/users/{username}'
    response=requests.get(url)

    if response.status_code==200:
        user_data=response.json()
        print('Username: ',user_data['login'])
        print('public Repos: ',user_data['public_repos'])
    else:
        print("Failed to fetch data")

get_username("chavakethan007")