import os
import sys
import datetime
from dotenv import load_dotenv
from supabase import create_client

# Add backend directory to path
sys.path.append(os.path.join(os.getcwd(), 'backend'))

load_dotenv(os.path.join(os.getcwd(), 'backend', '.env'))

url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")
supabase = create_client(url, key)

try:
    print("Fetching one claim from claim_applications...")
    res = supabase.table("claim_applications").select("id").limit(1).execute()
    if not res.data:
        print("No claims found in claim_applications.")
        sys.exit(1)
        
    claim_id = res.data[0]['id']
    print(f"Found ID: {claim_id}")
    
    print("\nAttempting to insert assignment for this ID...")
    assignment = {
        "claim_id": claim_id,
        "officer_name": "Debug Officer",
        "visit_deadline": datetime.datetime.now().isoformat(),
        "status": "Assigned"
    }
    
    res_insert = supabase.table("field_officer_assignments").insert(assignment).execute()
    print("Insert successful!")
    print(res_insert.data)

except Exception as e:
    print("\nERROR DETAILS:")
    print(e)
