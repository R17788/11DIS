from flask import Flask, render_template

app = Flask(__name__)
app.config["SECRET_KEY"] = 'myverysecretkey'  # used as session cookies can be encrypted


@app.route('/')
@app.route('/<name>')
def index():
    # if name:
    #     return "Welcome " + name
    # else:
        return 'Hello everyone '
        #return message
        #return render_template('index.html', data=message)


if __name__ == '__main__':
    host = '127.0.0.1'
    port = 5000
    app.run(host, port, debug=True)

