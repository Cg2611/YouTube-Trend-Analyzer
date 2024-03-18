import subprocess

# List of packages to install
packages = ["notebook", "PyQt5", "selenium", "beautifulsoup4", "nltk", "wordcloud", "matplotlib", "seaborn", "scikit-learn"]

# Install packages one by one
for package in packages:
    subprocess.check_call(["pip", "install", package])
