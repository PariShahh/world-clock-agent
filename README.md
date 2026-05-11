# 🌍 World Clock Agent

An AI Agent built using Google's Agent Development Kit (ADK) 
that tells the real current time in any city around the world.

## 🤖 About
This agent uses Google's ADK framework powered by Gemini 2.5 
Flash to understand natural language queries and automatically 
call a custom Python tool to fetch real-time data.

## ✨ Features
- 🌍 Real current time for any city in the world
- 🧠 Context aware — understands states vs cities
- ⚡ Automatic tool selection and execution
- 🕐 Returns accurate time with timezone information
- 💬 Natural language understanding

## 🛠️ Built With
- [Google ADK](https://google.github.io/adk-docs/) 
- Gemini 2.5 Flash
- Python 3.11
- geopy
- timezonefinder
- pytz

## 📁 Project Structure
my_agent/
    agent.py        # Main agent code
    __init__.py     # Package init
    .env            # API keys (not pushed to GitHub)
    .gitignore      # Git ignore file

## 🚀 Getting Started

### Prerequisites
- Python 3.11+
- Google ADK
- Gemini API Key

### Installation

1. Clone the repository:
git clone https://github.com/PariShahh/world-clock-agent.git

2. Create and activate a virtual environment:
conda create -n adk-env python=3.11
conda activate adk-env

3. Install dependencies:
pip install google-adk pytz timezonefinder geopy

4. Add your API key:
echo 'GOOGLE_API_KEY="YOUR_API_KEY"' > .env

5. Run the agent:
adk web --port 8000

6. Open your browser and go to:
http://127.0.0.1:8000

## 💬 Example Queries
- "What time is it in Mumbai?"
- "What's the current time in Tokyo?"
- "What time is it in New York?"
- "What time is it in London?"

## 📸 Demo
https://github.com/user-attachments/assets/f02c4346-4a0a-4702-b5ab-a479044d71ba

## 📝 License
This project is licensed under the MIT License.

## 🙋‍♀️ Author
**Pari Shah**  
[LinkedIn](https://www.linkedin.com/in/pari-shahh) | 
[GitHub](https://github.com/PariShahh)
