from flask import Flask, request, render_template
from src.predict import prediction

app = Flask(__name__)

def get_tweet(sentence):
	res, score = prediction(sentence,"data/tweets.csv","model/d2v.model")
	tweets_block = ""
	
	for index in range(len(res)):
		tweets_block += "<tr id=" + str(index) + " > <td>" + str(index) + "</td> <td>" + res[index] + "</td> </tr>"

	return render_template('index.html', tweets=tweets_block)

@app.route('/', methods=['GET','POST'])
def index():
	if request.method == 'POST':
		output = request.form 
		return get_tweet(output['sentence'])

	return render_template('index.html')

if __name__ == '__main__':
	app.run(host='0.0.0.0')