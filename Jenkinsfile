pipeline {

    agent any

    stages {

        stage("cleaning") {

            steps{
                echo 'cleaning the directory..'
                echo 'before cleaning..'
                sh 'ls -la'
                sh 'rm -rf temp_deploy'
                echo 'After cleaning..'
                sh 'ls -la'
            }
        }
        
        stage("build") {

            steps{
                echo 'building application..'
                echo 'creating virtual environment'
                sh "pwd"
                sh """
                    python3 -m venv pyenv
                    . pyenv/bin/activate
                   """
            }
        }

        stage("test") {

            steps{
                echo 'testing the application..'
                sh 'python3 test_emp.py'
                
            }
        }
        stage("deploy") {

            steps{
                echo 'Deploying the application..'
                echo 'removing previous deployed directory..'
                sh 'ssh ec2-user@3.82.109.51 rm -rf temp_deploy'
                echo 'create new deploy directory..'
                sh 'ssh ec2-user@3.82.109.51 mkdir -p temp_deploy'
                sh 'scp -r /var/lib/jenkins/workspace/pipeline-20954 ec2-user@3.82.109.51:/home/ec2-user/temp_deploy/'
                echo 'After moving files into ec2 instance'
                sh 'ssh ec2-user@3.82.109.51 ls -la'
                
                echo 'Running test application..'
                sh """
                    ssh ec2-user@3.82.109.51 python3 temp_deploy/pipeline-20954/test_emp.py
                   """
                
            }
        }
    }
}
