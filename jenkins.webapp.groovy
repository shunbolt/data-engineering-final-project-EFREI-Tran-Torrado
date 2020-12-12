def build_app(){
  sh 'echo whoami'
}

def run_app(){
  sh 'nohup python webapp.py'
}

def test_app(){
  sh 'python test_webapp.py'
}

def down_app(){

}

def release_app(){
}


return this