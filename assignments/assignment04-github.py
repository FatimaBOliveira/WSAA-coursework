# Program that reads a file from a repository and replace the text "Andrew" with my name.
# The program will then commit those changes and push it back to the repository.
# Author: Fatima Oliveira

from github import Github
import requests
from config import apikeys as cfg
