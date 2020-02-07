// Global Variables
dockerImage = "python"
gitRepo = "https://github.com/sarvesh371/ci-learning.git"

properties([
    buildDiscarder(logRotator(artifactDaysToKeepStr: '7', artifactNumToKeepStr: '500', daysToKeepStr: '7', numToKeepStr: '500')),
    parameters([
        string(defaultValue: 'Type What you want to print', description: "Input String", name: 'inputString'),
    ])
])

inputString = (params.inputString == null) ? 'Type What you want to print' : params.inputString.toString().trim().replaceAll('"', '')

node('master') {
    stage('Git-Clone') {
        checkout([
            $class: 'GitSCM',
            doGenerateSubmoduleConfigurations: false,
            branches: [[name: 'master']],
            extensions: [[$class: 'CleanBeforeCheckout']],
            userRemoteConfigs: [[credentialsId: 'sarveshsingh.03', url: gitRepo]]]
        )
    }
    workspace = pwd()
    currentBuild.result = "SUCCESS"
    sh "docker pull ${dockerImage}"
    withDockerContainer(args: '-v $workspace/:/root/:z --network=host', image: dockerImage) {
        gitHash = sh(returnStdout: true, script: 'git rev-parse --short --verify HEAD').trim()
        // Run in Container using base network on Host
        docWorkSpace = pwd()
        withEnv(["PYTHONPATH=${docWorkSpace}", "HASH=${gitHash}"]) {
            stage('Run Python Code') {
                sh "python3 -u learning.py --inputString=${inputString}"
            }
        }
    }
    sh "docker rmi ${dockerImage}"
}
