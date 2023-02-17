pipeline {
  agent any
  stages {
    stage('form_test') {
      steps {
        bat 'C:/Python310/python.exe Tests/form_test.py'
      }
    }
    stage('run') {
      steps {
        pysh 'C:/Python310/python.exe Tests/form_test.py'
      }
    }
  }
}
