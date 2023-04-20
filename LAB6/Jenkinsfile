pipeline {
     environment {
          registry = "iraxus/maven-docker-test"
          DOCKERHUB_CREDENTIALS = credentials('docker-login-pwd')
      }
     agent none
    options {
        skipStagesAfterUnstable()
    }
    stages {

        stage('Testing') {
            agent{
            docker {
                        image 'maven:3.8.6-amazoncorretto-17'
                        args '-u root:root'
                        args '-v /var/run/docker.sock:/var/run/docker.sock'
                        args '-w /app'
                    }
             }
            steps {
                echo 'Testing'
                sh 'mvn test'
                echo 'Testing done'
            }
        }
        stage('Mvn clean install') {
            agent{
                  docker {
                          image 'maven:3.8.6-amazoncorretto-17'
                          args '-u root:root'
                          args '-v /var/run/docker.sock:/var/run/docker.sock'
                          args '-w /app'
                         }
                  }
            steps {
                echo 'Building jar'
                sh 'mvn clean install'
                echo 'Building jar done'
            }
        }

        stage('Build Docker Image and Push') {
            agent {
                    docker {
                        image 'mmiotkug/node-curl'
                        args '-p 3000:3000'
                        args '-w /app'
                        args '-v /var/run/docker.sock:/var/run/docker.sock'
                    }
                }
            steps {
                    echo 'Building Docker Image'
                    sh 'docker image build -t $registry:$BUILD_NUMBER .'
                    echo 'Logging into DockerHub'
                    sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u iraxus --password-stdin'
                    echo 'Pushing Docker Image'
                    sh 'docker image push $registry:$BUILD_NUMBER'
                    echo 'Pushed Docker Image'
                    sh "docker image rm $registry:$BUILD_NUMBER"
                 }
        }

        stage('Remove unused images') {
            agent {
                    docker {
                        image 'mmiotkug/node-curl'
                        args '-p 3000:3000'
                        args '-w /app'
                        args '-v /var/run/docker.sock:/var/run/docker.sock'
                    }
                }
            steps {
                    echo 'Removing unused images'
                    sh 'docker image prune --force'
                    echo 'Removed unused images complete'
                 }
        }
    }
}