pipeline {
  agent any
  stages {
    stage('hello') {
      steps {
        bat 'C:/Python310/python.exe Tests/hello.py'
      }
    }
    stage('form_test'){
      steps {
        bat 'C:/Python310/python.exe Tests/form_test.py'
      }
    }
  }
}
