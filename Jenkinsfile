pipeline {
  agent any

  stages {
    stage('Build') {
        steps {
          echo 'Building'
        }
      }
      stage('Test') {
        steps {
          withPythonEnv('test_env/bin'){
            bash 'python --version'
            bash 'pip install -r requirements.txt'
            bash 'pytest --junitxml=./tests/results.xml'
          }
        }
      }
      stage('Deploy') {
        steps {
          echo 'Deploying'
        }
      }
    }
  post {
    always {
      echo 'This will always run'
      junit 'tests/*.xml'
    }
    success {
      echo 'This will run only if successful'
    }
    failure {
      echo 'This will run only if failed'
    }
    unstable {
      echo 'This will run only if the run was marked as unstable'
    }
    changed {
      echo 'This will run only if the state of the Pipeline has changed'
      echo 'For example, if the Pipeline was previously failing but is now successful'
    }
  }
}
