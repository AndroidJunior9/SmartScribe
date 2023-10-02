# SmartScribe

SmartScribe is a web application built with Flask, Python, HTML, CSS, and JavaScript that leverages the Nylas SDK and Hugging Face Text Summarization API to enhance your email inbox experience. This project is made for Nylas and AI: Email and Calendaring for the Future Hackthon

## Setting up Nylas in your project

#### Installing Nylas
```
pip install nylas
```
#### Install flask

```
pip install flask
```

#### Create a Virtual Environment

```
python<version> -m venv <virtual-environment-name>
```

```
source env/bin/activate
```

#### Making Nylas Client
```python
from flask import Flask, request, render_template, jsonify
from nylas import APIClient
from dotenv import load_dotenv
import os



load_dotenv()  # take environment variables from .env.

# You will get your client_id,client_secret, access_token from your nylas account

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
access_token = os.getenv("ACCESS_TOKEN")


nylas = APIClient(client_id, client_secret, access_token)
```

## Features  
* View and manage your emails directly from the web interface with the help of Nylas.  
* Summarize lengthy emails with a single click, saving you time and effort.  
* Powered by Hugging Face's state-of-the-art text summarization technology for accurate and concise email summaries.

## Note 
This app does not have authorization as hosted authorization needs you to subscribe to a paid plan. So you will need to provide it your access token as a environment variable.

## API Reference

#### HuggingFace Text Summarization API

```http
  https://api-inference.huggingface.co/models/facebook/bart-large-cnn
```

### Demo
```python
import json
import requests
API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
headers = {"Authorization": f"Bearer {API_TOKEN}"} #use your own api token you can get it from your hugging face account
def query(payload):
    data = json.dumps(payload)
    response = requests.request("POST", API_URL, headers=headers, data=data)
    return json.loads(response.content.decode("utf-8"))
#Note: You can access the summary by data[0]["summary_text"]
data = query("Add your text here...")
```
## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`API_KEY` for huggingFace(its also known as API_TOKEN so don't get confused)  
`CLIENT_ID`  
`CLIENT_TOKEN`  
`ACCES_TOKEN`

[Hugging Face]: https://huggingface.co/
[Nylas]: https://www.nylas.com/

## Links

Visit [Hugging Face] to check out their stunning ML/AI Models and their APIs.  
Learn more about email APIs at [Nylas].


