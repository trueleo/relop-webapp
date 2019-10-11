from flask import current_app, render_template, send_file
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
    app.run(host='0.0.0.0', port=5000, debug=True)
