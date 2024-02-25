from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    # Define the path to your discussions.txt file
    file_path = '/Users/devinfico/Research/Coding/SPARK/class_project/discussions.txt'
    
    # Initialize the first discussion variable
    first_discussion = ''
    
    # Try to open and read the first discussion from the file
    try:
        with open(file_path, 'r') as file:
            first_discussion = file.readline().strip()  # Read the first line
    except Exception as e:
        first_discussion = f'Error reading file: {e}'
    
    # Render the template, passing the first discussion
    return render_template('index.html', first_discussion=first_discussion)

if __name__ == '__main__':
    app.run(debug=True)
