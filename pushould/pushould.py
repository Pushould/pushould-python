import json
import requests


class Pushould(object):
    def __init__(self, url='', server_token='', email='', password=''):
        if url == '':
            raise ValueError('url is required')
        if server_token == '':
            raise ValueError('server_token is required')
        if email == '':
            raise ValueError('email is required')
        if password == '':
            raise ValueError('password is required')
        self.url = url
        self.headers = {'Accept': 'application/json'}
        self.server_token = server_token
        self.email = email
        self.password = password

    def trigger(self, room='', event='', data={}):
        if room == '':
            raise ValueError('room is required')
        if event == '':
            raise ValueError('event is required')
        account_info = {'email': self.email, 'password': self.password}
        data = {'room': room,
                'event': event,
                'token': self.server_token,
                'custom': data}
        payload = {'account': json.dumps(account_info),
                   'data': json.dumps(data)}
        requests.get(self.url, params=payload, headers=self.headers)
