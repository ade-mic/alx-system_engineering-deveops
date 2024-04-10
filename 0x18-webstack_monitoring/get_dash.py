#!/usr/bin/python3
"""
Get all dashboard lists returns "OK" response
"""

import requests

def get_dashboards():

    # Replace with your actual Datadog API and application keys
    API_KEY = 'a17145aa549834930ecc1950d2960294'
    APP_KEY = '45908cfb5c80da52fe800290f1ea889f3c014f71'

    # Datadog API endpoint for dashboards
    DASHBOARD_API_URL = 'https://api.datadoghq.com/api/v1/dashboard'

    headers = {
        'DD-API-KEY': API_KEY,
        'DD-APPLICATION-KEY': APP_KEY,
    }

    try:
        response = requests.get(DASHBOARD_API_URL, headers=headers)
        response.raise_for_status()  # Raise an exception if the request fails

        dashboards = response.json().get('dashboards', [])
        for dashboard in dashboards:
            dashboard_id = dashboard.get('id')
            dashboard_title = dashboard.get('title')
            print(f"Dashboard ID: {dashboard_id}, Title: {dashboard_title}")

    except requests.RequestException as e:
        print(f"Error fetching dashboards: {e}")

if __name__ == '__main__':
    get_dashboards()
