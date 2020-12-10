def build_app(){
   echo 'Build and run done through docker-compose'
}

def run_app(){
   sh 'docker-compose up -d'
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
