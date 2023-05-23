#!/usr/bin/python3
"""[Exports info from requests into CSV file
    format: ]
"""
if __name__ == "__main__":
    import csv
    import requests
    import sys

    url_user = "https://jsonplaceholder.typicode.com/users/{}".format(
        sys.argv[1])
    url_todo = "https://jsonplaceholder.typicode.com/users/{}/todos".format(
        sys.argv[1])
    employee = requests.get(url_user).json()
    # print(employee)
    employeeName = employee.get('username')
    employeeID = employee.get('id')
    print(employeeName)
    allTasks = requests.get(url_todo).json()
    # print(type(allTasks))
    csvfile = "{}.csv".format(sys.argv[1])

    for task in allTasks:
        with open(csvfile, 'a', newline='') as file:
            my_writer = csv.writer(file, quoting=csv.QUOTE_ALL)
            values = []
            values.append("{}".format(sys.argv[1]))
            values.append("{}".format(employeeName))
            values.append("{}".format(task.get('completed')))
            values.append("{}".format(task.get('title')))
            my_writer.writerow(values)
