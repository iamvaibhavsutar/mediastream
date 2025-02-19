pipeline {
    agent any
    
    environment {
        DOCKER_IMAGE_NAME = 'mediastream-hub'
        DOCKER_IMAGE_TAG = 'latest'
        DOCKERHUB_USERNAME = 'your-dockerhub-username'
        DOCKERHUB_PASSWORD = 'your-dockerhub-password'
        K8S_NAMESPACE = 'your-namespace'
    }
    
    stages {
        stage('Declarative: Checkout SCM') {
            steps {
                checkout scm
            }
        }
        
        stage('Clone Repository') {
            steps {
                // Ensure you're cloning the correct repository
                git url: 'https://github.com/iamvaibhavsutar/mediastream.git', credentialsId: 'your-credentials-id'
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
                    withCredentials([usernamePassword(credentialsId: 'dockerhub-credentials', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                        sh 'echo $DOCKER_PASSWORD | docker login -u $DOCKER_USERNAME --password-stdin'
                        sh 'docker push ${DOCKER_IMAGE_NAME}:${DOCKER_IMAGE_TAG}'
                    }
                }
            }
        }
        
        stage('Deploy to Kubernetes') {
            steps {
                script {
                    withCredentials([file(credentialsId: 'k8s-kubeconfig', variable: 'KUBE_CONFIG')]) {
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
