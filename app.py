from flask import Flask, request, render_template, jsonify
from nylas import APIClient
from dotenv import load_dotenv
import os
from transformers import pipeline
import requests
import json


load_dotenv()  # take environment variables from .env.

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
api_token = os.getenv("API_TOKEN")
API_URL = os.getenv("API_URL")
headers = {"Authorization": f"Bearer {api_token}"}
app = Flask(__name__)





nylas = APIClient(client_id, client_secret, access_token)

@app.route('/')
def index():
    return render_template('index.html')



@app.route('/get_emails', methods=['GET'])
def get_emails():
    # Get the first 5 messages in the inbox
    messages = nylas.messages.all(limit=5)

    # Extract the ID, subject, and body of each message
    emails = [{'id': message.id, 'subject': message.subject, 'body': message.body} for message in messages]


    return jsonify(emails)

@app.route('/display_email', methods=['GET'])
def display_email():
    # Get the ID of the email from the query parameters
    id = request.args.get('id')

    # Retrieve the email using the provided ID
    email = nylas.messages.get(id)

    # Render a new page to display the email
    return render_template('display_email.html', subject=email.subject, body=email.body)



from bs4 import BeautifulSoup

@app.route('/summarize_email', methods=['GET'])
def summarize_email():
    # Get the text to summarize from the request data
    id = request.args.get('id')

    # Retrieve the email using the provided ID
    email = nylas.messages.get(id)

    # Parse the HTML content of the email
    soup = BeautifulSoup(email.body, 'html.parser')

    # Extract the text from the HTML
    text = soup.get_text()

    # Send a POST request to the Hugging Face API
    data = json.dumps({"inputs": text})
    response = requests.request("POST", API_URL, headers=headers, data=data)

    # Return the summarized text
    return json.loads(response.content.decode("utf-8"))








if __name__ == '__main__':
    app.run(debug=True)
