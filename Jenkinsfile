pipeline {
    agent {
        label 'python docker'
    }

    environment {
        ROOT_PASSWORD=credentials('default-db-password')
        MYSQL_HOST=credentials('lesson28-mysql-host')
        MYSQL_USER=credentials('lesson28-mysql-username')
        MYSQL_PASSWORD=credentials('lesson28-mysql-password')

    }

    stages {

        stage('Start mysql') {
            steps {
                echo 'MySQL was started'
                sh 'docker-compose up -d mysql'
            }
        }

        stage('Install dependencies') {
            steps {
                sh 'pip install mysql-connector-python pytest pytest-cov'
                }
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest -v --cov-report=html --cov=script'
            }
        }


    }

}