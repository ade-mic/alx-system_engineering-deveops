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
    employee_name = user_data['name']
    user_id = user_data['id']
    user_name = user_data['username']

    # Fetch TODO list data
    todo_response = requests.get(todo_url)
    todo_data = todo_response.json()

    # Prepare CSV data
    csv_data = [['{}'.format(user_id), '{}'.format(user_name),
                 '{}'.format(task['completed']), '{}'.format(task['title'])]
                for task in todo_data]

    # Write CSV file
    file_name = '{}.csv'.format(user_id)
    with open(file_name, "w", newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerows(csv_data)


if __name__ == "__main__":
    main()
