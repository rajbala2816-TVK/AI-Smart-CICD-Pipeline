pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'Checking out source code...'
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Installing Python dependencies...'
                bat '"C:\\Users\\Lenovo\\AppData\\Local\\Programs\\Python\\Python312\\python.exe" -m pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running automated tests...'

                script {
                    def testResult = bat(
                        script: '"C:\\Users\\Lenovo\\AppData\\Local\\Programs\\Python\\Python312\\python.exe" -m pytest > jenkins_error.log 2>&1',
                        returnStatus: true
                    )

                    if (testResult != 0) {
                        echo 'Tests failed. AI Failure Analysis will be triggered.'
                        error('Automated tests failed.')
                    }
                }
            }
        }

        stage('Docker Build') {
            steps {
                echo 'Building Docker image...'
                bat '"C:\\Users\\Lenovo\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin\\docker.exe" build -t ai-smart-cicd .'
            }
        }

        stage('Docker Deploy') {
            steps {
                echo 'Deploying Docker container...'

                bat '"C:\\Users\\Lenovo\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin\\docker.exe" rm -f ai-smart-cicd-container || exit 0'

                bat '"C:\\Users\\Lenovo\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin\\docker.exe" run -d -p 5000:5000 --name ai-smart-cicd-container ai-smart-cicd'
            }
        }
    }

    post {

        success {
            echo 'CI/CD Pipeline completed successfully!'
        }

        failure {
            echo '========================================'
            echo 'AI FAILURE ANALYSIS'
            echo '========================================'

            bat '"C:\\Users\\Lenovo\\AppData\\Local\\Programs\\Python\\Python312\\python.exe" -c "from ai_failure_analyzer import analyze_failure; log=open(\'jenkins_error.log\', encoding=\'utf-8\', errors=\'ignore\').read(); result=analyze_failure(log); print(\'AI ERROR TYPE:\', result[\'error_type\']); print(\'POSSIBLE CAUSE:\', result[\'possible_cause\']); print(\'SUGGESTION:\', result[\'suggestion\'])"'
        }
    }
}