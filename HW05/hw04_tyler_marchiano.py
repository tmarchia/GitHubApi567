"""
Tyler Marchiano
Oct 1st, 2021

The primary goal of this file is to develop a function that will interface with GitHub
in order to extract and present useful information to the user.
"""

import requests

def get_repos(user_id):
    """
    This function will return a list of repositories that belong to the given userID
    """
    repo_list = []
    user_repositories = requests.get('https://api.github.com/users/'+user_id+'/repos').json()
    try:
        for repo in user_repositories:
            repo_list.append(repo['name'])
    except TypeError:
        return 'User ID was not found'
    return repo_list

def get_repo_commits(user_id, repo):
    """
    This function will return the number of commits a certain repo has
    """
    user_commits = requests.get('https://api.github.com/repos/'+user_id+'/'+repo+'/commits').json()
    return len(user_commits)

def main() -> None:
    '''Main function that prompts user for the GitHub User ID'''
    user_id = input('Please enter a GitHub User ID: ')
    repository_result = get_repos(user_id)
    if repository_result != 'User ID was not found':
        for repo in repository_result:
            print(f'Repo: {repo} Number of commits: {get_repo_commits(user_id, repo)}')
    else:
        print(repository_result)
if __name__ == "__main__":
    main()
    