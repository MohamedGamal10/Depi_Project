pipeline {
    agent any
    environment {
        DOCKER_IMAGE = "mohamedgamal10/app:$BUILD_NUMBER"
    }

    stages {
        stage('Pull Repository') {
            steps {
                echo 'Pulling the repository'
                 sh '''
                    git clone https://github.com/MohamedGamal10/Depi_Project.git
                    '''
            }
        }

        stage('Run Unit Tests') {
            steps {
                echo 'Running unit tests'
            }
        }

        stage('Build Docker Image & Push to Docker Hub') {
            steps {
                echo 'Building Docker image and pushing to Docker Hub'
                withCredentials([usernamePassword(credentialsId: 'docker_cred', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
                        sh '''
                        cd Depi_Project/app
                        docker build -t ${USERNAME}/app:${BUILD_NUMBER} .
                        echo "${PASSWORD}" | docker login -u "${USERNAME}" --password-stdin
                        docker push ${USERNAME}/my-react-app:${BUILD_NUMBER}
                        '''   
                    }
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
