#!/usr/bin/python3
"""
a Python script that, using this REST API, for a given employee ID, returns
information about his/her TODO list progress.
"""
import csv
import json
import requests


def main():
    """
    Program entrance
    """
    base_url = 'https://jsonplaceholder.typicode.com/'
    user_url = '{}/users/'.format(base_url)
    todo_url = '{}/todos?'.format(base_url)

    # Fetch uer data
    user_response = requests.get(user_url)
    user_data = user_response.json()

    # Fetch TODO list data
    todo_response = requests.get(todo_url)
    todo_data = todo_response.json()

    # Prepare CSV data
    json_data = {}
    for user in user_data:
        user_id = user['id']
        username = user['username']
        user_tasks = [{"username": username, "task": task['title'],
                       "completed": task['completed']}
                      for task in todo_data if task['userId'] == user_id]

    # Write JSON file
    file_name = 'todo_all_employees.json'
    with open(file_name, 'w') as jsonfile:
        json.dump(json_data, jsonfile, indent=4)


if __name__ == "__main__":
    main()
