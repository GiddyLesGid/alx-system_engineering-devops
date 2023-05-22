#!/usr/bin/python3
"""
Write a Python script that, using this REST API,
for a given employee ID,
returns information about his/her TODO list progress
"""

if __name__ == "__main__":
    import requests
    import sys

    eid = sys.argv[1]

    user = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(eid))
    tasks = requests.get("https://jsonplaceholder.typicode.com/todos/").json()
    total = 0
    done = 0
    completed = []
    for task in tasks:
        userId = task.get('userId')
        if userId == int(eid):
            total = total + 1
            if task.get('completed') is True:
                done = done + 1
                completed.append(task.get('title'))
    print("Employee {} is done with tasks({}/{}):".format(
        user.json().get('name'), done, total
    ))
    for task in completed:
        print("\t {}".format(task))
