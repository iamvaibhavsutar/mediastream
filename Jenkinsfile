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
                    // Build Docker image
                    sh "sudo docker build -t mediastream-image ."
                }
            }
        }
        stage('Run Docker Container') {
            steps {
                script {
                    // Run the Docker container
                    sh "sudo docker run -d -p 9600:80 --name mediastream-container mediastream-image"
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    // Test the application
                    sh "curl -f http://localhost:9600/health"
                }
            }
        }
        stage('Deploy') {
            steps {
                script {
                    // Example deployment command
                    // sh "ssh user@production_server 'docker run -d -p 9600:80 --name mediastream-container mediastream-image'"
                }
            }
        }
        stage('Cleanup') {
            steps {
                script {
                    // Clean up the resources
                    sh "sudo docker rm -f mediastream-container"
                    sh "sudo docker rmi mediastream-image"
                }
            }
        }
    }
}
