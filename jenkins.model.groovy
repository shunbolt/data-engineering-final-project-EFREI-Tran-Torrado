def build_app(){
  sh 'python import_nltk.py'
}

def run_app(){
}

def test_app(){
  sh 'python model_test.py'
}

def down_app(){
}

def release_app(){
}


return this
