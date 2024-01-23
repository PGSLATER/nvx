from flask import Flask, render_template, request
import os

app = Flask(__name__)

def get_content(path):
    content = []
    try:
        for item in os.listdir(path):
            full_path = os.path.join(path, item)
            if os.path.isdir(full_path):
                content.append({'name': item, 'type': 'folder'})
            else:
                content.append({'name': item, 'type': 'file'})
    except FileNotFoundError:
        # Handle the case where the directory does not exist
        pass
    return content

def normalize_path(path):
    # Convert backslashes to forward slashes for display in HTML
    return path.replace('\\', '/')

@app.route('/')
def index():
    base_path = os.path.expanduser("~")  # Set the base path to the user's home directory
    return render_template('index.html', current_path=normalize_path(base_path), content=get_content(base_path))

@app.route('/explore/<path:item_name>')
def explore(item_name):
    base_path = os.path.expanduser("~")
    current_path = request.args.get('current_path', base_path)
    current_path = os.path.join(current_path, item_name)
    current_path = normalize_path(current_path)

    content = get_content(current_path)
    return render_template('index.html', current_path=current_path, content=content)

@app.route('/goback')
def go_back():
    base_path = os.path.expanduser("~")
    current_path = request.args.get('current_path', base_path)
    parent_path = os.path.abspath(os.path.join(current_path, os.pardir))
    parent_path = normalize_path(parent_path)
    
    content = get_content(parent_path)
    return render_template('index.html', current_path=parent_path, content=content)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
