pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                script {
                    // Cloning the repository
                    checkout scm
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build Docker image from Dockerfile
                    sh 'docker build -t mediastream-image .'
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    // Run the container
                    sh 'docker run -d -p 9600:8000 mediastream-image'
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    // Run tests or any other tasks here
                    echo "Run tests here"
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    // Deploy to your environment, e.g., AWS, Kubernetes, etc.
                    echo "Deploying the app..."
                }
            }
        }
    }

    post {
        always {
            // Clean up after the pipeline is done
            echo "Cleaning up..."
        }

        success {
            echo "Pipeline completed successfully!"
        }

        failure {
            echo "Pipeline failed!"
        }
    }
}
