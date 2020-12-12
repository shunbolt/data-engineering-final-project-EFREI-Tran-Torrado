def build_app(){

}

def run_app(){
  sh 'nohup python webapp.py &'
}

def test_app(){
  sh 'python test_webapp.py'
}

def down_app(){
  sh 'process_flask_credit=`netstat -tulnp | grep :5000 | cut -c81-`
  sh 'process_id=`echo "$process_flask_credit" | tr -cd [:digit:]`'
  sh 'kill -9 $process_id' 
}

def release_app(){
}


return this
