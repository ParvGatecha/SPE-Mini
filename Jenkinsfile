pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/your-repo/scientific-calculator.git'
            }
        }
        stage('Test') {
            steps {
                sh 'pytest test_main.py'
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t scientific-calculator .'
            }
        }
        stage('Push to Docker Hub') {
            steps {
                withDockerRegistry([credentialsId: 'docker-hub-creds', url: '']) {
                    sh 'docker tag scientific-calculator your-docker-hub/scientific-calculator'
                    sh 'docker push your-docker-hub/scientific-calculator'
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