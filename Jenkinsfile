pipeline {

    environment {
        dockerimagename = "lmldocker/markdownpy"
        dockerImage = ""
    }

    agent any

    stages {

        stage('Clone git repository') {
            steps {
                script {
                    checkout scm
                }
            }
        }
        stage('Build container image') {
            steps {
                script {
                    dockerImage = docker.build("lmldocker/markdownpy:1.1")
                }
            }
        }
        stage('Push container image to public registry') {
            steps {
                script {
                    docker.withRegistry('https://registry.hub.docker.com', 'docker-hub-credentials') {
                        dockerImage.push("1.1")
                    }
                }
            }
        }
        stage('kubernetes deploy') {
            steps {
                script {
                    /*kubernetesDeploy(configs: "kubernetes-pod.yaml")*/
                    sh 'kubectl apply -f kubernetes-pod.yaml'
                }
            }
        }
        stage('kubernetes expose service') {
            steps {
                script {
                    /*kubernetesDeploy(configs: "kubernetes-svc.yaml")*/
                    sh 'kubectl apply -f kubernetes-svc.yaml'
                }
            }
        }

    }

}