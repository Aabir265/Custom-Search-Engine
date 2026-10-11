from flask import Flask, jsonify, render_template, request
from app import search_web
import requests
app = Flask(__name__, template_folder="." , static_folder=".", static_url_path="/")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search',methods=['GET', 'POST'])
def search():
    data = request.get_json()
    query = data.get('query', '').strip()

    if not query:
        return jsonify({"results": []})

    results = search_web(query)
    return jsonify({"results": results})

if __name__ == '__main__':
    app.run(debug=True)
    
