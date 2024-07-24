from flask import Flask, render_template, request, send_from_directory, redirect, url_for
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        directory = request.form['directory']
        return redirect(url_for('upload', directory=directory))
    else:
        directory = request.args.get('directory')
        if not os.path.isdir(directory):
            return 'Not a valid directory'
        
        images = [f for f in os.listdir(directory) if f.lower().endswith(('png', 'jpg', 'jpeg', 'gif', 'bmp'))]
        images_with_text = []
        
        for image in images:
            text_file = os.path.splitext(image)[0] + '.txt'
            text_path = os.path.join(directory, text_file)
            if os.path.isfile(text_path):
                with open(text_path, 'r') as file:
                    text_content = file.read()
            else:
                text_content = ''
                with open(text_path, 'w') as file:
                    file.write(text_content)
            
            images_with_text.append((image, text_content))
        
        return render_template('gallery.html', images_with_text=images_with_text, directory=directory)

@app.route('/save', methods=['POST'])
def save():
    directory = request.form['directory']
    for key in request.form:
        if key.startswith('text_'):
            image = key[len('text_'):]
            text_content = request.form[key]
            text_file = os.path.splitext(image)[0] + '.txt'
            text_path = os.path.join(directory, text_file)
            with open(text_path, 'w') as file:
                file.write(text_content)
    return redirect(url_for('upload', directory=directory))

@app.route('/images/<path:filename>')
def images(filename):
    directory = request.args.get('directory')
    return send_from_directory(directory, filename)

if __name__ == '__main__':
    app.run(debug=True)
