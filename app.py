"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/

This file creates your application.
"""

import os
from flask import Flask, render_template, request, redirect, url_for

import pandas as pd
flickr_df = pd.read_pickle( 'data/flickr_df.pickle')

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'this_should_be_configured')


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""

    # create context and default values
    context = {}
    context['tagName'] = 'tagname'

    # tag name
    if 'tagName' in request.args.keys():
        context['tagName'] = request.args['tagName']

    # mturk/hit specific values
    if 'hitId' in request.args.keys():
        context['hitId'] = request.args['hitId']
    if 'assignmentId' in request.args.keys():
        context['assignmentId'] = request.args['assignmentId']
    if 'workerId' in request.args.keys():
        context['workerId'] = request.args['workerId']
    if 'turkSubmitTo' in request.args.keys():
        context['turkSubmitTo'] = request.args['turkSubmitTo'] + '/mturk/externalSubmit'

    # get the imgId url argument
    imgIds = ''
    if 'imgIds' in request.args.keys():
        imgIds = request.args['imgIds']
    imgIds = imgIds.split( ',' )

    # select from the dataframe
    selectImgs = flickr_df.loc[ imgIds ]

    # create the list of dictionaries corresponding to the selected row entries
    imgList = [ { 'id' : imgid, 'url' : row.image_url }
                for imgid, row in selectImgs.iterrows() ]
    context['imageList'] = imgList

    # add the table as well
    context['table'] = selectImgs.to_html()

    return render_template('home.html', **context )


# @app.route('/about/')
# def about():
#     """Render the website's about page."""
#     return render_template('about.html')


###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=600'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)
