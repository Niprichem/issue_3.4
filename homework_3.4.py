import requests


def main():
    VERSION = '5,69'
    TOKEN = 'c6b72427d3176fd00c057e9c1bf160b17b080771634be52fd06250d6da74c656619122f212ae5cd17a722'

    params = {
        'access_token': TOKEN,
        'v': VERSION
    }

    response = requests.get('https://api.vk.com/method/friends.get', params).json()
    my_friends = set(response['response']['items'])
    all_friends_friends = set()
    for friend_id in my_friends:
        params = {
            'user_id': friend_id,
            'v': VERSION
        }
        response = requests.get('https://api.vk.com/method/friends.get', params).json()
        if response.get('error'):
            continue
        all_friends_friends = all_friends_friends | set(response['response']['items'])
    friend_intersection = my_friends & all_friends_friends
    print(friend_intersection)


if __name__ == '__main__':
    main()
