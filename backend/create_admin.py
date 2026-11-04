"""
Script to create an admin user
Run this from the backend directory: python create_admin.py
"""
import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from auth.email_service import auth_service

def create_admin_user():
    print("=" * 50)
    print("CREATE ADMIN USER")
    print("=" * 50)
    
    # Get admin details
    full_name = input("Enter admin full name (default: Admin User): ").strip() or "Admin User"
    email = input("Enter admin email (default: admin@letgo.com): ").strip() or "admin@letgo.com"
    password = input("Enter admin password (default: admin123): ").strip() or "admin123"
    
    print("\nCreating admin user...")
    print(f"Name: {full_name}")
    print(f"Email: {email}")
    print(f"Role: admin")
    
    try:
        user_data = auth_service.register_user(
            full_name=full_name,
            email=email,
            password=password,
            role='admin'
        )
        
        print("\n✅ Admin user created successfully!")
        print(f"User ID: {user_data['id']}")
        print(f"Email: {user_data['email']}")
        print(f"Role: {user_data['role']}")
        print("\nYou can now login at http://localhost:5173/auth")
        
    except ValueError as e:
        print(f"\n❌ Error: {e}")
        if "already exists" in str(e).lower():
            print("\nThe admin user already exists. Try logging in with:")
            print(f"Email: {email}")
            print(f"Password: {password}")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        print("\nMake sure:")
        print("1. Backend server is running")
        print("2. Database connection is configured in .env")
        print("3. Auth schema is set up in Supabase")

if __name__ == "__main__":
    create_admin_user()
