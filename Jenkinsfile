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
                docker build -t $IMAGE_NAME:$BUILD_NUMBER .
                docker tag $IMAGE_NAME:$BUILD_NUMBER $IMAGE_NAME:latest
                """
            }
        }
        stage('push image to aws ECR') {
            steps {
                sh """
                curl -O https://amazon-ecr-credential-helper-releases.s3.us-east-2.amazonaws.com/0.4.0/linux-amd64/${ecrLoginHelper}
                chmod +x ${ecrLoginHelper}
                mv ${ecrLoginHelper} /usr/local/bin/
                cd /usr/local/bin
                aws ecr get-login-password --region ${REGION} | docker login --username AWS --password-stdin ${IMAGE_NAME}'
                echo done2
                docker push $IMAGE_NAME:latest
                """
            }
        }
    }
}