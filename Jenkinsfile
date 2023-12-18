pipeline {
    agent any
    environment {
        MYSQL_ROOT_PASSWORD=credentials('default-db-password')
        MYSQL_HOST='0.0.0.0'
        MYSQL_USER=credentials('lesson28-mysql-username')
        MYSQL_PASSWORD=credentials('lesson28-mysql-password')
        registry = 'pathetic/db_creator'
    }

    stages {

        stage('Checkout') {

            steps {
                git branch: 'jenkins-branch', url: 'https://github.com/Houeta/repo_25'
            }
        }

        stage("Prepare environment for tests") {
            steps {
                echo "Start mysql service"
                sh 'docker run -d --rm --name mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=$MYSQL_ROOT_PASSWORD mysql:8'
                echo 'Install dependencies'
                sh '''
                apt-get update
                apt-get install python3 python3-pip -y
                python3 -m pip install mysql-connector-python pytest pytest-cov --break-system-packages

                '''
            }
        }

        stage('Test') {
            steps {
                echo 'Wait until mysql service is up'
                timeout(2) {
                    waitUntil() {
                        catchError {
                            sh(script:'docker exec mysql mysqladmin ping -h0.0.0.0 -uroot -ppassword',
                                returnStatus:true)
                        }
                    }
                }
                echo 'Run tests'
                sh 'pytest -v --cov-report=html --cov=script'

            }
        }
    }
    
    post {
        always {
             echo "Remove sql container"
             sh 'docker rm -f mysql'   
        }
    }

}