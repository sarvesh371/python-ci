// Global Variables
dockerImage = "python"

properties([
    buildDiscarder(logRotator(artifactDaysToKeepStr: '7', artifactNumToKeepStr: '500', daysToKeepStr: '7', numToKeepStr: '500')),
    parameters([
        string(defaultValue: 'Type What you want to print', description: "Input String", name: 'inputString'),
    ])
])

inputString = (params.inputString == null) ? 'Type What you want to print' : params.inputString.toString().trim().replaceAll('"', '')

node('master') {
    workspace = pwd()
    gitHash = sh(returnStdout: true, script: 'git rev-parse --short --verify HEAD').trim()
    // Run in Container using base network on Host
    sh "docker pull ${dockerImage}"
    withDockerContainer(args: '-v $workspace/:/root/:z --network=host', image: dockerImage) {
        docWorkSpace = pwd()
        withEnv(["PYTHONPATH=${docWorkSpace}", "HASH=${gitHash}"]) {
            stage('Get User') {
                sh "python3 -u learning.py --inputString=${inputString}"
            }
        }
    }
    sh "docker rmi ${dockerImage}"
}
