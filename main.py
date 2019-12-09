from flask import current_app, render_template, send_file, request, Response
import connexion
import os

# Create the application instance
import config


# Get the application instance
app = config.connex_app

# Read the swagger.yml file to configure the endpoints
app.add_api("swagger.yml")

# Create a URL route in our application for "/"
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/favicon.ico')
def favicon():
    return send_file("templates/favicon.ico")

@app.route('/favicon-16x16.png')
def favicon16():
    return send_file("templates/favicon-16x16.png")

@app.route('/favicon-32x32.png')
def favicon32():
    return send_file("templates/favicon-32x32.png")

@app.route('/android-chrome-192x192.png')
def android_chrome192():
    return send_file("templates/android-chrome-192x192.png")

@app.route('/android-chrome-512x512.png')
def android_chrome512():
    return send_file("templates/android-chrome-512x512.png")

@app.route('/apple-touch-icon.png')
def apple_touch():
    return send_file("templates/apple-touch-icon.png")

@app.route('/browserconfig.xml')
def browserconfig():
    return send_file("templates/browserconfig.xml")

@app.route('/mstile-150x150.png')
def mstile():
    return send_file("templates/mstile-150x150.png")

@app.route('/safari-pinned-tab.svg')
def safari():
    return send_file("templates/safari-pinned-tab.svg")

@app.route('/site.webmanifest')
def site_webmanifest():
    return send_file("templates/site.webmanifest")

@app.route('/<path:path>')
def redirect(path):
    return render_template("index.html")

@app.route('/js/<path:path>')
def returnjs(path):
    return send_file("templates/js/"+ path)

@app.route('/css/<path:path>')
def returncss(path):
    return send_file("templates/css/"+ path)

@app.route('/img/<path:path>')
def returnimg(path):
    return send_file("templates/img/"+ path)

# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
