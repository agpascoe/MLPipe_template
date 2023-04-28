# This is a brief gudie to me most used commands in this di-factory:pipeline management

## About pre-commit
* Git hook scripts are useful for identifying simple issues before submission to code review.
* https://pre-commit.com/
* use the configuration file to run (exactly) the hook.
	* .pre-commit-config.yaml

* Use among others the following:
	* black
		* Black is the uncompromising Python code formatter. By using it, you agree to cede control over minutiae of hand-formatting.
		* https://pypi.org/project/black/
		* `pip install black`
		* `poetry add black`
		* `black <file.py>`
		
	* flake8
		* Python linting tool that checks Python code for style and syntax errors
		* https://pypi.org/project/flake8/
		* `pip install flake8`
		* `poetry add flake8`
		* `flake8 <file.py>`
		
	* isort 
		* isort is a Python utility / library to sort imports alphabetically, and automatically separated into sections and by type
		* https://pycqa.github.io/isort/ 
		* `poetry add isort`
		* `isort <file.py or route>


## About graphviz
* Graphviz is open source graph visualization software.
* https://www.graphviz.org/
* poetry add graphviz
	* `poetry install graphviz`


## About make
*	Make is a tool which controls the generation of executables and other non-source files of a program from the program's source file
*	Quick reference: https://www.gnu.org/software/make/
	*	uses a makefile file to generate executables
	*	for example:
  	* `install:`
  	* `@echo installin`
  	* `pip install petry`
   
*	make install
	*	To run the part of install inside the makefile    
*	make
	*	To run the whole makefile    

## About Hydra
* It is a configuration management tool, based on yaml files.
	* conda install hydra-core
	* poetry add hydra-core
	* pip install hydra-core --upadte
	* Quick reference: https://hydra.cc/docs/intro/ 


## About poetry
* conda install poetry
	* poetry is a tool for python code and repository management.

* poetry install
	* shows all packages in the current environment and start to update, install, and resolve references
* poetry add
	* adds a new package to the current environment
* poetry remove
	* removes a package from the current environment
* poetry show
	* shows all packages in the current environment
* poetry show --tree
	* shows all packages in the current environment and all sub-packages
* poetry search <query>
 	* searches for packages
* fast reference: https://python-poetry.org/docs/

## About  cookiecutter
* conda config --add channels conda-forge
  * to add channel to conda-forge
* conda install -c conda-forge cookiecutter
  * to install cookiecutter
* cookiecutter < repo_name >
  * to create a new project
* cookiecutter https://github.com/khuyentran1401/data-science-template
  * to create a new template for data science project.. it creates a new directory with the project name you chose.


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
  
  
