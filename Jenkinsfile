pipeline {
    agent any  // Runs on any available agent
    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/soufianta/devops.git'
            }
        }
        stage('Run Python Script') {
            steps {
                sh 'python3 app.py'  // Replace with the actual script name
            }
        }
    }
}