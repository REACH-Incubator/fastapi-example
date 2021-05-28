pipeline {
    agent {
        kubernetes {
            yaml """
apiVersion: v1
kind: Pod
spec:
  containers:
  - name: python
    image: python:3
    command:
    - cat
    tty: true
  - name: docker
    image: docker:latest
    command:
    - cat
    tty: true
    volumeMounts:
    - mountPath: /var/run/docker.sock
      name: docker-sock
    env:
    - name: DOCKERHUB_USER
      valueFrom:
          secretKeyRef:
            name: memaldi-dockerhub
            key: DOCKERHUB_USER
    - name: DOCKERHUB_PASSWORD
      valueFrom:
          secretKeyRef:
            name: memaldi-dockerhub
            key: DOCKERHUB_PASSWORD 
  volumes:
  - name: docker-sock
    hostPath:
      path: /var/run/docker.sock
"""
        }
    }
    stages {
        stage('Test FastAPI project') {
            steps {
                git branch: 'jenkins', url: 'https://github.com/REACH-Incubator/fastapi-example'
                container('python') {
                    sh 'pip install -r requirements.txt'
                    sh 'pytest'
                }
            }
        }
        stage('Build and Push Docker image') {
            steps {
                git branch: 'jenkins', url: 'https://github.com/REACH-Incubator/fastapi-example'
                container('docker') {
                    sh 'docker build -t reachincubator/fastapi-example:$BUILD_NUMBER .'
                    sh 'docker login -u ${DOCKERHUB_USER} -p ${DOCKERHUB_PASSWORD}'
                    sh 'docker push reachincubator/fastapi-example:$BUILD_NUMBER'
                }
            }
        }
        stage('Deploy FastAPI at Kubernetes') {
            steps {
                git branch: 'jenkins', url: 'https://github.com/REACH-Incubator/fastapi-example'
                script {
                    kubernetesDeploy(
                        configs: "kubernetes/deployment.yaml", 
                        kubeconfigId: "kubeconfig-rancher",
                        enableConfigSubstitution: true)
                }        
            }
        }
    }
}