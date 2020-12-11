from flask import Flask, request, render_template

app = Flask(__name__)

def get_tweet(sentence):
	index = 1
	if sentence == 'election':
		tw = "This election is in my favor !"
	elif sentence == 'fraud':
		tw = "My opponent is a fraud !"
	else:
		tw = "Loser !"

	block = "<tr id=" + str(index) + " > <td>" + str(index) + "</td> <td>" + tw + "</td> </tr>"
	return render_template('index.html', tweets=block)

@app.route('/', methods=['GET','POST'])
def index():
	if request.method == 'POST':
		output = request.form 
		return get_tweet(output['sentence'])

	return render_template('index.html')

if __name__ == '__main__':
	app.run(host='0.0.0.0')