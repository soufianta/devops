pipeline {
    agent {label 'jenkins_agent'}
    stages {
        stage('Clone Repository') {
            steps {
                echo "cloning repo..."
            }
        }
        stage('testing') {
            steps {
                echo "testing..."
            }
        }
        stage('Run Python Script') {
            steps {
                sh 'python3 app.py'  // Replace with the actual script name
            }
        }
    }
}