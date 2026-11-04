import requests
import json

BASE_URL = "http://localhost:8000"

def test_endpoint(name, url, method="GET", payload=None):
    print(f"\n--- Testing {name} ({method} {url}) ---")
    try:
        if method == "GET":
            response = requests.get(url)
        elif method == "POST":
            headers = {"Content-Type": "application/json"}
            response = requests.post(url, json=payload, headers=headers)
        
        print(f"Status: {response.status_code}")
        if response.status_code == 200:
            try:
                data = response.json()
                print("Success: True")
                # Print summary if list
                if isinstance(data, list):
                    print(f"Items found: {len(data)}")
                elif isinstance(data, dict):
                     if "data" in data and isinstance(data["data"], list):
                         print(f"Items in 'data': {len(data['data'])}")
                     elif "products" in data:
                         print(f"Products found: {len(data['products'])}")
                     else:
                         print("Response keys:", list(data.keys()))
            except:
                print("Response not JSON:", response.text[:100])
        else:
             print("Error:", response.text[:200])
             
    except Exception as e:
        print(f"Failed: {e}")

def run_tests():
    # 1. Health
    test_endpoint("Health Check", f"{BASE_URL}/api/health")
    
    # 2. Products
    test_endpoint("Products", f"{BASE_URL}/api/products")
    
    # 3. Schemes (Feature 5) - Assuming endpoint /api/schemes/all or similar exist, need to check router
    # Checking main.py: app.include_router(feature5_router, prefix="/api/schemes", tags=["Schemes"])
    # Let's try listing schemes if likely endpoint exists. Typically /api/schemes/
    # From Step 25 output, we see feature5_router imported. We don't see exact paths.
    # But usually List is at root or /all. Let's try /api/schemes/subsidies (from main.py import get_all_subsidies)
    # Actually main.py has /api/subsidies explicitly defined at lines 312.
    test_endpoint("Subsidies (Main)", f"{BASE_URL}/api/subsidies", method="POST", payload={})
    
    # 4. News
    test_endpoint("News", f"{BASE_URL}/api/news/latest") # Guessing endpoint
    
    # 5. Blockchain (Feature 6)
    test_endpoint("Blockchain Inventory", f"{BASE_URL}/api/feature6/inventory") # Guessing
    
    # 6. Feature 3
    test_endpoint("Feature 3", f"{BASE_URL}/api/feature3/") # Guessing
    
    # 7. Warehouse (Feature 7)
    test_endpoint("Warehouse Safety", f"{BASE_URL}/api/feature7/status") # Guessing

if __name__ == "__main__":
    run_tests()
