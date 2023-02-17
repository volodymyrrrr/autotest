pipeline {
    agent any
    stages {
        stage('version') {
            steps {
                sh 'python --version'
                }
            }
            stage('hello') {
            steps {
                sh 'python form_test.py'
                }
            }
        }
    }