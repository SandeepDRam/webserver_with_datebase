pipeline {
   
   agent any //{label 'slave_linux'}
    stages {
        
    //stage('Checkout SCM')   {
        
      //  steps {
      //git ('https://github.com/arksinha93/python-flask-demo.git')
      //if (!fileExists("Dockerfile")) {
        // error('Dockerfile missing.')  

    stage('Build') {
       
       steps {       
          sh "sudo docker build -t my-flask-app ."
          
   }
   }

    stage('Test') {
       
       steps {
          sh "sudo docker rm --force my-flask-app"         
          sh "sudo docker run -p 5000:5000 --name my-flask-app -d my-flask-app"
   }      
   }
       stage('Sast') {
            steps {
                sh 'python3 -m unittest test_hello_world.py'
                  }
               post {
                failure {
                   mail to: 'drsandeep2024@gmail.com', subject: 'Compile failed', body: 'Please fix the build'
                   //Jira newIssue: true, summary: 'Compile failed', description: 'Please fix the build'
                   gitHubIssue title: 'Compile failed', body: 'Please fix the build', labels: 'build failure'
                         }
                success {
                   mail to: 'drsandeep2024@gmail.com', subject: 'Unit tests passed', body: 'Congratulations!'
                        }
                     }
        }
    stage('Dast') {
      steps {
         //sh 'source /path/to/venv/bin/activate && pip install flake8'
         //sh 'pip install flake8'
         //sh 'export PATH="/home/ec2-user/venv/lib/python3.9/site-packages";'
         //sh 'conda activate myenv; python3 app.py'
         //sh 'source /home/ec2-user/miniconda3/lib/python3.9/site-packages'
         sh 'sudo pip3 install flake8'
         sh 'sudo pip3 install flask'
         sh 'flake8 app.py'
      }
    }
    stage('Deploy') {
       
       steps {
          //sh "sudo docker rm --force my-flask-app"         
          //sh "sudo docker run -p 5000:5000 --name my-flask-app -d my-flask-app"
          sh "sudo docker ps" 
   }      
   }   
     }  // End of stages
 
} // End of pipeline
