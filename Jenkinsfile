pipeline {
    agent any
    environment {
        DOCKER_IMAGE = "mohamedgamal10/app:$BUILD_NUMBER"
        PROJECT_ID = "core-avenue-438213-r8"
    }

    stages {
        stage('Pull Repository') {
            steps {
                echo 'Pulling the repository'
                sh 'git clone https://github.com/MohamedGamal10/Depi_Project.git'
            }
        }

        stage('Set Up Python Environment') {
            steps {
                echo 'Setting up Python virtual environment'
                script {

                    sh '''
                        cd app
                        python3 -m venv venv  
                        . venv/bin/activate 
                        pip install --upgrade pip 
                    '''
                }
            }
        }

        stage('Run Unit Tests') {
            steps {
                echo 'Running unit tests'
                script {
                    def testResult = sh(script: '''
                        cd app
                        . venv/bin/activate  
                        pip install -r requirements.txt
                        pytest -v test.py  # Run tests
                    ''', returnStatus: true)

                    if (testResult != 0) {
                        error("Unit tests failed")
                    }
                }
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
                        docker push ${USERNAME}/app:${BUILD_NUMBER}
                    '''   
                }
            }
        }

        stage('Deploy to GKE') {
            steps {
                echo 'Deploying to Google Kubernetes Engine'
                script {
                    withCredentials([file(credentialsId: 'gcloud-key', variable: 'GCLOUD_KEY')]) {
                        sh """
                        gcloud auth activate-service-account --key-file=${GCLOUD_KEY}
                        gcloud config set project ${PROJECT_ID}
                        
                        #Kubernates commands
                        gcloud container clusters get-credentials <CLUSTER_NAME> --zone <ZONE>
                        kubectl cluster-info
                        kubectl set image deployment/app app="mohamedgamal10/app:$BUILD_NUMBER"
                        kubectl rollout status deployment/app
                        """
                    }
                }
                
            }
        }
    }

    post {
        always {
            cleanWs()
        }
        success {
            echo 'Pipeline succeeded!'
            slackSend(channel: '#depidevopsproject', color: 'good', message: "Build SUCCESSFUL: ${env.JOB_NAME} #${env.BUILD_NUMBER} (<${env.BUILD_URL}|Open>)")
        }
        failure {
            echo 'Pipeline failed!'
             slackSend(channel: '#depidevopsproject', color: 'danger', message: "Build FAILED: ${env.JOB_NAME} #${env.BUILD_NUMBER} (<${env.BUILD_URL}|Open>)")
        }
    }
}
