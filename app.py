from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


# @app.route('/output') 
# def output():
#       return render_template('output.html')

@app.route("/output", methods=['POST'])
def process():
    description = request.form['description']
    language = request.form['language']
    gender = request.form['gender']

#    return 'Name is: ' + name + ' and the comment is: ' + comment     # This line is also working, but def feunction can return only one task.
    return render_template('output.html', description=description, language=language, gender=gender)


if __name__ == '__main__':
	app.run(debug=True)