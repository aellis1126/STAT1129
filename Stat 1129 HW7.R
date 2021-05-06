#Question 1--> Creating two matrices and multiplying
a<- matrix(c(7,9,12,2,4,13),2,3,byrow=T)
b<- matrix(c(1,7,12,19,2,8,13,20,3,9,14,21),3,4,byrow=T)
ab=a%*%b

#Question 2a--> Creating a data frame
id<- c(1,2,3,4,5)
name<- c("Peter","Amy","Ryan","Gary","Michelle")
salary<- c(623.30,515.20,611,729,843.25)
Question2<- data.frame(id,name,salary)

#Question 2b--> Adding a column
department<- c("Finance","Human Resources", "Operations", 'Hospitality', "Technology")
NewQuestion2<- data.frame(Question2,department)

#Question 2c--> Extracting rows using the c function
NewQuestion2[c(1,3,5),c(2,3)]

#Question 2d--> Bar Chart for Salaries in Row's 1,4,5
data.new<- NewQuestion2[-c(2,3),]
barplot(data.new$salary, ylab= "Salary",xlab= "Name",main= "Breakdown of Income",names.arg = c("Peter","Gary","Michelle"))

#Question 2e--> Creating a Pie Chart for Min, Max, and Median Salary
Slices<- c(max(NewQuestion2$salary),min(NewQuestion2$salary),median(NewQuestion2$salary))
labels<- c("Maximum Income", "Minimum Income", "Median Income")
pie(Slices,labels=labels, main="Distribution of Income")

#Question 3 Part 1--> Transfering Python Functions into R Functions
isValid<- function(playerMove) {
  gameMoves<- c('R','P','S')

  if (playerMove %in% gameMoves) {
    return("True")
  } else {
    return("False")
  }
}

isValid('R')

#Question 3 Part 2 --> Transfering Python Functions into R Functions
updateScore<- function(winner) {
  playerScore<- c(1)
  computerScore<- c(0)
  start<- (1)
  
  if (winner == 0) {
    playerScore = playerScore + 1
    print("Player won! Function worked properly.")
  } else {
    computerScore = computerScore + 1
  }
  
  print("| Player: %d | Computer: %d | \n", playerScore, computerScore)
  
  userPlayAgain<-readline(prompt="Play again? (Y/N):")

  # Previous version of updateScore did not have a loop.
  # So I added the ability for the player to decide if they want to play again or not. 
  # The while loop is used to validate the userPlayAgain variable and assure they entered Y or N
  # If not Y or N, the loop asks again
  while (userPlayAgain != 'Y' && userPlayAgain != 'N') {
    userPlayAgain<-readline(prompt="Play again? (Y/N):")
  }
  
  if (userPlayAgain == 'Y') {
    start = 1
  } else {
    start = 0
  }
}

updateScore(1)



