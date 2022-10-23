# Git Cheat Sheet 

### Clone Repository to a Parent Folder:

    git clone https://github.com/leezael/TeamTrifecta_CS504.git

### New features should be housed in new branches until they are ready to move to main

    git switch -c "Branch Name"

### You can switch between branches by omitting the -c  flag

    git switch main

### Stage file(s) for commit

    git add filename 

### Commit files with Message

    git commit -m "What you changed"

### Push new Branch to GitHub

    git push -u origin <branch_name>

### Get latest version from GitHub

    git pull

