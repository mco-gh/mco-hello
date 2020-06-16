from flask import Flask, request, escape, render_template
from werkzeug.exceptions import HTTPException, BadRequest

import random

'''
Notes on how to run locally:

To build docker in the local directory use the following and pass a name to call for run:
docker build --tag name . 

If no name passed then note the pid and use that to run:
docker run -d -p 8080:8080 [name or id]

Stop the instance with:
docker stop [id - first 4]

Deploy to registry
'''
app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
@app.route('/<name>', methods=['POST', 'GET'])
def say_hello(name='World'):

  color = "%06x" % random.randint(0, 0xFFFFFF)
  style = "style=\"background-color:#" + str(color) + "\""
  combined_html = "<h1 " + style + ">Hello " + name + "!!!</h1>"

  # Option to simply return hello
  # return 'Hello {}!'.format(escape(name))
  # Option passes the generated html to the page
  return combined_html

@app.errorhandler(404)
def not_found(error):
  return """<h1> 404 </h1>"""

  #Option to use template 
  #return render_template('home.hml')

@app.errorhandler(BadRequest)
def handle_bad_request(e):
    return 'bad request!', 400

@app.errorhandler(HTTPException)
def handle_exception(e):
    """Return JSON instead of HTML for HTTP errors."""
    # start with the correct headers and status code from the error
    response = e.get_response()
    # replace the body with JSON
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description,
    })
    response.content_type = "application/json"
    return response

if __name__ == '__main__':
    # Use when running locally
    #app.run(host='0.0.0.0', use_reloader=True, debug=True)

  app.run(host='0.0.0.0',port=8080, use_reloader=True, debug=True, threaded=True)