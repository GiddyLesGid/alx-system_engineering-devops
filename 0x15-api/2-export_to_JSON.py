#!/usr/bin/python3
"""[Export data in json format]
"""

if __name__ == "__main__":
    import json
    import requests
    import sys
    url_user = "https://jsonplaceholder.typicode.com/users/{}".format(
        sys.argv[1])
    url_todo = "https://jsonplaceholder.typicode.com/users/{}/todos".format(
        sys.argv[1])

    employee = requests.get(url_user).json()
    emplyee_username = employee.get('username')

    # This loops the the tasks and check to
    all_tasks = requests.get(url_todo).json()
    # Create dictonary for inner level of dicts
    todo_dict = {}
    # file name
    file_name = "{}.json".format(sys.argv[1])
    # list for list of dictonaries
    todo_tasks = []
    with open(file_name, 'w') as f:
        for task in all_tasks:
            task_dict = {}
            # get each individual items doe the inner dicts which include task
            # completed, and username
            task_dict['task'] = task.get('title')
            task_dict['completed'] = task.get('completed')
            task_dict['username'] = emplyee_username
            # appending to the list of dictonaries
            todo_tasks.append(task_dict)
            # setting the id equal to the dictonary
        todo_dict[sys.argv[1]] = todo_tasks
        json.dump(todo_dict, f, indent=2)
