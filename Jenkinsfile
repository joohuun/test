def mainDir="wiprex"
def ecrLoginHelper="docker-credential-ecr-login"
// def region="<AWS Region>"
// def ecrUrl="<AWS ECR URL>"
// def deployHost="<Deploy VM Private IP>"
def repository="test"

def AWS_CREDENTIAL_NAME = "aws-key"
def ECR_PATH = "541062409049.dkr.ecr.ap-northeast-2.amazonaws.com"
def IMAGE_NAME = "541062409049.dkr.ecr.ap-northeast-2.amazonaws.com/test"
def REGION = "ap-northeast-2"


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
                echo 1단계
                docker build -t test .
                docker tag test zjstl2:latest
                """
            }
        }
        // stage('push image to aws ECR') {
        //     steps {
        //         sh """
        //         aws ecr get-login-password --region $REGION | docker login --username AWS --password-stdin $IMAGE_NAME
        //         docker push $IMAGE_NAME:latest
        //         """
        //     }
        // }
        // stage('pull image by aws ECR') {
        //     steps {
        //         sh """
        //         docker pull $IMAGE_NAME:latest
        //         docker run --rm -d  -v /tmp/.X11-unix:/tmp/.X11-unix --name uitest $IMAGE_NAME:latest
        //         """
        //     }
        // }
    }
}