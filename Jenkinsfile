// def mainDir="Chapter02/2-jenkins-docker"
// def ecrLoginHelper="docker-credential-ecr-login"
// def region="<AWS Region>"
// def ecrUrl="<AWS ECR URL>"
// def repository="<Image Repository Name>"
// def deployHost="<Deploy VM Private IP>"

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
                docker build -t test -f ./Dockerfile.
                """
            }
        }
        // stage('Build Docker Image by Jib & Push to AWS ECR Repository') {
        //     steps {
        //         withAWS(region:"${region}", credentials:"aws-key") {
        //             ecrLogin()
        //             sh """
        //                 curl -O https://amazon-ecr-credential-helper-releases.s3.us-east-2.amazonaws.com/0.4.0/linux-amd64/${ecrLoginHelper}
        //                 chmod +x ${ecrLoginHelper}
        //                 mv ${ecrLoginHelper} /usr/local/bin/
        //                 cd ${mainDir}
        //                 ./gradlew jib -Djib.to.image=${ecrUrl}/${repository}:${currentBuild.number} -Djib.console='plain'
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