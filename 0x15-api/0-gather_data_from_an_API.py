#!/usr/bin/python3

"""
Returns TODO list progress for a given employee ID and saves it to a file.
"""

import sys
import requests
import json

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("Usage: python script.py <employee_id>")

    employee_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com/"

    # Retrieve user information
    user_response = requests.get(base_url + "users/{}".format(employee_id))
    user_data = user_response.json()

    # Retrieve TODO list information
    todos_response = requests.get(base_url + "todos", params={"userId": employee_id})
    todos_data = todos_response.json()

    completed = [task.get("title") for task in todos_data if task.get("completed")]
    total_tasks = len(todos_data)

    print("Employee {} is done with tasks({}/{}):".format(user_data.get("name"), len(completed), total_tasks))
    for task_title in completed:
        print("\t{}".format(task_title))
    
    # Save TODO list to a file
    filename = "todos_employee_{}.json".format(employee_id)
    with open(filename, "w") as file:
        json.dump(todos_data, file)
    print("TODO list saved to", filename)
