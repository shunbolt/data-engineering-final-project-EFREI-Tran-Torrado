def build_app(){
  
}

def run_app(){
  sh 'nohup python webapp.py &'
}

def test_app(){
  sh 'python test_webapp.py'
}

def down_app(){
  sh './kill_flask_process.sh'
}

def release_app(){
}


return this