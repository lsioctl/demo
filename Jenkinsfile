pipeline {
    agent any 
    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                sh 'python -V' 
            }
        }
        stage('Test') {
            agent { docker { image 'python:3' } }
            steps {
                echo 'Testing..'
		sh 'python test.py'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
                sh 'python -V'
            }
        }
    }
}
