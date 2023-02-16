from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)


# API endpoint for the OpenAI API
api_endpoint = "https://api.openai.com/v1/engines/text-davinci-002/jobs"

# API Key for the OpenAI API
api_key ='api key'

@app.route('/')
def index():
    return render_template('index.html')


# Connect to the mysql database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    # passwd="your_mysql_password_here",
    database="strokes"
)
cursor = conn.cursor()

# Send a request to the OpenAI API
def send_request(text):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    data = {
        "prompt": text,
        "max_tokens": 100,
        "temperature": 0.5,
    }
    response = requests.post(api_endpoint, headers=headers, json=data)
    return response.json()

# Retrieve data from the mysql database
def retrieve_data(query):
    cursor.execute(query)
    return cursor.fetchall()

# Example usage
# text = "What is the capital of France?"
# response = send_request(text)
# answer = response["choices"][0]["text"]
# print(answer)

#get query from frontend


result = retrieve_data(query)
print(result)


if __name__ == '__main__':
    app.run(debug=True)