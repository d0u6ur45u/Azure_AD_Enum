# Azure AD Email Enumeration PoC

This script performs an enumeration of emails against Azure Active Directory by analyzing authentication error responses.

## ⚠️ Disclaimer
This tool is intended for educational and security research purposes only. Do not use it against systems without proper authorization.

## 🔧 Requirements
- Python 3.x
- `requests` module

Install dependencies with:
```sh
pip install requests
```

## 🚀 Usage
1. Modify the `emails` list in the script with the target email addresses.
2. Replace `TENANTID` in the `url` variable with the actual Azure AD tenant ID.
3. Run the script:
```sh
python 
```

## 📌 Response Interpretation
- 🟢 `[VALID]` The user exists, but the password is incorrect.
- 🔴 `[INVALID]` The user does not exist.
- 🟡 `[UNKNOWN]` An unexpected error occurred.
- 🚨 `[ERROR]` Unexpected HTTP response.

## 📝 Example Output
```
🟢 [VALID] User exists but password is incorrect: john@email.com (Error: AADSTS50126)
🔴 [INVALID] User does not exist: jane@email.com (Error: AADSTS50034)
🟡 [UNKNOWN] Unexpected error for test@email.com: Some error description
🚨 [ERROR] Unexpected response for unknown@email.com: 403 - Forbidden
```

## 📜 License
This project is open-source and available under the MIT License.