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
                sh '''#!/bin/bash
                sudo docker build -t mediastream-image .
                '''
            }
        }
        stage('Run Docker Container') {
            steps {
                sh '''#!/bin/bash
                sudo docker run -d -p 9600:80 --name mediastream-container mediastream-image
                '''
            }
        }
        stage('Test') {
            steps {
                sh '''#!/bin/bash
                curl -f http://localhost:9600/health
                '''
            }
        }
        stage('Deploy') {
            steps {
                // Add deployment steps as needed
                // Example:
                // sh "ssh user@production_server 'docker run -d -p 9600:80 --name mediastream-container mediastream-image'"
            }
        }
        stage('Cleanup') {
            steps {
                sh '''#!/bin/bash
                sudo docker rm -f mediastream-container
                sudo docker rmi mediastream-image
                '''
            }
        }
    }
}
