pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'mediastream-image'
        DOCKER_CONTAINER_NAME = 'mediastream-container'
        PORT = '9601'  // Updated port
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Build Docker Image') {
            steps {
                script {
                    sh '''
                    docker build -t $DOCKER_IMAGE .
                    '''
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    sh '''
                    sudo docker run -d -p $PORT:80 --name $DOCKER_CONTAINER_NAME $DOCKER_IMAGE
                    '''
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    // Add your test commands here
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    // Add your deploy commands here
                }
            }
        }

        stage('Cleanup') {
            steps {
                script {
                    sh 'sudo docker stop $DOCKER_CONTAINER_NAME'
                    sh 'sudo docker rm $DOCKER_CONTAINER_NAME'
                }
            }
        }
    }
}
