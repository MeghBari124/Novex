Annadata Saathi- Digital Agri Ecosystem

Problem Statement (PS)
Small and marginal farmers face crop losses due to delayed disease detection, unpredictable weather, inefficient resource utilization, and limited access to agricultural experts. Fragmented agricultural services and low digital accessibility further make it difficult for farmers to obtain timely guidance, access government benefits, and connect directly with buyers.

Proposed Solution
Annadata Saathi is an AI-powered smart agriculture platform designed to support farmers throughout the agricultural lifecycle. It combines crop monitoring, disease detection, personalized farming recommendations, and digital agricultural services in one accessible platform.

Key Features
- Crop Disease Detection: Identifies potential crop diseases from uploaded images.
- NDVI Field Monitoring: Uses satellite-based vegetation analysis to monitor crop health.
- AI Farming Advisory: Provides crop care, irrigation, and fertilizer recommendations.
- IoT Monitoring: Optional soil sensors monitor moisture, NPK, pH, and environmental conditions.
- Government Schemes Portal: Helps farmers discover relevant agricultural schemes and benefits.
- Agronomist Connect: Enables farmers to seek expert agricultural guidance.
- Voice-Based Navigation: Supports easier interaction through voice commands.
- AI Calling Agent: Delivers automated farming reminders and alerts.
- Marketplace and Inventory: Supports produce management and farmer-to-buyer connections.
- Smart Warehouse Monitoring: Provides safety alerts for potential storage hazards.

Technology Stack Used
Component| Technology
Frontend| React.js
Backend| Python, FastAPI
Database and Authentication| Supabase
Disease Detection| CNN-based image classification
AI Advisory| AI and machine learning
Voice Calling| Twilio APIs
Field Monitoring| Satellite-based NDVI
Hardware Integration| IoT sensors
Deployment| Web hosting and cloud infrastructure

System Architecture
The platform follows a modular architecture in which the frontend communicates with backend APIs, which process agricultural data and connect with the required services.

Architecture Flow
Farmer / User
      |
      v
React.js Frontend
      |
      v
FastAPI Backend
      |
      +----------------------+
      |                      |
      v                      v
AI and ML Services     Supabase
      |                 Database
      |
      +----------------------+
      |          |           |
      v          v           v
   Disease     NDVI       Farming
  Detection  Monitoring   Advisory
      |
      v
Recommendations, Alerts and Farmer Services
IoT sensors provide soil and environmental readings to the backend. Twilio supports automated calls and notifications, while external satellite and weather services supply relevant agricultural data.

5. How to Run the Project
Prerequisites
Install the following software before running the project:
- Node.js and npm
- Python 3.10 or a compatible version
- Git
- A Supabase project with the required credentials

Step 1: Clone the Repository
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd <PROJECT_FOLDER>

Step 2: Set Up the Backend
Open a terminal inside the backend directory.
cd backend
python -m venv .venv
Activate the virtual environment.
Windows:
.venv\Scripts\activate
Linux or macOS:
source .venv/bin/activate
Install the backend dependencies and start the server.
pip install -r requirements.txt
uvicorn main:app --reload
The backend will typically run at:
"http://localhost:8000"
API documentation is available at:
"http://localhost:8000/docs"

Step 3: Set Up the Frontend
Open another terminal.
cd frontend
npm install
npm run dev
The frontend will typically run at:
"http://localhost:5173"
Open this address in your browser to access the application.

Step 4: Configure Environment Variables
Create the required ".env" files for the frontend and backend.
Configure the following values using your actual project credentials:
SUPABASE_URL=
SUPABASE_KEY=
TWILIO_ACCOUNT_SID=
TWILIO_AUTH_TOKEN=
TWILIO_PHONE_NUMBER=
Add the frontend API URL and any required AI or satellite service credentials as well.
Never commit secret keys or passwords to a public repository.

Step 5: Verify the Application
- Confirm that the frontend loads successfully.
- Verify backend API connectivity.
- Test database connectivity and authentication.
- Test disease detection and other implemented AI features.
- Verify optional integrations such as NDVI, IoT sensors, and automated calling.
Note: The commands above assume separate "frontend" and "backend" directories, a FastAPI entry point named "main.py", and a "requirements.txt" file. Adjust these commands to match your actual repository structure.

6. Hosted Project Link
The deployed application can be accessed using the following link:
Live Demo: https://annadatasaathi.vercel.app/

Youtube Link: https://youtu.be/6NGVtaal0-M?si=iB6OuavCTqgHdXE4

Google Drive Link: https://drive.google.com/drive/folders/1irV_cRrdul3iO_6N9gzjG56NWYeboaDF?usp=sharing

The live demo allows users to explore the deployed platform, while the GitHub repository provides access to the source code and implementation details.

Project Vision: To make intelligent, affordable, and climate-resilient farming accessible to small and marginal farmers through integrated AI, IoT, and digital agricultural services.
