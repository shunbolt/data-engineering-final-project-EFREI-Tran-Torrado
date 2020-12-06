pipeline {
  agent any
  stages {
    stage('Build docker image') {
      steps {
        sh 'docker stop $(docker ps -a -q)'
        sh 'docker rm $(docker ps -a -q)'
        sh 'docker build -t webapp .'
      }
    }

    stage('Run docker image') {
      steps {
        sh 'docker run -d -p 5000:5000 --name twitter webapp'
      }
    }

    stage('Remove docker container') {
      steps {
        sh 'docker stop twitter'
        sh '''docker rm -f twitter

'''
      }
    }

    stage('Remove docker image') {
      steps {
        sh 'docker rmi -f webapp'
      }
    }

  }
}