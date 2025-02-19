pipeline {
    agent any

    environment {
        DOCKER_IMAGE_NAME = 'mediastream-hub'
        DOCKER_IMAGE_TAG = 'latest'
        DOCKERHUB_USERNAME = 'vaibhav411007'  // Replace with your Docker Hub username
        K8S_NAMESPACE = 'your-namespace'  // Update your namespace here
    }

    stages {
        stage('Declarative: Checkout SCM') {
            steps {
                checkout scm
            }
        }

        stage('Clone Repository') {
            steps {
                // Ensure you're using the correct branch
                git url: 'https://github.com/iamvaibhavsutar/mediastream.git', branch: 'main', credentialsId: 'your-credentials-id'  // Update 'your-credentials-id'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker build -t ${DOCKER_IMAGE_NAME}:${DOCKER_IMAGE_TAG} .'
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: 'dockerhub-credentials', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                        // Docker login using the credentials stored in Jenkins
                        sh 'echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin'

                        // Push the built Docker image to Docker Hub
                        sh 'docker push ${DOCKER_IMAGE_NAME}:${DOCKER_IMAGE_TAG}'
                    }
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                script {
                    withCredentials([file(credentialsId: 'k8s-kubeconfig', variable: 'KUBE_CONFIG')]) {
                        // Deploy to Kubernetes with the updated Docker image
                        sh 'kubectl --kubeconfig=$KUBE_CONFIG set image deployment/${DOCKER_IMAGE_NAME} ${DOCKER_IMAGE_NAME}=${DOCKER_IMAGE_NAME}:${DOCKER_IMAGE_TAG} --namespace=${K8S_NAMESPACE}'
                    }
                }
            }
        }
    }

    post {
        failure {
            echo 'Pipeline failed!'
        }
        success {
            echo 'Pipeline succeeded!'
        }
    }
}
