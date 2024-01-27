#!/usr/bin/python3
"""sends a POST request to the giving url with the letter as a parameter"""


if __name__ == '__main__':
    import requests
    from sys import argv

    URL = 'http://0.0.0.0:5000/search_user'
    if len(argv) >= 2:
        data = {'q': argv[1]}
    else:
        data = ""

    response = requests.post(URL, data)
    cont_type = response.headers['content-type']

    if cont_type == 'application/json':
        r = response.json()
        id = r.get('id')
        name = r.get('name')
        if (r != {} and id is not None and name is not None):
            print("[{}] {}".format(id, name))
        else:
            print('No result')
    else:
        print('Not a valid JSON')
