# EdAsh - A Simple NLM-based Text Summarizer
EdAsh is a text summarizer that utilises a zero-shot natural language model to parse long articles into a simple summary, provide key points for quick reads, and suggests potential titles for your own personal writeup.

# Tech Stack
- Runtime: Python 3.11
- Language: Python
- Frontend: HTML + CSS 
- Backend: Flask
- AI Service:
    Hugging Face Transformer pipeline
        - Summariser Model: 'facebook/bart-large-cnn'
        - Title Generator Model: 'czearing/article-title-generator'
- HTTP Client: Fetch API
- Hosting: Localhost

## Quick Start

### Prerequisites
- Python v3.11.9
- Transformers v4.40.0 (Recent v5.5 dev builds do not support the pipelines in this project)
- flask (Backend API) 
- flask-cors (Frontend - Backend communication)
- torch - communicates with transformers to run language models.

## Installation Guide

### Install Pythin v3.11.9
1. Go to [Python Installer](https://www.python.org/ftp/python/3.11.9/python-3.11.9-amd64.exe)
2. Run the installer
3. Ensure the "Add Python to PATH" is checked before install
4. Verify using 'python --version'

### Clone the Repository 
```
git clone https://github.com/your-username/edme-summarybot.git
cd edme-summarybot
```
### Install the Python packages
```
py -3.11 -m pip install transformers flask flask-cors torch
```
### Run the frontend and backend code
```
py -3.11 summarybot-backend.py
```
I noticed this process was long during the first load as the models had to be loaded. However for future runs, this process is much faster.
After it shows "model running-"
```
start summarybot-frontend.html
```

### Ready to use!
A pop-up will be shown with the text summarizer

## Development Challenges
- The first major hurdle was choosing the right APIs and models. I opted for NLMs rather than LLMs as they are free, run natively on your local device and fairly easy to plug into web development environments.
- Version control is the primary reason why this project requires a stable build of python. Unfortunately with recent versions of Python, Hugging Face transformers face installation issues mostly with recognising the summariser model. Simply, Python's 3.13 incompatibility with tokenizers pre-built wheels forcing a downgrade to 3.11.
- the "transformers_repo" folder was initially titled "transformers" which caused an override with the installed package. 

## Fixes for future builds
### Revamping Data Presentation methods
Achieving a clean, readable UI was challenging as the original vision was a chatbot-style interface, which was scaled back due to time constraints.

Due to time constraints, this project works closer to a summary generator. For future versions the following could be improvements:
- Using an LLM such as Anthropic's Claude or OpenAI's API for providing better summaries and realistic titles.
- Revamping the UI stylisation. Users would be able to communicate directly with a chatbot
- Access previously generated summaries on the device storage.
- Ability to add PDFs, Word documents or other text related documents.

## Sources
Learning how to use hugging face models and understanding API's would not be possible without these articles
[Setting up text summarizers by Heiko Hotz](https://medium.com/data-science/setting-up-a-text-summarisation-project-daae41a1aaa3)









