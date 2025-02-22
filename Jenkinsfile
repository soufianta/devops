pipeline {
    agent any  // Runs on any available agent
    stages {
        stage('Clone Repository') {
            steps {
                echo "cloning repo..."
            }
        }
        stage('test app from testing branch') {
            steps {
                echo "testing..."
            }
        }
        stage('Run Python Script') {
            steps {
                sh 'python3 -u app.py'  // Replace with the actual script name
            }
        }
    }
}
