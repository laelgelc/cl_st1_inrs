#!/bin/bash

clear

# Update and upgrade the system
sudo apt update && sudo apt upgrade -y || { echo "Failed to update and upgrade packages"; exit 1; }

# Install necessary packages
sudo snap install aws-cli --classic
sudo apt install -y ripgrep html2text unzip python3-pip python3-venv

# Create directory for TreeTagger
mkdir -p ~/treetagger/

# Define base URL for TreeTagger files
BASE_URL="https://cis.uni-muenchen.de/~schmid/tools/TreeTagger/data"

# Download TreeTagger files
curl -O ${BASE_URL}/tree-tagger-linux-3.2.5.tar.gz -o ~/treetagger/$(basename ${BASE_URL}/tree-tagger-linux-3.2.5.tar.gz)
curl -O ${BASE_URL}/tagger-scripts.tar.gz -o ~/treetagger/$(basename ${BASE_URL}/tagger-scripts.tar.gz)
curl -O ${BASE_URL}/install-tagger.sh -o ~/treetagger/$(basename ${BASE_URL}/install-tagger.sh)
curl -O ${BASE_URL}/english.par.gz -o ~/treetagger/$(basename ${BASE_URL}/english.par.gz)
curl -O ${BASE_URL}/portuguese2.par.gz -o ~/treetagger/$(basename ${BASE_URL}/portuguese2.par.gz)

# Install TreeTagger
~/treetagger/install-tagger.sh

# Append TreeTagger paths to .bashrc
echo >> ~/.bashrc
echo "# The following lines add TreeTagger to the PATH variable" >> ~/.bashrc
echo "export PATH=\$PATH:/home/ubuntu/treetagger/cmd" >> ~/.bashrc
echo "export PATH=\$PATH:/home/ubuntu/treetagger/bin" >> ~/.bashrc

# Set up Python virtual environment
python3 -m venv my_env
source "$HOME"/my_env/bin/activate
pip install ipython pandas demoji nltk
deactivate

# Logout to apply changes
logout
