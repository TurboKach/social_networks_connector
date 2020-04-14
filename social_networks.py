import requests
from abc import ABC


class SocialNetwork(ABC):
    """
    Abstract social network class
    """

    def __init__(self, token=None, api_version=None):
        self.token = token
        self.api_version = api_version

    def get_user_profile(self, user_id=None):
        pass

    def get_user_friends(self, user_id=None):
        pass

    def get_user_posts(self, user_id=None):
        pass


class Vk(SocialNetwork):
    """
    VK social network class
    """

    def __init__(self, token=None, api_version='5.103'):
        super().__init__(token, api_version)
        if token is None:
            print('No token provided!')
            raise TypeError
        self.token = token
        self.api_version = api_version

    def get_user_profile(self, user_id=None) -> dict:
        url = 'https://api.vk.com/method/users.get'
        params = {
            'user_ids': user_id,
            'v': self.api_version,
            'access_token': self.token
        }
        try:
            res = requests.get(url, params=params).json()['response'][0]
            return res
        except Exception as e:
            print('Error: ', e)
            return {}

    def get_user_friends(self, user_id=None) -> list:
        if not isinstance(user_id, int) and user_id is not None:
            try:
                user_id = self.get_user_profile(user_id)['id']
            except TypeError:
                print(f'Invalid user id: {user_id}.')
        url = 'https://api.vk.com/method/friends.get'
        params = {
            'user_id': user_id,
            'v': self.api_version,
            'access_token': self.token
        }
        try:
            res = requests.get(url, params=params).json()['response']['items']
            return res
        except Exception as e:
            print('Error: ', e)
            return []

    def get_user_posts(self, user_id=None) -> list:
        if not isinstance(user_id, int) and user_id is not None:
            try:
                user_id = self.get_user_profile(user_id)['id']
            except TypeError:
                print(f'Invalid user id: {user_id}.')
        url = 'https://api.vk.com/method/wall.get'
        params = {
            'owner_id': user_id,
            'v': self.api_version,
            'access_token': self.token
        }
        try:
            res = requests.get(url, params=params).json()['response']['items']
            return res
        except Exception as e:
            print('Error: ', e)
            return []


class Twitter(SocialNetwork):
    """
    Twitter social network class
    """

    def __init__(self, token=None, api_version='5.103'):
        super().__init__(token, api_version)
        if token is None:
            print('No token provided!')
            raise TypeError
        self.token = token
        self.api_version = api_version

