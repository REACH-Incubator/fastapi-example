podTemplate(containers: [
    containerTemplate(name: 'python', image: 'python:3', ttyEnabled: true, command: 'cat')
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
    }
}
