#!/usr/bin/python3
"""
Returns to-do list information for a given employee ID.
"""
import requests
import sys

def fetch_todo_list(employee_id):
    url = "https://jsonplaceholder.typicode.com/"

    # Fetch user information
    user_response = requests.get(url + "users/{}".format(employee_id))
    if user_response.status_code != 200:
        print("Failed to fetch user information")
        return

    user = user_response.json()

    # Fetch TODO list
    todos_response = requests.get(url + "todos", params={"userId": employee_id})
    if todos_response.status_code != 200:
        print("Failed to fetch TODO list")
        return

    todos = todos_response.json()

    # Count completed tasks
    completed_tasks = [task for task in todos if task["completed"]]
    completed_count = len(completed_tasks)

    # Display output
    print("Employee {} is done with tasks({}/{}):".format(
        user["name"], completed_count, len(todos)))

    for task in completed_tasks:
        print("\t{}".format(task["title"]))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide an employee ID as a command-line argument.")
    else:
        employee_id = int(sys.argv[1])
        fetch_todo_list(employee_id)
