from flask import Flask, request, jsonify
from flask_cors import CORS
from transformers import pipeline

app = Flask(__name__)
CORS(app)

summarizer = pipeline("summarization", model='facebook/bart-large-cnn')
#A major issue was the titles were not catchy enough or felt like an extract out of the summary
#The solution was to import a seperate pipeline for generating the title
title_generator = pipeline("text2text-generation", model="czearing/article-title-generator")

@app.route('/summarize', methods=['POST'])
def summarize():
    text = request.json.get('text', '')
    
    if len(text.split()) < 30:
        return jsonify({'error': 'Text too short, please enter at least 30 words.'})
    
    summary= summarizer(text, min_length=20, max_length=130)[0]['summary_text']
    key_points= [s.strip() for s in summary.split('.') if s.strip()]
    title = title_generator(summary, max_length=10)[0]['generated_text']
    
    return jsonify({
        'summary': summary,
        'key_points': key_points,
        'title': title
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)