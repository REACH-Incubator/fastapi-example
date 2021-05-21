podTemplate(containers: [
    containerTemplate(name: 'python', image: 'python:3', ttyEnabled: true, command: 'cat'),
    containerTemplate(
        name: 'docker', 
        image: 'docker', 
        ttyEnabled: true, 
        command: 'cat', 
        envVars: [
            secretEnvVar(key: 'DOCKERHUB_USER', secretName: 'memaldi-dockerhub', secretKey: 'username'),
            secretEnvVar(key: 'DOCKERHUB_PASSWORD', secretName: 'memaldi-dockerhub', secretKey: 'password')
        ]),
]) {
    
    node(POD_LABEL) {
        stage('Test FastAPI project') {
            git branch: 'jenkins', url: 'https://github.com/REACH-Incubator/fastapi-example'
            container('python') {
                stage('Run tests') {
                    sh 'pip install -r requirements.txt'
                    sh 'pytest'
                }
            }
        }

        stage('Build and Push Docker image') {
            git branch: 'jenkins', url: 'https://github.com/REACH-Incubator/fastapi-example'
            container('docker') {
                sh 'export GIT_COMMIT=$(git rev-parse --verify HEAD)'
                sh 'docker build -t reachincubator/fastapi-example:${GIT_COMMIT} .'
                sh 'docker login ${DOCKERHUB_USER} ${DOCKERHUB_PASSWORD}'
                sh 'docker push reachincubator/fastapi-example:${GIT_COMMIT}'
            }
        }
    }
}
