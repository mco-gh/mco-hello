from flask import Flask, request, escape, render_template
import random

# To build docker in the local directory use the following and pass a name to call for run
# docker build --tag name . 
# If no name passed then not the pid and use that to run
# Run with 
# docker run -d -p 8080:8080 [name or id]
# Stop
# docker stop [id - first 4]

app = Flask(__name__)

# Fix for the load.io token - ?
#   http.HandleFunc("/"+token+"/", sendToken)
# def send_token(request) 
#   token = "loaderio-b1563d0e1a489bdfd2b21cc76d9b3c22"
#   w.Write([]byte(token))


@app.route('/', methods=['POST', 'GET'])
@app.route('/<name>', methods=['POST', 'GET'])
def say_hello(name='World'):
  num = random.randint(1,1000)

  # if request:
  #   request_json = request.get_json(silent=True)
  #   request_args = request.args
  #   if request_json and 'name' in request_json:
  #       name = request_json['name']
  #       print(request_json)
  #   elif request_args and 'name' in request_args:
  #       name = request_args['name']
  #       print(request_args)
  # print(request)


  color = random.randint(1,16777215)
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

#   if err := http.ListenAndServe(":8080", nil); err != nil 
#     panic(err)
  

if __name__ == '__main__':

    # option 2
    # app.add_url_rule('/say_hello', 'say_hello', say_hello, methods=['POST', 'GET'], defaults={'request': request})

    app.run(host='0.0.0.0', port=8080, use_reloader=True, debug=True)

