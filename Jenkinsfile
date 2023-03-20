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
                docker build -t $IMAGE_NAME:$BUILD_NUMBER .
                docker tag $IMAGE_NAME:$BUILD_NUMBER $IMAGE_NAME:latest
                """
            }
        }
        stage('push image to aws ECR') {
            steps {
                sh """
                aws ecr get-login-password --region ${REGION} | docker login --username AWS --password-stdin ${IMAGE_NAME}'
                docker push $IMAGE_NAME:latest
                """
            }
        }
        stage('pull image from aws ECR')
            steps(
                sh """
                docker pull $IMAGE_NAME:latest
                docker run --rm -d  -v /tmp/.X11-unix:/tmp/.X11-unix --name uitest $IMAGE_NAME:latest
                """
            )

        // stage('Build Docker Image & Push to AWS ECR Repository') {
        //     steps {
        //         withAWS(region:"${region}", credentials:"aws-key") {
        //             ecrLogin()
        //             sh """
        //                 curl -O https://amazon-ecr-credential-helper-releases.s3.us-east-2.amazonaws.com/0.4.0/linux-amd64/${ecrLoginHelper}
        //                 chmod +x ${ecrLoginHelper}
        //                 mv ${ecrLoginHelper} /usr/local/bin/

        //             """
        //         }
        //     }
        // }
        // stage('Deploy to AWS EC2 VM'){
        //     steps{
        //         sshagent(credentials : ["deploy-key"]) {
        //             sh "ssh -o StrictHostKeyChecking=no ubuntu@${deployHost} \
        //              'aws ecr get-login-password --region ${region} | docker login --username AWS --password-stdin ${ecrUrl}/${repository}; \
        //               docker run -d -p 80:8080 -t ${ecrUrl}/${repository}:${currentBuild.number};'"
        //         }
        //     }
        // }
    }
}