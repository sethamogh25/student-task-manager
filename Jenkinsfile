pipeline {
    agent any

    environment {
        DOCKER_CREDENTIALS = 'dockerhub-creds'
        DOCKER_IMAGE = 'amoghseth25/student-task-manager'
        K8S_DEPLOYMENT = 'student-task-manager'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies and Test') {
    steps {
        sh '''
            python3 -m venv .venv
            .venv/bin/python -m pip install --upgrade pip
            .venv/bin/python -m pip install -r requirements.txt
            .venv/bin/python -m py_compile app.py
            .venv/bin/python -m pytest -v
        '''
    }
}

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t ${DOCKER_IMAGE}:${BUILD_NUMBER} .'
                sh 'docker tag ${DOCKER_IMAGE}:${BUILD_NUMBER} ${DOCKER_IMAGE}:latest'
            }
        }

        stage('Push Docker Image') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: "${DOCKER_CREDENTIALS}",
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_TOKEN'
                )]) {
                    sh '''
                        echo "$DOCKER_TOKEN" | docker login -u "$DOCKER_USER" --password-stdin
                        docker push ${DOCKER_IMAGE}:${BUILD_NUMBER}
                        docker push ${DOCKER_IMAGE}:latest
                        docker logout
                    '''
                }
            }
        }

        stage('Deploy to Minikube') {
            steps {
                sh '''
                    kubectl --kubeconfig=/var/lib/jenkins/.kube/config \
                        set image deployment/${K8S_DEPLOYMENT} \
    student-task-manager=${DOCKER_IMAGE}:${BUILD_NUMBER}
                    kubectl --kubeconfig=/var/lib/jenkins/.kube/config \
                        rollout status deployment/${K8S_DEPLOYMENT} --timeout=120s
                '''
            }
        }
    }

    post {
        success {
            echo 'CI/CD pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Check the Jenkins console output.'
        }
    }
}
