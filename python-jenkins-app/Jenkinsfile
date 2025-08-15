pipeline {
    agent any
    
    environment {
        // Define environment variables if needed
        PYTHON_VERSION = '3.10'
    }
    
    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out source code...'
                // Code is automatically checked out by Jenkins
                sh 'ls -la'
            }
        }
        
        stage('Setup Python Environment') {
            steps {
                echo 'Setting up Python environment...'
                sh '''
                    python3 --version
                    pip3 --version
                '''
            }
        }
        
        stage('Install Dependencies') {
            steps {
                echo 'Installing Python dependencies...'
                sh '''
                    # Install PyInstaller directly
                    pip3 install --user pyinstaller
                    
                    # Check if requirements.txt exists and install from it
                    if [ -f requirements.txt ]; then
                        echo "Installing additional dependencies from requirements.txt"
                        pip3 install --user -r requirements.txt
                    else
                        echo "No requirements.txt found, using direct PyInstaller installation"
                    fi
                '''
            }
        }
        
        stage('Run Tests') {
            steps {
                echo 'Running unit tests...'
                sh '''
                    python3 test_hello.py
                '''
            }
            post {
                always {
                    echo 'Test stage completed'
                }
                success {
                    echo 'All tests passed!'
                }
                failure {
                    echo 'Tests failed!'
                }
            }
        }
        
        stage('Build Application') {
            steps {
                echo 'Building application with PyInstaller...'
                sh '''
                    # Build the executable
                    python3 -m PyInstaller --onefile hello.py
                    
                    # List the dist directory to confirm build
                    ls -la dist/
                '''
            }
        }
        
        stage('Test Executable') {
            steps {
                echo 'Testing the built executable...'
                sh '''
                    # Run the executable to test it works
                    ./dist/hello
                '''
            }
        }
        
        stage('Archive Artifacts') {
            steps {
                echo 'Archiving build artifacts...'
                archiveArtifacts artifacts: 'dist/*', fingerprint: true
            }
        }
    }
    
    post {
        always {
            echo 'Pipeline execution completed'
            // Clean up workspace if needed
            cleanWs()
        }
        success {
            echo 'Pipeline succeeded! 🎉'
        }
        failure {
            echo 'Pipeline failed! ❌'
        }
        unstable {
            echo 'Pipeline is unstable'
        }
    }
}
