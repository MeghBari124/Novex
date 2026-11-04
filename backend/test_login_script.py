import requests
import json

BASE_URL = "http://localhost:8000"

def test_health():
    try:
        response = requests.get(f"{BASE_URL}/api/health")
        print(f"Health Check: {response.status_code}")
        print(response.json())
    except Exception as e:
        print(f"Health Check Failed: {e}")

def test_login(email, password, role_name):
    url = f"{BASE_URL}/api/auth/login"
    payload = {
        "email": email,
        "password": password
    }
    headers = {
        "Content-Type": "application/json"
    }
    
    try:
        response = requests.post(url, json=payload, headers=headers)
        print(f"\nLogin Test for {role_name} ({email}):")
        print(f"Status Code: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            print("Success:", data.get("success"))
            print("Message:", data.get("message"))
            print("User Role:", data.get("user", {}).get("role"))
        else:
            print("Response:", response.text)
    except Exception as e:
        print(f"Login Failed: {e}")

if __name__ == "__main__":
    test_health()
    test_login("bingostingo1@gmail.com", "bingostingo1", "User")
    test_login("samarthbhirud123@gmail.com", "samarthbhirud", "Admin")
