pipeline {
    agent any
    environment {
        MYSQL_ROOT_PASSWORD=credentials('default-db-password')
        MYSQL_HOST="mysql"
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
                // mysql_id = sh(script:'docker run -d --rm --name mysql -p 3306:3306 --network="jenkins_default" -e MYSQL_ROOT_PASSWORD=$MYSQL_ROOT_PASSWORD mysql:8', returnStdout: true)
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
                timeout(10) {
                    waitUntil() {
                        script {
                            try {
                                sh 'docker exec mysql mysqladmin ping -h0.0.0.0 -uroot -ppassword'
                                return true
                            } catch (exception) {
                                return false
                            }
                        }
                    }
                }
                echo 'Run tests'
                sh 'pytest -v --cov-report=html --cov=script'

            }
        }
        
        stage('Publish HTML') {
            steps {
                publishHTML (target: [alwaysLinkToLastBuild:true, reportDir: 'htmlcov', reportName: "Test Reports", reportTitles: 'My HTML Report' ])
            }
        }
    }
    
    // post {
    //     always {
    //          echo "Remove sql container"
    //          sh 'docker compose down mysql'   
    //     }
    // }

}