# MLPipe_template
Template for di-factory Pipeline

## Steps:
0. General Considerations
2. Clone repository
3. Activate VDC
4. Load data
5. Preprocessing
6. Feature engineering
7. Training
8. Model Evaluation
9. CD Automation (4..7)
10. Experiments evaluation
11. CI Automation (3..9)
12. Deployment
13. Model updating for new data

## Contents:
### 0. General Considerations
* Used cookiecutter as a template maker for the di-factory:pipeline dir structure
* Anaconda as a local environment
* Use jupyter notebooks as a local tool for data exploration and modeling at first steps
* Use mlflow as tool for model tracking
* Use DVC as tool for data and model versioning
* Use Git as tool for version control
* Use Python 3.8 or higher


### 1. Clone repository
* $ git clone https://github.com/MLPipe_template.git
  * Change the directory name locally according with templates schemas

### 2. Activate VDC
* $ dvc init 
  * Check that dvc must be includen in requirements.txt.
  * fast reference at: https://github.com/iterative

to associate a repo for data in gcp managed by dvc, for example
* $ dvc remote add -d myremote gdrive://10AyMRWPwMf2Bp04t1jIhhyi6mawh3Z 
  * in this case goes to mydrive/data/remote for example

* $ dvc add <files>
* $ dvc add <files> .gitignore

* $ git add <files>
* $ git commit -m "dvc updating git"
* $ git push

* $ dvc push

to get a file from dvc repo
* $ dvc pull <filename> 
  * the file <filenname> must be present in the directory

to list which files are in DVC
* $ dvc list <route to repo> repo 
  * Sample: $ dvc list https://github.com/iterative/dataset-registry get-started

to access to a particular file
* $ dvc get <route to repo> repo/file
  * or
* $ dvc import <route to repo> repo 
  * here in repo.dvc you will found where you get this repo

to get the new versio fo a repo/file:
* $ dvc update repo/file.dvc

### 10. CI Automation
### using DVC

* $ dvc repro 
  * this execute dvc.yaml script
  * here a fast ref: https://dvc.org/doc/user-guide/how-to/resolve-merge-conflicts#dvcyaml
  
