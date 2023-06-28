def mainDir="wiprex"
def ecrLoginHelper="docker-credential-ecr-login"
// def region="<AWS Region>"
// def ecrUrl="<AWS ECR URL>"
// def deployHost="<Deploy VM Private IP>"
def repository="test"
def AWS_CREDENTIAL_NAME = "aws-key"

def IMAGE_NAME = ""
def REGION = ""
def DeployHost = ""

pipeline {
    agent any

    stages {
        stage('Pull Codes from Github'){
            steps{
                checkout scm
            }
        }
        stage('Build Image by docker') {
            steps {
                sh """
                docker build -t $IMAGE_NAME:$BUILD_NUMBER .
                docker tag $IMAGE_NAME:$BUILD_NUMBER $IMAGE_NAME:latest
                """
            }
        }
        stage('push image to aws ECR') {
            steps {
                sh """
                aws ecr get-login-password --region $REGION | docker login --username AWS --password-stdin $IMAGE_NAME
                docker push $IMAGE_NAME:latest
                """
            }
        }
        stage('pull image by aws ECR') {
            steps {
                sshagent(credentials : ["prod"]) {
                    sh "ssh -o StrictHostKeyChecking=no prod@$DeployHost \
                    ' ls; \
                    aws ecr get-login-password --region $REGION | docker login --username AWS --password-stdin $IMAGE_NAME; \
                    docker pull $IMAGE_NAME:latest; \
                    docker ps;'" 
                }
            }
        }

        // stage('pull image by aws ECR') {
        //     steps {
        //         sshagent(credentials : ["prod"]) {
        //             sh "ssh -o StrictHostKeyChecking=no prod@$DeployHost \
        //             'aws ecr get-login-password --region $REGION | docker login --username AWS --password-stdin $IMAGE_NAME; \
        //             docker pull $IMAGE_NAME:latest; \
        //             docker run --rm -d  -v /tmp/.X11-unix:/tmp/.X11-unix --name uitest $IMAGE_NAME:latest \
        //             docker ps'" 
        //         }
        //     }
        // }


    }
}
