from github import Github
from base64 import b64decode
g = Github("jacksonhenry3", "7ffa7ace35")

repos = g.get_user().get_repos()

repo = repos[14]

def get_file_contents(repo,path):
	github_file       = repo.get_file_contents(path)
	b64_file_contents = github_file.content
	contents          = b64decode(b64_file_contents)
	return(contents)


def make_projectPage(repo):
	name = repo.name
	title = name.replace('_',' ')
	owner = repo.owner
	desc  = repo.description

	readme = get_file_contents(repo,'README.md')
	f = open(name+'.html','w')
	f.write(readme) # python will convert \n to os.linesep
	f.close() 
	# print(readme)

make_projectPage(repo)