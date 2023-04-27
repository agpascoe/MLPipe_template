# This is a brief gudie to me most used commands in this di-factory:pipeline management
## About GitHub
### Update local changes to github repo
* git add <files>
* git commit -m "message associated to commit"
* git push

### To get the status of the sync
* git status
  
### To get the log of the sync
* git log

### to create a remote repo
* git init && git add . && git commit -m "first commit"  
* git remote add origin <remote_url>
* git push -u origin master/main

## About DVC
  
### initialize dvc
* dvc init
  
### add a directory to the repo
* dvc add <directory>

### add a file to the repo
* dvc add <file>
 
### to create a remote gdrive repo
* dvc remote add --default myremote gdrive://0AIac4JZqHhKmUk9PDA/dvcstore  
* dvc remote modify myremote gdrive_acknowledge_abuse true
  
### update the repo
* dvc push  

### to see the result of an experiment run
* dvc metrics show -T

## About Jupyter notebook
* conda install -python_env ipykernel
  * to install jupyter in a particular conda enviroment if not run
* python -m ipykernel install --user --name <env_name>
  
  
