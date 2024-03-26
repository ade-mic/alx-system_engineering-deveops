#!/usr/bin/python3
"""
a Python script that, using this REST API, for a given employee ID, returns
information about his/her TODO list progress.
"""
import csv
import json
import requests
from sys import argv


def main():
    """
    Program entrance
    """
    employee_id = argv[1]
    base_url = 'https://jsonplaceholder.typicode.com/'
    user_url = '{}/users/{}'.format(base_url, employee_id)
    todo_url = '{}/todos?userId={}'.format(base_url, employee_id)

    # Fetch uer data
    user_response = requests.get(user_url)
    user_data = user_response.json()
    user_id = user_data['id']
    user_name = user_data['username']

    # Fetch TODO list data
    todo_response = requests.get(todo_url)
    todo_data = todo_response.json()

    # Prepare CSV data
    json_data = {
        "USER_ID": [{"task": task['title'], "completed": task['completed'],
                     "username": user_name} for task in todo_data]
    }

    # Write CSV file
    file_name = '{}.csv'.format(user_id)
    with open(file_name, "w", newline='') as jsonfile:
        json.dump(json_data, jsonfile, indent=4)


if __name__ == "__main__":
    main()
