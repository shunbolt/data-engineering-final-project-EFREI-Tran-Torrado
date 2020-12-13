def build_app(){
   echo 'Build and run done through docker-compose'
}

def run_app(){
   sh 'docker-compose up -d --build'
}

def test_web(){
  sh 'python test_webapp.py'
}

def test_app(){
  test_web()
}

def down_app(){
  sh 'docker-compose down'
}

def release_app(){
   echo 'docker branch not subject to release'
}


return this
