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
                    // Explicitly invoke the shell command
                    sh '''#!/bin/bash
                    sudo docker build -t mediastream-image .
                    '''
                }
            }
        }
        stage('Run Docker Container') {
            steps {
                script {
                    // Run the Docker container
                    sh '''#!/bin/bash
                    sudo docker run -d -p 9600:80 --name mediastream-container mediastream-image
                    '''
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    // Test the application
                    sh '''#!/bin/bash
                    curl -f http://localhost:9600/health
                    '''
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
                    sh '''#!/bin/bash
                    sudo docker rm -f mediastream-container
                    sudo docker rmi mediastream-image
                    '''
                }
            }
        }
    }
}
