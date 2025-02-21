pipeline {
    agent any  // Runs on any available agent
    stages {
        stage('Clone Repository') {
            steps {
                echo "cloning repo..."
            }
        }
        stage('Run Python Script') {
            steps {
                sh 'python3 app.py'  // Replace with the actual script name
            }
        }
    }
}