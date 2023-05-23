#!/usr/bin/python3
"""[Export data in json format]
"""

if __name__ == "__main__":
    import json
    import requests
    import sys
    url_user = "https://jsonplaceholder.typicode.com/users"
    employee = requests.get(url_user).json()
    todo_dict = {}
    # file name
    file_name = "todo_all_employees.json"
    # list for list of dictonaries
    for user_id in employee:
        url_to = "https://jsonplaceholder.typicode.com/users/{}/todos".format(
            user_id.get('id'))
        all_tasks = requests.get(url_to).json()

        todo_tasks = []
        with open(file_name, 'w') as f:
            for task in all_tasks:
                task_dict = {}
                # completed, and username
                task_dict['task'] = task.get('title')
                task_dict['completed'] = task.get('completed')
                task_dict['username'] = user_id.get('username')
                # appending to the list of dictonaries
                todo_tasks.append(task_dict)
                # setting the id equal to the dictonary
            todo_dict[user_id.get('id')] = todo_tasks
            json.dump(todo_dict, f, indent=2)
