from flask import Flask, render_template, request, jsonify
from service import initialize_qa

app = Flask(__name__, static_folder='static')
qa_instance = None

def initialize_qa_if_needed():
    global qa_instance
    if qa_instance is None:
        qa_instance = initialize_qa()

@app.route('/', methods=['GET', 'POST'])
def index():
    initialize_qa_if_needed()
    if request.method == 'POST':
        query = request.form['query']
        res = qa_instance(query)
        answer = res['result']
        return jsonify({'answer': answer})  # Return JSON response
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
