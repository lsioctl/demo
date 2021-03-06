pipeline {
    agent {
        label 'master'
    }
    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                sh 'pwd'
                sh 'ls'
                sh "docker build -t lsioctl/myapp:${env.BUILD_NUMBER} ."
            }
        }
        stage('JavaBuild') {
            agent { docker { image 'maven:3-alpine' } }
            steps {
                echo 'Building..'
                sh 'pwd'
                sh 'mvn --version'
            }
        }
        stage('Test') {
            agent { docker { image "lsioctl/myapp:${env.BUILD_NUMBER}" } }
            steps {
                echo 'Testing..'
                sh 'pwd'
                sh 'ls'
                sh 'cd /app; python test.py'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
                sh "docker tag lsioctl/myapp:${env.BUILD_NUMBER} lsioctl/myapp:latest"
                ansiblePlaybook( 
                    playbook: 'deploy/playbook.yml',
                    inventory: 'deploy/site.yml')
            }
        }
    }
}
