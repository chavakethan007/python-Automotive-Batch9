import requests
import json

def get_response():
    url='https://api.github.com'
    response=requests.get(url)

    print('Status Code: ',response.status_code)
    print("headers: ",response.headers)
    print("Data: ",response.json())

if __name__=="__main__":
    get_response()


    