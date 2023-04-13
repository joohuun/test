def mainDir="wiprex"
def ecrLoginHelper="docker-credential-ecr-login"
// def region="<AWS Region>"
// def ecrUrl="<AWS ECR URL>"
// def deployHost="<Deploy VM Private IP>"
def repository="test"
def AWS_CREDENTIAL_NAME = "aws-key"
// def ECR_PATH = "541062409049.dkr.ecr.ap-northeast-2.amazonaws.com"
def IMAGE_NAME = "577561256345.dkr.ecr.ap-northeast-2.amazonaws.com/juhoon-test"
def REGION = "ap-northeast-2"
def DeployHost = "10.10.1.251"

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
                    'aws ecr get-login-password --region $REGION | docker login --username AWS --password-stdin $IMAGE_NAME; \
                    docker pull $IMAGE_NAME:latest; \
                    docker run --rm -d  -v /tmp/.X11-unix:/tmp/.X11-unix --name uitest $IMAGE_NAME:latest \
                    docker ps'" 
                }
            }
        }

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