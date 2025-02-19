pipeline {
    agent any
    
    environment {
        // Define Docker image names and tags for frontend and backend
        DOCKER_IMAGE_BACKEND = 'vaibhav411007/mediastream-backend'
        DOCKER_IMAGE_FRONTEND = 'vaibhav411007/mediastream-frontend'
        DOCKER_IMAGE_TAG = 'latest'
        
        // Kubernetes namespace for deployment
        K8S_NAMESPACE = 'default'  // Update with your actual namespace if different
    }
    
    stages {
        stage('Checkout Code') {
            steps {
                git url: 'https://github.com/iamvaibhavsutar/mediastream.git', branch: 'main', credentialsId: 'your-credentials-id'
            }
        }
        
        stage('Build Backend Docker Image') {
            steps {
                script {
                    // Build Docker image for the backend
                    sh 'docker build -t ${DOCKER_IMAGE_BACKEND}:${DOCKER_IMAGE_TAG} backend/'
                    sh 'docker tag ${DOCKER_IMAGE_BACKEND}:${DOCKER_IMAGE_TAG} ${DOCKER_IMAGE_BACKEND}:${DOCKER_IMAGE_TAG}'
                }
            }
        }
        
        stage('Build Frontend Docker Image') {
            steps {
                script {
                    // Build Docker image for the frontend
                    sh 'docker build -t ${DOCKER_IMAGE_FRONTEND}:${DOCKER_IMAGE_TAG} frontend/'
                    sh 'docker tag ${DOCKER_IMAGE_FRONTEND}:${DOCKER_IMAGE_TAG} ${DOCKER_IMAGE_FRONTEND}:${DOCKER_IMAGE_TAG}'
                }
            }
        }
        
        stage('Push Docker Images to Docker Hub') {
            steps {
                script {
                    // Push both backend and frontend Docker images to Docker Hub
                    withCredentials([usernamePassword(credentialsId: 'dockerhub-credentials', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                        sh 'echo $DOCKER_PASSWORD | docker login -u $DOCKER_USERNAME --password-stdin'
                        sh 'docker push ${DOCKER_IMAGE_BACKEND}:${DOCKER_IMAGE_TAG}'
                        sh 'docker push ${DOCKER_IMAGE_FRONTEND}:${DO
