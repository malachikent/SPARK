from flask import Flask  
from flask import render_template
from flaskwebgui import FlaskUI # import FlaskUI
from flask import request, jsonify
from pdf_parser import parse_pdf_sections
import tempfile
from flask import jsonify, url_for, session
import os

app = Flask(__name__)
app.secret_key = os.urandom(16)  # Generates a random key for the session

@app.route("/")
def hello():  
    return render_template('index.html')

@app.route("/home", methods=['GET'])
def home(): 
    return render_template('some_page.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    if file and file.filename.endswith('.pdf'):
        with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as temp:
            file.save(temp.name)
            parsed_sections = parse_pdf_sections(temp.name)
            session['parsed_sections'] = parsed_sections  # Store in session
        return jsonify({'redirect': url_for('report_edit_page')})
    else:
        return jsonify({'error': 'Invalid file type'}), 400
    
@app.route('/report_edit')
def report_edit_page():
    parsed_sections = session.get('parsed_sections', {})
    print("Parsed Sections:", parsed_sections)  # Debug print
    return render_template('report_edit.html', sections=parsed_sections)



if __name__ == "__main__":
  FlaskUI(app=app, server="flask").run()