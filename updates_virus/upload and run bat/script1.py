import os
import subprocess
from flask import Flask, render_template, request

app = Flask(__name__)

# Set the default upload folder
DEFAULT_UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = DEFAULT_UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the folder path from the form
        folder_path = request.form['folder_path']

        # Get the list of BAT files in the specified folder
        files = [file for file in os.listdir(folder_path) if file.endswith('.bat')]
        return render_template('contents.html', files=files, folder_path=folder_path, default_upload_folder=DEFAULT_UPLOAD_FOLDER)

    # Render the initial form
    return render_template('contents.html', files=None, folder_path=None, default_upload_folder=DEFAULT_UPLOAD_FOLDER)

@app.route('/upload', methods=['POST'])
def upload_file():
    # Check if the post request has the file part
    if 'file' not in request.files:
        return 'No file part'

    file = request.files['file']

    # If user does not select a file, browser also submits an empty part without a filename
    if file.filename == '':
        return 'No selected file'

    # Get the upload folder from the form field or use the default
    upload_folder = request.form.get('upload_folder', DEFAULT_UPLOAD_FOLDER)

    # Ensure the specified folder exists, create it if necessary
    upload_folder_path = os.path.join(app.root_path, upload_folder)
    os.makedirs(upload_folder_path, exist_ok=True)

    # Save the file to the specified folder
    file.save(os.path.join(upload_folder_path, file.filename))

    return 'File successfully uploaded to {}'.format(upload_folder)

@app.route('/run/<filename>', methods=['GET'])
def run_file(filename):
    # Get the folder path from the form
    folder_path = request.args.get('folder_path', default='.')

    # Construct the full path to the selected file
    file_path = os.path.join(folder_path, filename)

    try:
        # Use subprocess to run the file on the server
        subprocess.run(file_path, shell=True, check=True)
        message = f"File '{filename}' executed successfully."
    except Exception as e:
        message = f"Error executing file '{filename}': {str(e)}"

    # Display a message indicating the result
    return message

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
