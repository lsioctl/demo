pipeline {
    agent any 
    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                sh 'uname -a' 
            }
        }
        stage('Test') {
            agent { docker { image 'python:3' } }
            steps {
                echo 'Testing..'
                sh 'uname -a' 
		sh 'python test.py'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
                sh 'uname -a' 
            }
        }
    }
}
