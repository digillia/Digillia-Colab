This project consists in Jupyter notebooks organised in 3 directories:  `/algorithms`, `/tools` and `/use-cases`.
These notebooks showcase artificial intelligence code and may use data stored in the `/data` directory.

`/requirements.txt` should contain all the Python packages that are available by default in Google Colab. These can be installed locally using `make install` from Makefile. Other relevant packages should be installed by each Jupyter notebook using `!pip3 install -qU <package>` statements for use either locally or from Github CI workflows with pytest when needed.

When run locally, API keys are loaded from /.env file using `load_dotenv(find_dotenv())`. In Google Colab, API keys are loaded from `userdata`. In Github CI workflows, API keys are stored as secrets and loaded in the OS environment in `jobs:build:env` in the workflow yaml file. Refer to /.github/workflows/pytest.yaml.

When temporary files are needed or generated, the jupyter notebook should create a temporary directory of the same name using `!mkdir -p $work_directory` after initializing `work_directory="./<ipynb_filename>` and clean up at the end of the notebook using `!rm -rf $work_directory`. 