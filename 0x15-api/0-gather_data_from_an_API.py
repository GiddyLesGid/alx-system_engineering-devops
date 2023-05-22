#!/usr/bin/python3

import sys
from urllib import request
import json

if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com/"
    employee_id = sys.argv[1]
    
    # Retrieve user information
    user_url = base_url + "users/{}".format(employee_id)
    user_response = request.urlopen(user_url)
    user_data = json.loads(user_response.read().decode())

    # Retrieve TODO list information
    todos_url = base_url + "todos?userId={}".format(employee_id)
    todos_response = request.urlopen(todos_url)
    todos_data = json.loads(todos_response.read().decode())
    
    completed = [t.get("title") for t in todos_data if t.get("completed") is True]
    total_tasks = len(todos_data)
    
    print("Employee {} is done with tasks({}/{}):".format(
        user_data.get("name"), len(completed), total_tasks))
    
    for task_title in completed:
        print("\t{}".format(task_title))
