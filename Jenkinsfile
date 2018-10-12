pipeline {
    agent {
        label 'master'
    }
    stages {
        // this is automatically done when pipeline from scm
        stage ('git'){
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/master']],
                userRemoteConfigs: [[url: 'http://github.com/lsioctl/demo.git']]])
            }
        }
        stage('Build') {
            steps {
                echo 'Building..'
                sh 'pwd'
                sh 'ls'
                sh "docker build -t lsioctl/myapp:${env.BUILD_NUMBER} ."
            }
        }
        stage('Test') {
            agent { docker { image "lsioctl/myapp:${env.BUILD_NUMBER}" } }
            steps {
                echo 'Testing..'
                sh 'python test.py'
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
