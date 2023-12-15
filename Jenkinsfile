pipeline {
    agent {
        label 'master'
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
                sh 'docker compose up -d mysql'
            }
        }

        stage('Build script') {
            steps {
                timeout(2) {
                    waitUntil() {
                        sh 'docker compose up -d script'
                    }
                }
            }
        }

        stage('Run Tests') {
            steps {
                sh 'docker ps -a'
            }
        }


    }

}