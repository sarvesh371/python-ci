// Global Variables
gitRepo = 'https://github.com/sarvesh371/ci-learning.git'
dockerImage = "python"
gitBranch = 'master'

node('master') {
    workspace = pwd()
    gitHash = sh(returnStdout: true, script: 'git rev-parse --short --verify HEAD').trim()
    // Run in Container using base network on Host
    sh "docker pull ${dockerImage}"
    withDockerContainer(args: '-v $workspace/:/root/:z --network=host', image: dockerImage) {
        docWorkSpace = pwd()
        withEnv(["PYTHONPATH=${docWorkSpace}", "HASH=${gitHash}"]) {
            stage('Get User') {
                sh "python3 -u learning.py"
            }

        }
    }
    docker rmi Image python
}
