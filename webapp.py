from flask import Flask, request, render_template
from src.predict import prediction
import time
from prometheus_client import start_http_server
from prometheus_client import Counter
from prometheus_client import Summary

REQUESTS = Counter('flask_twitter_webapp_calls_total', 'Number of calls')
LATENCY = Summary('flask_twitter_webapp_latency_seconds', 'Time needed for a request for the home page')
LATENCY_SEARCH = Summary('flask_twitter_webapp_search_latency_seconds', 'Time needed for a search request')

app = Flask(__name__)

def get_tweet(sentence,start):
	
	tweets_block = ""
	if sentence:
		res, score = prediction(sentence,"data/tweets.csv","model/d2v.model")
		for index in range(len(res)):
			tweets_block += "<tr id=" + str(index) + " > <td>" + str(index) + "</td> <td>" + res[index] + "</td> </tr>"

	LATENCY_SEARCH.observe(time.time() - start)
	return render_template('index.html', tweets=tweets_block)

@app.route('/', methods=['GET','POST'])
def index():
	REQUESTS.inc()
	start = time.time()
	if request.method == 'POST':
		output = request.form 
		return get_tweet(output['sentence'],start)

	LATENCY.observe(time.time() - start)

	return render_template('index.html')

if __name__ == '__main__':
	start_http_server(8010)
	app.run(host='0.0.0.0')