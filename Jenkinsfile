node {
    def app
    stage('Clone git repository') {
        checkout scm
    }
    stage('Build container image') {
        app = docker.build("lmldocker/markdownpy:1.1")
    }
    stage('Push container image to public registry') {
        docker.withRegistry('https://registry.hub.docker.com', 'docker-hub-credentials') {
            app.push("1.1")
        }
    }
    stage('kubernetes deploy') {
        steps {
            script {
                kubernetesDeploy(configs: "kubernetes-pod.yaml")
            }
        }
    }
    stage('kubernetes expose service') {
        steps {
            script {
                kubernetesDeploy(configs: "kubernetes-svc.yaml")
            }
        }
    }

}