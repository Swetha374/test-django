##Sample TEST script

import requests, subprocess

HOST = 'http://127.0.0.1:6565'
status = {'home_page': '-', 'register_user': '-', 'login_user': '-', 'profile_page': '-'}

def test_home_page():
    response = requests.get(HOST)
    if response.status_code == 200:
        status['home_page'] = '✅'
        # print('Home page check passed')
    else:
        status['home_page'] = '❌' 
def register_user():
    auth_data = {
                    "email": "test@email.com",
                    "first_name": "test1",
                    "last_name": "tes_last",
                    "phone_number": "9876543211",
                    "password": "i9P@nd23mciud"
                }
    response = requests.post(HOST+'/api/user/register', data=auth_data)
    if response.status_code == 200:
        status['register_user'] = '✅' 
    else:
        status['register_user'] = '❌' 
def login_user():
    auth_data = {
                    "email": "test@email.com", 
                    "password": "i9P@nd23mciud"
                }
    response = requests.post(HOST+'/api/user/login', data=auth_data)
    if response.status_code == 200:
        status['login_user'] = '✅' 
    else:
        status['login_user'] = '❌'
def profile_page():
    try:
        response = requests.get(HOST+'/api/user/me')
        if response.status_code == 200:
            if response.json()['email'] == 'test@email.com':
                status['profile_page'] = '✅'
            else:
                status['profile_page'] = '~No Json❌' 
        else:
            status['profile_page'] = '❌'
    except Exception as e:
        status['profile_page'] = '❌'

def check_data_loading():
    pass  #in real script
def check_hompage_features():
    pass #in real script
def check_code_quality(): 
    try: 
        result = subprocess.run(['pre-commit', 'run', '--all-files'], check=True, text=True, capture_output=True)
        print("Pre-commit checks passed successfully.")
        status['check_code_quality'] = '✅'
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print("Pre-commit checks failed.")
        status['check_code_quality'] = '❌'
        print(e.output)
 

if __name__ == '__main__':
    test_home_page()
    register_user()
    login_user()
    profile_page()
    check_data_loading()
    check_hompage_features()
    check_code_quality()
    print(status)