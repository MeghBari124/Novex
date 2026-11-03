import os
from supabase import create_client
from dotenv import load_dotenv

load_dotenv("backend/.env")

url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")
supabase = create_client(url, key)

try:
    print("Checking 'claims' table...")
    supabase.table("claims").select("id").limit(1).execute()
    print("Table 'claims' exists.")
except Exception as e:
    print(f"Table 'claims' check failed: {e}")

try:
    print("Checking 'claim_applications' table...")
    supabase.table("claim_applications").select("id").limit(1).execute()
    print("Table 'claim_applications' exists.")
except Exception as e:
    print(f"Table 'claim_applications' check failed: {e}")

try:
    print("Checking 'field_officer_assignments' table...")
    supabase.table("field_officer_assignments").select("id").limit(1).execute()
    print("Table 'field_officer_assignments' exists.")
except Exception as e:
    print(f"Table 'field_officer_assignments' check failed: {e}")
