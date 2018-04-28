# Instructions on GitHub      

# When work with myself

1. Establish a repository on github.com

2. Copy the SSH of that repository 

3. Clone the repository on pc  
  
  git clone url 

  git log // need to show the history made to the repository


4. Edit new files in the repository from pc

5. Add the files from pc to github.com
  
  git add filename
  
  /git add .
  
  git commit -m'message about this change'
  
  git push

6. In case you want to get files from github.com to pc
  
  git pull

# When work with others in a repository:

1. Get a branch name for yourself 

    git branch branchName

2. Switch to your branch
    
    git checkout branchName

3. Check the status to see if there's something uncommited

    git status

4. Check the difference between commits
    
    git diff partial commit 1 partial commit 2

5. Push your work (to push the newly created branch into repository)

    git push --set-upstream origin branchName

# Advanced Branching

1. When the master branch is edited at the same time we work on our branch
	
    git checkout branchName
	
    git rebase master
	
	OR 
	
    git checkout master

    git merge branchName
	
