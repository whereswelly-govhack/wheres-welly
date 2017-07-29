import json
import sys
import getpass
import requests

app_id = '{Ri3XuznuO1KxP5HRSdj1}'
app_code = '{qYlHGxozqUYD67mWrz5DiQ}'

# This function obtains an access token.
#
# @param user_name User name associated with HERE Account
# @param password Password associated with HERE Account
# @param app_id The value of app_id
# @param app_code The value of app_code
#
# @return A string containing the HERE access token

def get_access_token(user_name, password, app_id, app_code):
    url = 'https://datalens.api.here.com/v1/sign_in/?%s=%s&%s=%s' % ('app_id', app_id, 'app_code', app_code)
    payload = json.dumps({'email': user_name, 'password': password})
    r = requests.post(url,
                      headers={'Content-Type': 'application/json'},
                      data=payload)

    if r.status_code == 200:
        response = r.json()
        return response['access_token']

    raise Exception('Cannot get Data Lens access_token. Status code: %s ' % r.status_code)

# This function runs a request to retrieve data sets.
#
# @param access_token The HERE access token
# @param app_id The value of app_id
# @param app_code The value of app_code
#
# @return A JSON string containing the retrieved data sets

def get_datasets(acess_token, app_id, app_code):
    url = 'https://datalens.api.here.com/v1/datasets/?%s=%s&%s=%s'% ('app_id', app_id, 'app_code', app_code)
    r = requests.get(url,
                     headers={'Content-Type': 'text/plain',
                              'Authorization': 'Bearer %s' % access_token})
    if r.status_code == 200:
        return r.json()

    raise Exception('Cannot get retrieve datasets: %s' % r.status_code)

# The main function of the script expects two command line arguments:
# the HERE Account user name and the HERE Account password. It uses
# them, along with the application-specific app_id and app_code, to
# obtain an access token and request datasets.

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print 'get_token.py - provides an Auth token (valid for 1 hour)'
        print 'usage: get_token.py username'
        sys.exit()
    user_name = sys.argv[1]
    password = getpass.getpass()
    access_token = get_access_token(user_name, password, app_id, app_code)
    if access_token:
        print get_datasets(access_token, app_id, app_code)