pipeline {
    agent any

    stages {
        stage('Pull Repository') {
            steps {
                echo 'Pulling the repository'
            }
        }

        stage('Run Unit Tests') {
            steps {
                echo 'Running unit tests'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image'
            }
        }

        stage('Push to Docker Hub') {
            steps {
                echo 'Pushing Docker image to Docker Hub'
            }
        }

        stage('Deploy to GKE') {
            steps {
                echo 'Deploying to Google Kubernetes Engine'

            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}
