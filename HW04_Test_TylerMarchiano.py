"""
Tyler Marchiano
Oct 1st, 2021

The primary goal of this file is to develop a function that will interface with GitHub
in order to extract and present useful information to the user.
"""

import unittest

from HW04_TylerMarchiano import getGitHubRepos, getGitHubRepoCommits

class TestGitHub(unittest.TestCase):

    #Test ID 1
    def testGitHubRepos1(self): 
        self.assertEqual(getGitHubRepos('richkempinski'),['csp', 'hellogitworld', 'helloworld', 'Mocks', 'Project1', 'richkempinski.github.io', 'threads-of-life', 'try_nbdev', 'try_nbdev2'])

    #Test ID 2
    def testGitHubRepos2(self): 
        self.assertEqual(getGitHubRepos('richkpinski'),'User ID was not found')
        
    #Test ID 3
    def testGitHubRepos3(self): 
        self.assertEqual(getGitHubRepos('tmarchia'),['GitHubApi567', 'SSW567', 'Student-Repository'])
        
    #Test ID 4
    def testGitHubRepos4(self): 
        self.assertEqual(getGitHubRepos('tmarchiaaaa'), 'User ID was not found')
    """
    #Test ID 5
    def testGitHubRepoCommits1(self): 
        self.assertEqual(getGitHubRepoCommits('tmarchia', 'Student-Repository'), NUMBER)
    
    #Test ID 6
    def testGitHubRepoCommits1(self): 
        self.assertEqual(getGitHubRepoCommits('richkempinski', 'hellogitworld'), NUMBER)
    """

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

