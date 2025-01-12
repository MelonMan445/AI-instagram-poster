AI Instagram Poster
---
This program allows you to automatically generate and post AI-generated content (images and captions) directly to your Instagram account based on a user-provided prompt.

Features
---
AI-Powered Content Creation: Generates both an image and a caption based on the prompt you provide.
Automated Instagram Posting: Posts the generated content directly to your Instagram account.
Customizable: Feel free to modify the code for your specific needs or integrate it into larger projects.
Requirements

To run this bot, you'll need to install the following Python packages:
---
- Pillow: Python Imaging Library (PIL) fork for image processing.
- Instabot: A Python library for automating Instagram tasks.
- Requests: For making HTTP requests.
- google-generativeai: For accessing Google's Gemini AI model for image and caption generation.
pip install Pillow instabot requests google-generativeai

Setting Up
---
- Get a Google Gemini API key from Google AI Studio. https://aistudio.google.com/app/apikey
- Create a new project and select the gemini-1.5-flash model (or any model you prefer).

---
API_KEY = "" #add you google gemini ai api key 

---
model = genai.GenerativeModel("") #select the model you are using

---
- go into the code and replace with right info^

Running the Bot
---
run aiposter.py to start the code
Follow the on-screen prompts to log in to your Instagram account and create a new post using AI-generated content.

Customization
---
You can modify the code to:

Change the AI model used for content generation. Adjust how the generated content is formatted or displayed.

---
Feel free to use this script as-is, customize it, or integrate it into larger projects. You can modify or distribute the code under your preferred terms, but make sure to comply with the usage rules of the libraries and APIs involved.
