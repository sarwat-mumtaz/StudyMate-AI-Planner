# StudyMate-AI-Planner
AI-powered study planner with interactive chat interface

StudyMate is an AI-powered chatbot that helps students create personalized study plans.
It uses OpenAI GPT for smart responses and Panel for an interactive dashboard.

🚀 Features

🤖 Friendly chatbot that guides you step by step

📝 Collects study details: subjects, available hours, exam date, study style

📅 Generates daily & weekly study schedules

☕ Suggests break times and motivation tips

🎨 Interactive dashboard built with Panel

🛠️ Installation

Clone this repository:

git clone https://github.com/sarwatmumtaz/StudyMate.git
cd StudyMate


Install dependencies:

pip install -r requirements.txt


Create a .env file and add your OpenAI API key:

OPENAI_API_KEY=your_api_key_here

▶️ Usage

Run the app:

python studymate.py


👉 The dashboard will open, where you can chat with StudyMate and get your custom study plan.

📦 Project Structure
StudyMate/
│── studymate.py        # Main app code
│── requirements.txt    # Project dependencies
│── .gitignore          # Ignore sensitive/extra files
│── README.md           # Project documentation
│── .env                # (Not uploaded) contains API key

💡 Example Conversation

👤 Student: Hi, I have exams in 2 weeks.
🎓 StudyMate: Great! Which subjects do you need to study?

👤 Student: Math, Physics, and English.
🎓 StudyMate: Perfect! How many hours per day can you study?

... (StudyMate generates a full study schedule)

🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss.
