#!flask/bin/python
import os
from flask import Flask, request, redirect, url_for

UPLOAD_FOLDER = 'temp_image_folder'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
@app.route('/index')
def index():
    return "Classifier API v1.0. Use classifier/api/v1.0/classifyImage to POST an image to the classifier"

@app.route('/classifier/api/v1.0/sampleFileUpload')
def fileUploadHtml():
    return '''<!doctype html>
        <title>Upload a picture</title>
        <h2>Upload a Picture</h2>
        <form method="POST" enctype=multipart/form-data action="http://localhost:5000/classifier/api/v1.0/classifyImage">
        <input type="file" name="file"/>
        <input type="submit" value="Upload"/>
        </form>
        </html>'''

@app.route('/classifier/api/v1.0/classifyImage', methods=['POST'])
def classifier():
	#1. The POST request should have a file - get it here. If no file sent, return
	#2. Save the file to a temp location and give it a unique name
	loc = upload_file(request)

	#3. Send the file to the classifier
	#4. JSONify the classifier's return string
	#    - Does the output need something else/more? Do it here
	#5. Delete the local file
	#	 - It's Hackathon but lets learn to clean after we're done
	return "You uploaded a file to test the classifier at " + os.path.abspath(loc)

def upload_file(request):
	if request.method == 'POST':
		if 'file' not in request.files:
			return redirect(request.url)
		file = request.files['file']
		if file.filename == '':
			return redirect(request.url)
		if file:
			loc = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
			file.save(loc)
			return loc
	return