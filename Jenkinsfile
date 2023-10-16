node {
    def app
    stage('Clone repository') {
        checkout scm
    }
    stage('Build image') {
        app = docker.build("lmldocker/markdownpy:1.1")
    }
    stage('Push image') {
        docker.withRegistry('https://registry.hub.docker.com', 'docker-hub-credentials') {
            app.push("1.1")
        }
    }
    stage('kubernetes run pod ') {
        steps {
            script {
                kubernetesDeploy(configs: "kubernetes-pod.yaml", "kubernetes-svc.yaml")
            }
        }
    }
}