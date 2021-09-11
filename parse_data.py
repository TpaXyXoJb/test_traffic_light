import requests
import json


def get_users_data():
    pk = 0

    new_list = []
    users_url = 'http://jsonplaceholder.typicode.com/users'
    users_response = requests.get(users_url)

    users_data = users_response.json()

    with open('users_data.json', 'w') as json_data:
        d = users_data
        for item in d:
            pk += 1

            item = {"model": "users_posts.User", "pk": pk, "fields": item}

            new_list.append(item)

            json_data.close()

    list_to_json_file(new_list, 'users_data')


def get_posts_data():
    pk = 0
    new_list = []
    posts_url = 'http://jsonplaceholder.typicode.com/posts'
    posts_response = requests.get(posts_url)

    posts_data = posts_response.json()

    with open('posts_data.json', 'w') as json_data:
        d = posts_data
        for item in d:
            pk += 1
            item = {"model": "users_posts.Post", "pk": pk, "fields": item}

            new_list.append(item)
            json_data.close()

    list_to_json_file(new_list, 'posts_data')


def list_to_json_file(list_of_dicts, file_name):
    with open(file_name + '.json', 'w') as file:
        json.dump(list_of_dicts, file)


get_users_data()
get_posts_data()
