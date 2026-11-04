"""
Comprehensive API Test Suite for Let Go 3.0
Tests all features and endpoints
"""
import requests
import json
import time

BASE_URL = "http://127.0.0.1:8000"

# Color codes for terminal output
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
RESET = '\033[0m'

def print_header(text):
    print(f"\n{BLUE}{'='*60}{RESET}")
    print(f"{BLUE}{text.center(60)}{RESET}")
    print(f"{BLUE}{'='*60}{RESET}")

def test_endpoint(name, url, method="GET", payload=None, files=None, expected_status=200):
    """Test a single endpoint"""
    print(f"\n{YELLOW}Testing: {name}{RESET}")
    print(f"  URL: {method} {url}")
    
    try:
        if method == "GET":
            response = requests.get(url, timeout=10)
        elif method == "POST":
            if files:
                response = requests.post(url, files=files, timeout=10)
            else:
                headers = {"Content-Type": "application/json"}
                response = requests.post(url, json=payload, headers=headers, timeout=10)
        elif method == "PATCH":
            headers = {"Content-Type": "application/json"}
            response = requests.patch(url, json=payload, headers=headers, timeout=10)
        
        status_ok = response.status_code == expected_status
        status_color = GREEN if status_ok else RED
        
        print(f"  Status: {status_color}{response.status_code}{RESET} (Expected: {expected_status})")
        
        if response.status_code in [200, 201]:
            try:
                data = response.json()
                if isinstance(data, list):
                    print(f"  {GREEN}[OK] Success - {len(data)} items{RESET}")
                elif isinstance(data, dict):
                    if "data" in data and isinstance(data["data"], list):
                        print(f"  {GREEN}[OK] Success - {len(data['data'])} items in 'data'{RESET}")
                    elif "products" in data:
                        print(f"  {GREEN}[OK] Success - {len(data['products'])} products{RESET}")
                    elif "success" in data:
                        print(f"  {GREEN}[OK] Success: {data.get('success')}{RESET}")
                    else:
                        print(f"  {GREEN}[OK] Success - Keys: {list(data.keys())[:5]}{RESET}")
                return True
            except:
                print(f"  {GREEN}[OK] Success (Non-JSON response){RESET}")
                return True
        else:
            print(f"  {RED}[X] Failed: {response.text[:200]}{RESET}")
            return False
            
    except requests.exceptions.ConnectionError:
        print(f"  {RED}[X] Connection Error - Is backend running?{RESET}")
        return False
    except requests.exceptions.Timeout:
        print(f"  {RED}[X] Timeout - Request took too long{RESET}")
        return False
    except Exception as e:
        print(f"  {RED}[X] Error: {str(e)[:100]}{RESET}")
        return False

