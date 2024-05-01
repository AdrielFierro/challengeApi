pipeline{
    agent any
    tools{
        maven 'Maven'
    }
    stages{
        stage("build docker image"){
            steps{
                script{
                    powershell 'docker build -t challengeapi .' 
                    
                }
            }
        }
        stage("push docker image"){
            
            steps{
                script{
                    
                    withCredentials([usernamePassword(credentialsId: '62e8a1c9-aa37-4144-9769-03f78cb83f17', passwordVariable: 'pwd', usernameVariable: 'user')]) {
                    powershell 'docker login -u ${user} -p ${pwd}'
}
            
                powershell 'docker push challengeapi'
                
                
                        }
                
                }
            
            
        }
            }
        
    }       