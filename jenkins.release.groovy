def build_app(){
  sh 'python import_nltk.py'
}

def run_app(){
  sh 'nohup python webapp.py &'
}

def test_model(){
  sh 'python model_test.py'
}

def test_web(){
  sh 'python test_webapp.py'
}

def test_app(){
  test_model()
  test_web()
}

def down_app(){
  sh './kill_flask_process.sh'
}

def release_app(){
	echo "Ready to be published on master branch"
}


return this