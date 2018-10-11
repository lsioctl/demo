pipeline {
    agent {
        label 'master'
    } 
    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                sh 'pwd' 
            }
        }
        stage('Test') {
            agent { docker { image 'python:3' } }
            steps {
                echo 'Testing..'
                sh 'pwd' 
		sh 'python test.py'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
                sh 'pwd' 
            }
        }
    }
}
