from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)       
app.config['DEBUG'] = True  

form = """
<!DOCTYPE html>
<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
        <form action="/" method="POST">
            <label for="rot">Rotate by: </label>
            <input type="text" name="rot" value="0"/>
            <textarea name="text"></textarea>
            <input type="submit" value="Submit Query" />
        </form>
    </body>
</html>
"""

@app.route("/") #render the form
def index():                
    return form

@app.route("/", methods=['POST'])
def encrypt():
    user_text = request.form["text"]
    user_rot = int(request.form["rot"])
    encrypted = '<h1>'
    encrypted += rotate_string(user_text, user_rot)
    encrypted += '</h1>'

    #encrypted = '<h1>' + rotate_string(user_text, user_rot) + '</h1>'

    return encrypted

app.run()