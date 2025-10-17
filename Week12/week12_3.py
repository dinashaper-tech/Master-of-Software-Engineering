from flask import Flask, request, send_from_directory
import os


app = Flask(__name__)


UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route('/')
def home():
    return '''
        <div style="text-align:center; margin-top:50px; font-family:Arial;">
            <h2 style="color:#2E8B57;">Welcome to the Image Uploader! (Using Flask)</h2>
            <p>Click the link below to upload your image </p>
            <a href="/upload" 
               style="text-decoration:none; background-color:#4CAF50; color:white; padding:10px 20px; border-radius:8px;">
               Upload Image
            </a>
        </div>
    '''

@app.route('/upload')
def upload_form():
    return '''
        <div style="text-align:center; margin-top:50px; font-family:Arial;">
            <h3 style="color:#0066cc;">Upload an Image</h3>
            <form method="POST" action="/show" enctype="multipart/form-data"
                  style="display:inline-block; background-color:#f2f2f2; padding:20px; border-radius:10px;">
                <input type="file" name="image" style="margin:10px;"><br>
                <input type="submit" value="Upload" 
                       style="background-color:#4CAF50; color:white; border:none; padding:8px 16px; border-radius:5px;">
            </form>
            <br><br>
            <a href="/" style="text-decoration:none; color:#555;">← Back to Home</a>
        </div>
    '''


@app.route('/show', methods=['POST'])
def show_image():
    file = request.files['image']
    if file.filename == '':
        return '''
            <div style="text-align:center; margin-top:50px; font-family:Arial; color:red;">
                <h3>No file selected.</h3>
                <a href="/upload" style="color:#0066cc;">Try Again</a>
            </div>
        '''

    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    return f'''
        <div style="text-align:center; margin-top:40px; font-family:Arial;">
            <h3 style="color:#2E8B57;">Image Uploaded Successfully!</h3>
            <img src="/uploads/{file.filename}" width="300" style="border-radius:10px; box-shadow:2px 2px 10px gray;"><br><br>
            <a href="/" 
               style="text-decoration:none; background-color:#4CAF50; color:white; padding:8px 16px; border-radius:5px;">
               Back to Home
            </a>
        </div>
    '''


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)


if __name__ == '__main__':
    app.run(debug=True)
