"""
Client to the VK API, which will consider the age distribution of friends
for the specified user. That is, the username or user_id of the user is input,
the output is a list of pairs (<age>, <number of friends with this age>),
sorted in descending order by the second key (number of friends) and in ascending
order by the first key (age). For example:
[(26, 8), (21, 6), (22, 6), (40, 2), (19, 1), (20, 1)]
"""

import requests
from collections import *
import json


def calc_age(uid):

    """ Function for getting friends list of the user with user id in sorted order """

    uid = uid
    access_token = 'First paste here vk access_token to API'  # first do here and go bottom
    # get user id by username or user_id:
    get_id = requests.get(f'https://api.vk.com/method/users.get?v=5.87&access_token={access_token}&user_ids={uid}')
    # get a list of user`s friends
    get_friends = requests.get(f'https://api.vk.com/method/friends.get?v=5.87&access_token={access_token}&user_id={uid}&fields=bdate')
    age = []
    data = json.loads(get_friends.text)  # loads json
    friends = data['response']['items']
    for friend in friends:
        try:
            age.append((2018 - int(friend['bdate'].split('.')[2])))
        except KeyError:
            continue
        except IndexError:
            continue
    return friends_sort(age)  # calls sorting function


def friends_sort(age):

    """ Sorting function """

    age = dict(Counter(age))
    keys = list(Counter.keys(age))
    values = list(Counter.values(age))
    age = list(zip(keys[:len(keys)], values[:len(values)]))

    age = sorted(age, key=lambda tup: (-tup[1], tup[0]))
    return age


# If you want import as a module, comment this block
if __name__ == '__main__':
    res = calc_age(uid='Paste VK uid of target user here as an int')  # second do here than start script
    print(res)
