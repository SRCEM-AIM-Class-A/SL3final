pipeline {
    agent any

    environment {
        DOCKER_HUB_CREDS = credentials('docker-hub-credentials')
        FLASK_IMAGE = 'aman-asses/flask-app'
        DJANGO_IMAGE = 'aman-asses/django-app'
        // Add path to Docker commands for Windows
        DOCKER_PATH = isUnix() ? '' : 'docker'
        COMPOSE_PATH = isUnix() ? 'docker-compose' : 'docker-compose'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Images') {
            parallel {
                stage('Build Flask App') {
                    steps {
                        script {
                            dir('flask_app') {
                                bat(script: "${DOCKER_PATH} build -t ${FLASK_IMAGE}:${BUILD_NUMBER} .", returnStatus: true)
                                bat(script: "${DOCKER_PATH} tag ${FLASK_IMAGE}:${BUILD_NUMBER} ${FLASK_IMAGE}:latest", returnStatus: true)
                            }
                        }
                    }
                }

                stage('Build Django App') {
                    steps {
                        script {
                            dir('django_app') {
                                bat(script: "${DOCKER_PATH} build -t ${DJANGO_IMAGE}:${BUILD_NUMBER} .", returnStatus: true)
                                bat(script: "${DOCKER_PATH} tag ${DJANGO_IMAGE}:${BUILD_NUMBER} ${DJANGO_IMAGE}:latest", returnStatus: true)
                            }
                        }
                    }
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    try {
                        bat(script: "${COMPOSE_PATH} up -d", returnStatus: true)
                        // Wait for services to be ready
                        sleep(time: 30, unit: 'SECONDS')
                        
                        // Test Flask app
                        def flaskStatus = bat(script: 'curl -f http://localhost:5000', returnStatus: true)
                        if (flaskStatus != 0) {
                            error "Flask app test failed"
                        }
                        
                        // Test Django app
                        def djangoStatus = bat(script: 'curl -f http://localhost:8000', returnStatus: true)
                        if (djangoStatus != 0) {
                            error "Django app test failed"
                        }
                    } finally {
                        bat(script: "${COMPOSE_PATH} down", returnStatus: true)
                    }
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                        bat(script: "echo %DOCKER_PASS% | ${DOCKER_PATH} login -u %DOCKER_USER% --password-stdin", returnStatus: true)
                        
                        // Push Flask images
                        bat(script: "${DOCKER_PATH} push ${FLASK_IMAGE}:${BUILD_NUMBER}", returnStatus: true)
                        bat(script: "${DOCKER_PATH} push ${FLASK_IMAGE}:latest", returnStatus: true)
                        
                        // Push Django images
                        bat(script: "${DOCKER_PATH} push ${DJANGO_IMAGE}:${BUILD_NUMBER}", returnStatus: true)
                        bat(script: "${DOCKER_PATH} push ${DJANGO_IMAGE}:latest", returnStatus: true)
                        
                        bat(script: "${DOCKER_PATH} logout", returnStatus: true)
                    }
                }
            }
        }
    }

    post {
        always {
            script {
                // Clean up Docker images
                bat(script: "${DOCKER_PATH} system prune -f", returnStatus: true)
                cleanWs()
            }
        }
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed! Check the logs for details.'
        }
    }
} 