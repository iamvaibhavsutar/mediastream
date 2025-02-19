pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    sh 'sudo docker build -t mediastream-image .'
                }
            }
        }
        stage('Run Docker Container') {
            steps {
                script {
                    sh 'sudo docker run -d -p 9600:80 --name mediastream-container mediastream-image'
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    sh 'curl -f http://localhost:9600/health' // Adjust this URL as per your app
                }
            }
        }
        stage('Deploy') {
            steps {
                script {
                    // Example deployment using SSH or Kubernetes
                    // sh 'ssh user@production_server "docker run -d -p 9600:80 --name mediastream-container mediastream-image"'
                }
            }
        }
        stage('Cleanup') {
            steps {
                script {
                    sh 'sudo docker rm -f mediastream-container'
                    sh 'sudo docker rmi mediastream-image'
                }
            }
        }
    }
}
