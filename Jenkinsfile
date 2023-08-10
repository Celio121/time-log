pipeline{
    agent any
// Create stage to build and run the application
    stages{
        stage('Setup') {
            steps {
                    // Set up the environment
                    sh 'python3 -m venv venv'
                    sh '. venv/bin/activate'
            }
        }

        stage('Running application'){
            steps {
                //Run the application
                sh '. venv/bin/activate && python3 app.py 3'
            }
        }
        stage('Testing'){
            steps{
                //Run tests
                sh '. venv/bin/activate && apt install pytest'
                sh '. venv/bin/activate && pytest test_app.py'
            }
        }

        stage('Cleanup') {
            steps {
                // Deactivate the virtual environment and clean up
                sh '. venv/bin/activate && deactivate'
                sh 'rm -rf venv'
            }
        }
    }
}