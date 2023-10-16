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
            /*app.push("${env.BUILD_NUMBER}")*/
            /*app.push("latest")*/
            app.push("lmldocker/markdownpy:1.1")
        }
    }
    
}