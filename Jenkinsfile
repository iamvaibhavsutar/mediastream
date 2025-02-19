pipeline {
    agent any
    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/your-repo/mediastream-hub.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t your-dockerhub-username/mediastream-hub:latest .'
            }
        }
        stage('Push to Docker Hub') {
            steps {
                sh 'docker login -u your-dockerhub-username -p your-password'
                sh 'docker push your-dockerhub-username/mediastream-hub:latest'
            }
        }
        stage('Deploy to Kubernetes') {
            steps {
                sh 'kubectl apply -f k8s/deployment.yaml'
            }
        }
    }
}

