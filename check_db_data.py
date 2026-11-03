import os
import sys
import json
from dotenv import load_dotenv
from supabase import create_client

# Add backend directory to path to import supabase_client if needed, 
# but better to just recreate connection here to be standalone
sys.path.append(os.path.join(os.getcwd(), 'backend'))

load_dotenv(os.path.join(os.getcwd(), 'backend', '.env'))

url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")

if not url or not key:
    print("Error: Missing SUPABASE_URL or SUPABASE_KEY")
    sys.exit(1)

supabase = create_client(url, key)

print(f"Connecting to Supabase: {url}")

try:
    print("\n--- Fetching claim_applications ---")
    response = supabase.table("claim_applications").select("*").execute()
    claims = response.data
    print(f"Found {len(claims)} claims.")
    
    for i, claim in enumerate(claims):
        inspector_id = claim.get('assigned_inspector_id')
        app_details = claim.get('application_details', {})
        
        # Check fallback
        fallback_inspector = app_details.get('assigned_inspector_id') if app_details else None
        
        print(f"\nClaim {i+1}: ID={claim.get('id')}")
        print(f"  Ref No: {claim.get('reference_no')}")
        print(f"  DB Column 'assigned_inspector_id': {inspector_id}")
        print(f"  JSONB 'assigned_inspector_id': {fallback_inspector}")
        print(f"  Farmer Name: {claim.get('farmer_name')}")
        
    print("\n--- Fetching users (if accessible) ---")
    # Usually strictly protected, but let's try reading public profiles if they exist
    try:
        # Check for a 'users' or 'profiles' table which might hold real user names
        profiles = supabase.table("farmer_profiles").select("*").execute() # Just guessing table name for staff?
        # Or maybe there is an admin/staff table?
        print(f"Found {len(profiles.data)} farmer_profiles (not necessarily officers).")
    except Exception as e:
        print(f"Could not fetch profiles: {e}")

except Exception as e:
    print(f"Error: {e}")
