pipeline {
    agent {
        node {
            label "dev01"
        }
    }
    tools {
        jdk 'jdk8'
    }



    stages {
        // ************************
        // *** DEPLOYMENT STAGE ***
        // ************************

        // ***** ELK Deployment *****
        stage("DMHT Deployment"){
            steps{
                withCredentials([file(credentialsId: 'test-vaggelis-file', variable: 'vaggelis'),
                   file(credentialsId: 'test-panos-file', variable: 'panos')]) {
                       sh "python test_files.py "
                }
            }
        }
    }
}
