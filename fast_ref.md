# This is a brief gudie to me most used commands in this di-factory:pipeline management

## About PyCaret
PyCaret is an open-source, low-code machine learning library in Python that automates machine learning workflows.
https://pycaret.gitbook.io/docs/
* `pip install --upgrade pycaret`
* install analysis extras
	* `pip install pycaret[analysis]`
* models extras
	* `pip install pycaret[models]`
* install tuner extras
	* `pip install pycaret[tuner]`
* install mlops extras
	* `pip install pycaret[mlops]`
* install parallel extras
	* `pip install pycaret[parallel]`
* install test extras
	* `pip install pycaret[test]`
* install multiple extras together
	* `pip install pycaret[analysis,models]`

### Classification OOP API Examples
* loading sample dataset
	* `from pycaret.datasets import get_data`
	* `data = get_data('juice')`

* init setup
	* `from pycaret.classification import ClassificationExperiment`
	* `s = ClassificationExperiment()`
	* `s.setup(data, target = 'Purchase', session_id = 123)`

* model training and selection
	* `best = s.compare_models()`

* evaluate trained model
	* `s.evaluate_model(best)`

* predict on hold-out/test set
	* `pred_holdout = s.predict_model(best)`

* predict on new data
	* `new_data = data.copy().drop('Purchase', axis = 1)`
	* `predictions = s.predict_model(best, data = new_data)`

* save model
	* `s.save_model(best, 'best_pipeline')`

![image](https://user-images.githubusercontent.com/45379312/235204321-d26ebbd3-3522-4cf1-b3bf-4f0f3c558ca0.png)



## About pre-commit
* Git hook scripts are useful for identifying simple issues before submission to code review.
* https://pre-commit.com/
* Use the configuration file to run (exactly) the hook.
	* `.pre-commit-config.yaml`
* Steps:
	* `pre-commit install`
	* `git add .`
	* `git commit -m "message"`
		* Activate pre-commit and run .pre-commit-config.yaml 

* Use, among others the following:
	* **black**
		* Black is the uncompromising Python code formatter. By using it, you agree to cede control over minutiae of hand-formatting.
		* https://pypi.org/project/black/
		* `pip install black`
		* `poetry add black`
		* `black <file.py>`
		
	* **flake8**
		* Python linting tool that checks Python code for style and syntax errors
		* https://pypi.org/project/flake8/
		* `pip install flake8`
		* `poetry add flake8`
		* `flake8 <file.py>`
		
	* **isort** 
		* isort is a Python utility / library to sort imports alphabetically, and automatically separated into sections and by type
		* https://pycqa.github.io/isort/ 
		* `poetry add isort`
		* `isort <file.py or route>`
	
	* **iterrogate**
		* iterrogate is a Python utility / library to generate documentation for Python classes and functions
		* https://iterrogate.readthedocs.io/en/latest/
		* `pip install iterrogate`
		* `poetry add iterrogate`
		* `iterrogate <file.py>`	


## About graphviz
* Graphviz is open source graph visualization software.
* https://www.graphviz.org/
* `poetry add graphviz`
* `pip install graphviz`


## About make
* Make is a tool which controls the generation of executables and other non-source files of a program from the program's source file
* Quick reference: https://www.gnu.org/software/make/
* Uses a <makefile> file to generate executables. For example <makfile>:
  * `install:`
  * `@echo installin`
  * `pip install petry`
* To run the part of install inside the makefile    
	* `make install`
* To run the whole makefile    
	* `make`
* To generate documentation from docstrings    
	* `make docs_view`
	* uses pdoc behind the scenes
	* other option is to use pdoc3 (without make)

## About pdoc3
* pdoc3 is a Python library for generating documentation from Python modules.
* https://pdoc3.readthedocs.io/
* `pip install pdoc3`
* `poetry add pdoc3`
* `pdoc --http localhost:8080 <file.py>`
	
## About Hydra
* It is a configuration management tool, based on yaml files.
* `conda install hydra-core`
* `poetry add hydra-core`
* `pip install hydra-core --upadte`
* Quick reference: https://hydra.cc/docs/intro/ 


## About poetry
* Is a tool for dependency management and packaging in Python. It allows you to declare the libraries your project depends on and it will manage (install/update) them for you. 
* `conda install poetry`
	* poetry is a tool for python code and repository management.
* `poetry install`
	* shows all packages in the current environment and start to update, install, and resolve references
* `poetry add`
	* adds a new package to the current environment
* `poetry remove`
	* removes a package from the current environment
* `poetry show`
	* shows all packages in the current environment
* `poetry show --tree`
	* shows all packages in the current environment and all sub-packages
* `poetry search <query>`
 	* searches for packages
* fast reference: https://python-poetry.org/docs/

## About  cookiecutter
Is a tool for dependency management and packaging in Python. It allows you to declare the libraries your project depends on and it will manage (install/update) them for you. 
* `conda config --add channels conda-forge`
  * to add channel to conda-forge
* `conda install -c conda-forge cookiecutter`
  * to install cookiecutter
* `cookiecutter < repo_name >`
  * to create a new project
* `cookiecutter https://github.com/khuyentran1401/data-science-template`
  * to create a new template for data science project.. it creates a new directory with the project name you chose.


## About GitHub
Update local changes to github repo
	* `git add <files>`
	* `git commit -m "message associated to commit"`
	* `git push`
To get the status of the sync
	* `git status`
To get the log of the sync
	* `git log
to create a remote repo
	* `git init && git add . && git commit -m "first commit"`  
	* `git remote add origin <remote_url>`
	* `git push -u origin master/main`

## About DVC
Platform-agnostic version system for data, machine learning models, and experiments  
initialize dvc
	* `dvc init`
add a directory to the repo
	* `dvc add <directory>`
add a file to the repo
	* `dvc add <file>`
to create a remote gdrive repo
	* `dvc remote add --default myremote gdrive://0AIac4JZqHhKmUk9PDA/dvcstore`  
	* `dvc remote modify myremote gdrive_acknowledge_abuse true`
update the repo
	* `dvc push`  
to see the result of an experiment run
	* `dvc metrics show -T`

## About Jupyter notebook
to install jupyter in a particular conda enviroment
	* `conda install -python_env ipykernel`
if not run
	* `python -m ipykernel install --user --name <env_name>
  
  
