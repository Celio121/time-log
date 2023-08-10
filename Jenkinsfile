pipeline{
    agent any

    stages{
        stage('Build and Run') {
            steps {
                script {
                    // Set up the environment
                    sh 'python3 -m venv venv'
                    sh '. venv/bin/activate'

                    // Installing Dependencies
                    sh 'pip install -r requirements.txt'

                    // Run the app.py program
                    sh 'python3 app.py'
                }
            }
        }
    }
}