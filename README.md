# Data engineering project - Final
### By Raphaël Tran & Yoann Torrado

### Requirements :
- Docker 
- docker-compose
- Selenium library to run the tests on your machine : `pip install selenium`
- Prometheus `https://prometheus.io/download/`
- Grafana `https://grafana.com/grafana/download`
- Locust to run stress test `pip install locust`

### Installation :
- `git clone https://github.com/shunbolt/data-engineering-final-project-EFREI-Tran-Torrado.git`
- `cd data-engineering-final-project-EFREI-Tran-Torrado`

### Starting the app :
- use `docker-compose up` to start the app 
- You can then access the webapp on `http://localhost:5000`

### Running tests  :
- `python test_webapp.py` to test the webapp
- `python model_test.py` to test the model 

If you have an issue regarding Geckodriver, you can follows these steps on a Unix/Ubuntu machine :

1. Download Geckodriver :

`wget https://github.com/mozilla/geckodriver/releases/download/v0.24.0/geckodriver-v0.24.0-linux64.tar.gz`

2. Extract it :

`tar -xvzf geckodriver*`

3. Give execution permissions :

`chmod +x geckodriver`

4. Move it to binaries directory :

`sudo mv geckodriver /usr/local/bin/`

### Running stress test :

- use `locust -f locustfile.py` to start the stress test UI
-  You can then access the locust UI on http://localhost:8089

### Running monitoring : 

- We launch Prometheus, Node_explorer and Grafana and then we can observe the dashboard into Grafana