def run_all_tests():
    """Run comprehensive test suite"""
    results = {"passed": 0, "failed": 0, "total": 0}
    
    print_header("LET GO 3.0 - API TEST SUITE")
    
    # Wait for server
    print(f"\n{YELLOW}Checking if server is running...{RESET}")
    for i in range(5):
        try:
            requests.get(f"{BASE_URL}/api/health", timeout=2)
            print(f"{GREEN}[OK] Server is running!{RESET}")
            break
        except:
            if i < 4:
                print(f"  Waiting... ({i+1}/5)")
                time.sleep(2)
            else:
                print(f"{RED}[X] Server not responding. Please start backend first!{RESET}")
                return
    
    # ========== CORE ENDPOINTS ==========
    print_header("CORE ENDPOINTS")
    
    tests = [
        ("Root Endpoint", f"{BASE_URL}/"),
        ("Health Check", f"{BASE_URL}/api/health"),
        ("Products List", f"{BASE_URL}/api/products"),
    ]
    
    for name, url in tests:
        results["total"] += 1
        if test_endpoint(name, url):
            results["passed"] += 1
        else:
            results["failed"] += 1
    
    # ========== FEATURE 1: LAND REGISTRY (BLOCKCHAIN) ==========
    print_header("FEATURE 1: LAND REGISTRY (BLOCKCHAIN)")
    
    tests = [
        ("List Lands", f"{BASE_URL}/api/feature1/lands"),
        ("Get Land Details", f"{BASE_URL}/api/feature1/land/1", "GET", None, None, 404),  # Expected 404 if no data
    ]
    
    for name, *args in tests:
        results["total"] += 1
        if test_endpoint(name, *args):
            results["passed"] += 1
        else:
            results["failed"] += 1
    
    # ========== FEATURE 2: CROP HEALTH & DISEASE DETECTION ==========
    print_header("FEATURE 2: CROP HEALTH & DISEASE")
    
    tests = [
        ("Get Agronomists", f"{BASE_URL}/api/feature2/agronomists?count=2"),
        ("Get Scheme Applications", f"{BASE_URL}/api/feature2/scheme-applications?limit=10"),
        ("Application Statistics", f"{BASE_URL}/api/feature2/scheme-applications/statistics"),
    ]
    
    for name, url in tests:
        results["total"] += 1
        if test_endpoint(name, url):
            results["passed"] += 1
        else:
            results["failed"] += 1
    
    # ========== FEATURE 3: AUTONOMOUS FARM CONTROL ==========
    print_header("FEATURE 3: AUTONOMOUS FARM")
    
    tests = [
        ("Get Sensor History", f"{BASE_URL}/api/feature3/history?user_id=HARDWARE_DEFAULT"),
        ("Get Recommendations", f"{BASE_URL}/api/feature3/recommendations?user_id=HARDWARE_DEFAULT"),
    ]
    
    for name, url in tests:
        results["total"] += 1
        if test_endpoint(name, url):
            results["passed"] += 1
        else:
            results["failed"] += 1
    
    # ========== FEATURE 4: CROP RECOMMENDATIONS (DRL) ==========
    print_header("FEATURE 4: CROP RECOMMENDATIONS")
    
    tests = [
        ("Health Check", f"{BASE_URL}/api/feature4/health"),
        ("Available Crops", f"{BASE_URL}/api/feature4/crops"),
    ]
    
    for name, url in tests:
        results["total"] += 1
        if test_endpoint(name, url):
            results["passed"] += 1
        else:
            results["failed"] += 1
    
    # Test recommendation endpoint with sample data
    results["total"] += 1
    sample_data = {
        "soil_n": 50,
        "soil_p": 35,
        "soil_k": 40,
        "soil_ph": 6.5,
        "soil_moisture": 55,
        "avg_temperature": 28,
        "seasonal_rainfall": 850,
        "humidity": 65,
        "crop_duration_days": 120,
        "district": "Sample",
        "state": "Sample",
        "soil_type": "Alluvial",
        "climate_season": "Kharif",
        "previous_crop": "Rice",
        "crop_water_requirement": "Medium"
    }
    if test_endpoint("Crop Recommendation", f"{BASE_URL}/api/feature4/recommend", "POST", sample_data):
        results["passed"] += 1
    else:
        results["failed"] += 1
    
    # ========== FEATURE 5: EQUIPMENT & SUBSIDIES ==========
    print_header("FEATURE 5: EQUIPMENT & SUBSIDIES")
    
    tests = [
        ("Get Subsidies", f"{BASE_URL}/api/subsidies", "POST", {}),
        ("Available States", f"{BASE_URL}/api/subsidies/states"),
    ]
    
    for name, *args in tests:
        results["total"] += 1
        if test_endpoint(name, *args):
            results["passed"] += 1
        else:
            results["failed"] += 1
    
    # ========== FEATURE 6: INVENTORY & BLOCKCHAIN ==========
    print_header("FEATURE 6: INVENTORY & BLOCKCHAIN")
    
    tests = [
        ("List Batches", f"{BASE_URL}/api/feature6/list/farmer123"),
        ("Get Timeline", f"{BASE_URL}/api/feature6/timeline/batch123", "GET", None, None, 404),  # Expected 404
    ]
    
    for name, *args in tests:
        results["total"] += 1
        if test_endpoint(name, *args):
            results["passed"] += 1
        else:
            results["failed"] += 1
    
    # ========== HARDWARE & SENSORS ==========
    print_header("HARDWARE & SENSORS")
    
    tests = [
        ("Latest Sensor Data", f"{BASE_URL}/api/hardware/latest?user_id=HARDWARE_DEFAULT"),
    ]
    
    for name, url in tests:
        results["total"] += 1
        if test_endpoint(name, url):
            results["passed"] += 1
        else:
            results["failed"] += 1
    
    # ========== NEWS ==========
    print_header("NEWS & ALERTS")
    
    tests = [
        ("Get News", f"{BASE_URL}/api/news"),
    ]
    
    for name, url in tests:
        results["total"] += 1
        if test_endpoint(name, url):
            results["passed"] += 1
        else:
            results["failed"] += 1
    
    # ========== FINAL RESULTS ==========
    print_header("TEST RESULTS")
    
    pass_rate = (results["passed"] / results["total"] * 100) if results["total"] > 0 else 0
    
    print(f"\n  Total Tests: {results['total']}")
    print(f"  {GREEN}Passed: {results['passed']}{RESET}")
    print(f"  {RED}Failed: {results['failed']}{RESET}")
    print(f"  Pass Rate: {GREEN if pass_rate >= 80 else YELLOW if pass_rate >= 50 else RED}{pass_rate:.1f}%{RESET}")
    
    if pass_rate >= 80:
        print(f"\n  {GREEN}[OK] EXCELLENT! Most features are working!{RESET}")
    elif pass_rate >= 50:
        print(f"\n  {YELLOW}[!] PARTIAL - Some features need attention{RESET}")
    else:
        print(f"\n  {RED}[X] CRITICAL - Many features are failing{RESET}")
    
    print(f"\n{BLUE}{'='*60}{RESET}\n")

if __name__ == "__main__":
    run_all_tests()
