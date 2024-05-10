pipeline{

    agent any

    stages{
        stage("build docker image"){
            steps{
                script{
                    bat 'docker build -t  afierro4458/challengeapi:latest .' 
                    
                }
            }
        }
        stage("push docker image"){
            
            steps{
                script{
                    bat 'docker push afierro4458/challengeapi:latest'
                
                }
            
            
        }
            }
        
    }
        
    }