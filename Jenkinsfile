pipeline {
  agent any

  stages {
    stage('Build') {
        steps {
          bash 'source /Users/avi/Library/Python/3.8/bin/virtualenvwrapper.sh'
          bash 'python --version'
          bash '#!/bin/bash workon hello-world'
          bash 'python --version'
        }
      }
      stage('Test') {
        steps {
          bash 'pytest --junitxml=./tests/results.xml'
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
