pipeline{
    agent any
// Create stage to build and run the application
    stages{
        stage('Build and Run') {
            steps {
                script {
                    // Set up the environment
                    sh 'python3 -m venv venv'
                    sh 'source venv/bin/activate'

                    // Installing Dependencies
                    sh 'pip install -r requirements.txt'

                    // Run the app.py program
                    sh 'python3 app.py'

                    
                }
            }
        }

        stage('Cleanup') {
            steps {
                // Deactivate the virtual environment and clean up
                sh 'deactivate'
                sh 'rm -rf venv'
            }
        }
    }
}