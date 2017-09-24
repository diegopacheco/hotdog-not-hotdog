# Copyright 2015 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START app]



from __future__ import print_function # In python 2.7
import sys


import logging
import os, glob
from flask import Flask, request, redirect, url_for, render_template, flash, session
from werkzeug.utils import secure_filename
from google.cloud import storage
import pdb
import runner


app = Flask(__name__)
# app.secret_key = os.urandom(19)

app.debug = True


if not app.debug:

    # Do this as it's production
    # Configure this environment variable via app.yaml
    CLOUD_STORAGE_BUCKET = os.environ['CLOUD_STORAGE_BUCKET']
else:    
    script_dir = os.path.dirname(__file__)
    UPLOAD_FOLDER  = os.path.join(os.path.join(script_dir,r'static'),r'upload')
    app.config['UPLOAD_FOLDER']  = UPLOAD_FOLDER


    
    





@app.route('/foo', methods=['POST'])
def foo():
    """Process the uploaded file and upload it to Google Cloud Storage."""
    uploaded_file = request.files.get('file')
    file = request.files['file']
    if not uploaded_file:
        return redirect(url_for('index')) 
        # return 'No file uploaded.', 400

    if not app.debug:

        # Create a Cloud Storage client.
        gcs = storage.Client()

        # Get the bucket that the file will be uploaded to.
        bucket = gcs.get_bucket(CLOUD_STORAGE_BUCKET)

        # Create a new blob and upload the file's content.
        blob = bucket.blob(uploaded_file.filename)

        blob.upload_from_string(
            uploaded_file.read(),
            content_type=uploaded_file.content_type
        )
        
        file_perma_url = blob.public_url
        #Process the file and calculate the result
    else:
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        file_perma_url = os.path.join(app.config['UPLOAD_FOLDER'], filename)

    # print(uploaded_file, file=sys.stderr)
    # pdb.set_trace()
    result_dict = runner.start_main_process(file_perma_url)
    print(result_dict, file=sys.stderr)
    if (result_dict['hotdog'] > result_dict['nothotdog']):
        result = "Hotdog!"
    else:
        result = "Not hotdog!"

    print(result, file=sys.stderr)


    return render_template('foo.html',  messages={'main':result, 'second':file_perma_url })

    # list_of_files = glob.glob(UPLOAD_FOLDER+'/*')
    # latest_file = max(list_of_files, key=os.path.getctime)
    # try:
    #     image_loc = session['file_location']
    #     print(image_loc, file=sys.stderr)
    # except:
    #     image_loc = ''
    # result = 'Hotdog!'
    
    # if (image_loc == ''):
    #     return redirect(url_for('index')) 
    # else:

'''<!doctype html>
<title>Hello from Flask</title>
<h1>Hello World!</h1>
<img src="latest_file">

'''

@app.route('/')
def index():
    # if request.method == 'POST':
    #     # check if the post request has the file part
    #     if 'file' not in request.files:
    #         flash('No file part')
    #         return redirect(request.url)
    #     file = request.files['file']
    #     # if user does not select file, browser also
    #     # submit a empty part without filename
    #     if file.filename == '':
    #         flash('No selected file')
    #         return redirect(request.url)
    #     if file and allowed_file(file.filename):
    #         filename = secure_filename(file.filename)
    #         file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    #         # return redirect(url_for('uploaded_file',filename=filename))
    #         file1 = os.path.join(UPLOAD_FOLDER,filename)
    #         session['file_location'] = file1
    #         return redirect(url_for('foo'))
    return render_template('home.html')



def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # return redirect(url_for('uploaded_file',filename=filename))
            
            return redirect(url_for('foo'))

    # if request.method == 'GET':
    #     return redirect(url_for('foo'))

    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''

#testing stuff



@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


if __name__ == '__main__':
    # This is used when running locally. Gunicorn is used to run the
    # application on Google App Engine. See entrypoint in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END app]
