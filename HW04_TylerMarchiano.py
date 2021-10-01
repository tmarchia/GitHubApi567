"""
Tyler Marchiano
Oct 1st, 2021

The primary goal of this file is to develop a function that will interface with GitHub
in order to extract and present useful information to the user.
"""

import json
import requests
import sys

def getGitHubRepos(userID):
    """
    This function will return a list of repositories that belong to the given userID
    """
    repoList = []
    userRepositories = requests.get('https://api.github.com/users/'+userID+'/repos').json()
    try:
        for repo in userRepositories:
            repoList.append(repo['name'])
    except:
        return 'User ID was not found'
    
    return repoList

def getGitHubRepoCommits(userID, repo):
    """
    This function will return the number of commits a certain repo has
    """
    userRepoCommits = requests.get('https://api.github.com/repos/'+userID+'/'+repo+'/commits').json()
    
    return len(userRepoCommits)
        

def main() -> None:
    '''Main function that prompts user for the GitHub User ID'''
    userID = input('Please enter a GitHub User ID: ')
    print()
    
    repositoryResult = getGitHubRepos(userID)
    
    if repositoryResult != 'User ID was not found':
        for repo in repositoryResult:
            numCommits = getGitHubRepoCommits(userID, repo)
            print(f'Repo: {repo} Number of commits: {numCommits}')
    else:
        print(repositoryResult)
        
if __name__ == "__main__":
    print()
    print("Running main()....")
    main()