pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: "https://github.com/ParvGatecha/SPE-Mini.git"
            }
        }
        stage('Test') {
            steps {
                sh 'pytest test.py'
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t parvg/scientific-calculator .'
            }
        }
        stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials', usernameVariable: 'DOCKERHUB_USERNAME', passwordVariable: 'DOCKERHUB_PASSWORD')]) {
                    sh 'echo $DOCKERHUB_PASSWORD | docker login -u $DOCKERHUB_USERNAME --password-stdin'
                    sh 'docker parvg/scientific-calculator'
                }
            }
        }
        stage('Deploy with Ansible') {
            steps {
                sh 'ansible-playbook -i inventory deploy.yml'
            }
        }
    }
}