🔧 How To Run This Project Locally
1️⃣ Clone the Repository
git clone https://github.com/BeuRaze/multi-agent-automotive-system.git
cd multi-agent-automotive-system

2️⃣ Create Virtual Environment
python -m venv venv


Activate:

Windows:

venv\Scripts\activate


Mac/Linux:

source venv/bin/activate

3️⃣ Install Dependencies

If you don't have requirements.txt, create one:

langchain
langchain-groq
python-dotenv
groq


Then run:

pip install -r requirements.txt

4️⃣ Add Groq API Key

Create a .env file in root:

GROQ_API_KEY=your_api_key_here

5️⃣ Run Project
python main.py
