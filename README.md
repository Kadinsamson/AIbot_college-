# 🤖 Sentiment-Aware Contextual Chatbot

## 📌 Overview
An AI-powered **college assistance chatbot** that understands both **context** and **emotion** in user queries.  
Designed for students and parents to get empathetic, relevant, and conversational answers in real-time.

---

## 🧠 Problem Statement
Traditional chatbots often:
- Give **generic, robotic replies**.
- Fail to understand **emotions** like stress or excitement.
- Lack **context awareness** for follow-up questions.

For example:
> User: "I'm stressed about my exams"  
> Traditional bot: "Okay, noted."  
> This chatbot: "I understand exams can be stressful. Do you want some study tips or relaxation techniques?"

---

## 💡 Solution
This chatbot combines **Natural Language Processing** (NLP) and **Sentiment Analysis** to provide:
- Context-based answers for college-related queries.
- Emotion-aware responses using **VADER** sentiment analysis.
- **Intent detection** with spaCy to identify user needs.
- **LLaMA via Groq API** for natural, human-like conversations.
- Multi-turn conversation support with tone adaptation.
- **FAQ integration** using JSON files served via Flask API.

---

## 🛠 Tech Stack
| Technology | Purpose |
|------------|---------|
| Python | Core programming |
| Flask | Backend API for chatbot |
| spaCy | NLP & intent detection |
| VADER | Sentiment analysis |
| Groq API (LLaMA) | AI text generation |
| JSON | FAQ storage |

---

## 🚀 Installation & Running

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Kadinsamson/College_Chatbot.git
cd College_Chatbot
```
Install Dependencies
```
pip install -r requirements.txt
```
3️⃣ Run the Flask Server
```
python chatbot_app.py
```
4️⃣ Access the Chatbot

Open http://127.0.0.1:5000/chat in your browser or integrate with a frontend/Telegram bot.

📸 Screenshots
Home 
<img width="1042" height="654" alt="Screenshot 2025-08-15 131521" src="https://github.com/user-attachments/assets/06104356-5fcc-4c23-9bb8-81385407ba87" />
conversations
<img width="1038" height="913" alt="Screenshot 2025-08-15 131619" src="https://github.com/user-attachments/assets/d34d9dda-f368-41d5-b0cf-6078c4feb326" />

<img width="570" height="681" alt="Screenshot 2025-08-15 131821" src="https://github.com/user-attachments/assets/cb189299-30f8-4878-a459-57db77ec19ee" />
<img width="502" height="547" alt="Screenshot 2025-08-15 131916" src="https://github.com/user-attachments/assets/d82b7d3e-5546-461b-91d1-d810277d3616" />

👩‍💻 Authors

Kadin Samson – GitHub | 📩 l.kadinsamson@gmail.com

Kavya K – 📩 kavyasenthamarai@gmail.com 
