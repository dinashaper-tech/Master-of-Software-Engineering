from flask import Flask, request, send_from_directory
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

#home page
@app.route('/')
def home():
    return '''
        <h3>Hello!</h3>
        <a href= "/upload"> Click here to upload an image</a>
        '''

#upload image
@app.route('/upload')
def upload_form():
    return '''
        <h3> Upload an image</h3>
        <form method= "POST" action="/show" enctype="multipart/form-data">
            <input type="file" name="image">
            <input type="submit" value="Upload">
        </form>  
   '''

#show image
@app.route('/show', methods=['POST'])
def show_image():
    file = request.files['image']
    if file.filename == '':
        return ' No file selected.'
    
    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    return f'''
        <h3>Image Uploaded!</h3>
        <img src = "/uploads/{file.filename}" width="300">
        <br>
        <a href = "/"> Back to Home<a>
    '''

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

if __name__ == '__main__':
    app.run(debug=True)