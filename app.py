import json
import os
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from groq import Groq
import spacy
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize spaCy model & sentiment analyzer
nlp = spacy.load("en_core_web_sm")
analyzer = SentimentIntensityAnalyzer()

app = Flask(__name__)
CORS(app)

class Chatbot:
    def __init__(self, api_key, json_file):
        self.memory = {}
        self.chat_history = []  # Store last 5 messages for context
        self.client = Groq(api_key=api_key)

        # Load JSON data
        with open(json_file, "r") as file:
            self.json_data = json.load(file)
        self.json_summary = json.dumps(self.json_data)[:2000]  # Limit JSON size

    def ask(self, user_input):
        if not user_input:
            return "I didn't catch that. Could you please repeat? 😊"

        self.chat_history.append({"role": "user", "content": user_input[:300]})
        if len(self.chat_history) > 5:
            self.chat_history.pop(0)

        # Handle special cases
        response = self.handle_special_cases(user_input)
        if not response:
            response = self.generate_response(user_input)

        self.chat_history.append({"role": "assistant", "content": response})
        self.memory[user_input] = response

        return response

    def handle_special_cases(self, user_input):
        if self.is_greeting(user_input):
            return "Hey there! 😊 How can I assist you regarding Saveetha Engineering College?"
        elif self.is_conversational(user_input):
            return "I'm here to help! Ask me anything about SEC. 😃"
        elif self.is_about_bot(user_input):
            return "I'm Kavy, your friendly assistant at Saveetha Engineering College! Ask me about courses, programs, and more! 😄"
        elif self.is_negative_query(user_input):
            return "I understand your concerns, but SEC has a lot to offer! Let me know what you'd like to explore."
        elif self.is_sensitive_query(user_input):
            return "For details about fees, admissions, or scholarships, please contact the admissions office at +91 XXXXXXXXXX. 📞"
        return None

    def generate_response(self, user_input):
        try:
            messages = [{"role": "system", "content": "You are an assistant for Saveetha Engineering College. Answer only with SEC-related information."}]
            messages.extend(self.chat_history[-5:])
            messages.append({"role": "user", "content": user_input[:300]})

            completion = self.client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=messages,
                temperature=1,
                max_tokens=300,
                top_p=1
            )
            response = completion.choices[0].message.content.strip()
            return self.shorten_response(response)
        except Exception as e:
            print(f"Error generating response: {e}")
            return "Oops! Something went wrong. 😓 Can I assist with something else?"

    def shorten_response(self, response):
        words = response.replace("\n", " ").split()
        return " ".join(words[:50]) + ("..." if len(words) > 50 else "")

    def is_greeting(self, user_input):
        return any(greet in user_input.lower() for greet in ['hi', 'hello', 'hey', 'good morning', 'good evening'])

    def is_conversational(self, user_input):
        return any(phrase in user_input.lower() for phrase in ['can we talk', 'let’s chat', 'talk to me', 'let’s talk'])

    def is_about_bot(self, user_input):
        return any(phrase in user_input.lower() for phrase in ['what is your name', 'who are you', 'are you a bot'])

    def is_negative_query(self, user_input):
        return any(keyword in user_input.lower() for keyword in ['disadvantage', 'worst', 'bad', 'downside'])
    
    def is_sensitive_query(self, user_input):
        return any(keyword in user_input.lower() for keyword in ['fees', 'admission fee', 'scholarship', 'cutoff', 'eligibility'])

# Initialize chatbot
api_key = os.getenv("GROQ_API_KEY")
json_file = "new.json"
chatbot = Chatbot(api_key=api_key, json_file=json_file)
 
@app.route('/')
def home():
    welcome_message = "Hello! I’m Kavy, your friendly assistant at Saveetha Engineering College. 😊 How can I assist you today?"
    return render_template('index.html', welcome_message=welcome_message)

@app.route('/index', methods=['POST'])
def chat():
    user_input = request.json.get('message', '').strip()
    if not user_input:
        return jsonify({'reply': "I didn't catch that. Could you please repeat? 😊"})
    bot_response = chatbot.ask(user_input)
    return jsonify({'reply': bot_response})

if __name__ == '__main__':
    app.run(debug=True)
    
    
    