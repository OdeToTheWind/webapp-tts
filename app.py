from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    languages = ['Hindi', 'English', 'Kannada', 'Telugu']
    genders = ['Male', 'Female']
    return render_template('index.html', languages=languages, genders=genders)
    
        

@app.route("/output", methods=['POST'])
def process():
    description = request.form['description']
    language = request.form.get('language')
    gender = request.form.get('gender')

    # please save the audio file in the form of "/home/pghosh/Documents/CODES/OPEN-DAY/TTS_Sathvikwebapp/webapp_tts/static/assets/temp.wav"#

    return render_template('output.html', description=description, language=language, gender=gender)  #passing the test, language, gender and dir of generated audio


if __name__ == '__main__':
	app.run(debug=True)