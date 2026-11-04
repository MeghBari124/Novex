import sys
import os

# Add current directory to path
sys.path.append(os.getcwd())

try:
    print("Attempting to import feature7.router...")
    import feature7.router
    print("Success: feature7.router imported.")
except Exception as e:
    print(f"Error importing feature7.router: {e}")
    import traceback
    traceback.print_exc()
