pipeline {
  agent any
  stages {
    stage('Clone Repository') {
      steps {
        echo 'cloning repo...'
      }
    }

    stage('test app from testing branch') {
      parallel {
        stage('test app from testing branch') {
          steps {
            echo 'testing...'
          }
        }

        stage('list repo content after checkout') {
          steps {
            sh 'ls'
          }
        }

      }
    }

    stage('Run Python Script') {
      steps {
        sh 'python3 app.py'
      }
    }

  }
}
