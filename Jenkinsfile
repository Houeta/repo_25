pipeline {
    agent {
        docker {
            image 'python:alpine'
            args '-v "/var/run/docker.sock:/var/run/docker.sock" -v "/usr/bin/docker:/usr/bin/docker"'
        }
    }

    environment {
        MYSQL_ROOT_PASSWORD=credentials('default-db-password')
        MYSQL_HOST='localhost'
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

        stage('Test') {
            agent {
                docker {
                    image 'mysql:latest'
                    args '--name mysql -e MYSQL_ROOT_PASSWORD=$MYSQL_ROOT_PASSWORD -d'
                }
            }
            steps {
                echo 'Install dependencies'
                sh 'pip install mysql-connector-python pytest pytest-cov'
                echo 'Run tests'
                sh 'pytest -v --cov-report=html --cov=script'
            }
        }
    }

}