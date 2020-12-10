def build_app(){
  sh 'docker build -t webapp .'
}

def run_app(){
   sh 'docker-compose up'
}

def test_app(){
  echo 'docker branch does not perform unit or integration tests'
}

def down_app(){
  sh 'docker-compose down'
}

def release_app(){
   echo 'docker branch not subject to release'
}



return this