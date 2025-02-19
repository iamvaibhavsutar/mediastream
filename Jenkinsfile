pipeline {
    agent any
    
    environment {
        DOCKER_IMAGE_NAME = 'vaibhav411007/mediastream-hub'
        DOCKER_IMAGE_TAG = 'latest'
        K8S_NAMESPACE = 'default'  // Update with your actual namespace if different
    }
    
    stages {
        stage('Checkout Code') {
            steps {
                git url: 'https://github.com/iamvaibhavsutar/mediastream.git', branch: 'main', credentialsId: 'your-credentials-id'
            }
        }
        
        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker build -t ${DOCKER_IMAGE_NAME}:${DOCKER_IMAGE_TAG} .'
                    sh 'docker tag ${DOCKER_IMAGE_NAME}:${DOCKER_IMAGE_TAG} ${DOCKER_IMAGE_NAME}:${DOCKER_IMAGE_TAG}'
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
                        sh 'kubectl --kubeconfig=$KUBE_CONFIG set image deployment/mediastream-hub mediastream-hub=${DOCKER_IMAGE_NAME}:${DOCKER_IMAGE_TAG} --namespace=${K8S_NAMESPACE}'
                    }
                }
            }
        }
    }
    
    post {
        failure {
            echo '❌ Pipeline failed!'
        }
        success {
            echo '✅ Pipeline succeeded!'
        }
    }
}
