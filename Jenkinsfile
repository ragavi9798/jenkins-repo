pipeline {

    agent any

    stages {

        stage("clean up") {

            steps{
                sh 'rm -rf dir'
            }
        }
        
        stage("build") {

            steps{
                echo 'create virtual environment'
                sh """
                    python3 -m venv pyenv
                    . pyenv/bin/activate
                   """
            }
        }

        stage("test") {

            steps{
                echo 'Test the App'
                sh 'python3 test_emp.py'
                
            }
        }
        stage("deploy") {

            steps{
                echo 'Deploy the App'
                //sh 'scp -i '$WORKSPACE/20954-quantiphi.pem' -o StrictHostKeyChecking=no -r try.txt ec2-user@3.82.109.51:/tmp'
            }
        }
    }
}
