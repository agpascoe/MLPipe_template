# MLPipe_template
Template for di-factory Pipeline
Steps:
1. Clone repository
2. Activate VDC
3. Load data
4. Preprocessing
5. Feature engineering
6. Training
7. Evaluation

1. Clone repository
$ git clone https://github.com/MLPipe_template.git
Change the directory name locally according with templates schemas

2. Activate VDC
$ dvc init # Check that dvc must be includen in requirements.txt.
# fast reference at: https://github.com/iterative

# to associate a repo for data in gcp managed by dvc, for example
$ dvc remote add -d myremote gdrive://10AyMRWPwMf2Bp04t1jIhhyi6mawh3Z #in this case goes to mydrive/data/remote for example
$ dvc add <files>
$ dvc add <files> .gitignore

$ git add <files>
$ git commit -m "dvc updating git"
$ git push

$ dvc push

# to get a file from dvc repo
$ dvc pull <filename>


