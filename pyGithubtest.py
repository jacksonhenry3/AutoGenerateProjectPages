from github import Github
from html_template import *
from base64 import b64decode
g = Github("jacksonhenry3", "7ffa7ace35")

repos = g.get_user().get_repos()
repoList = []
repo = repos[0]
for r in repos:
	repoList.append(r.name.replace('_',' '))



def get_file_contents(repo,path):
	github_file       = repo.get_file_contents(path)
	b64_file_contents = github_file.content
	contents          = b64decode(b64_file_contents)
	return(contents)


def make_project_page(repo):
	name = repo.name
	title = name.replace('_',' ')
	owner = repo.owner
	desc  = repo.description

	readme = get_file_contents(repo,'README.md')
	# generate_page(name,title,title,desc,readme)

	projects_sidebar = make_projects_side_bar(repoList)

	head = make_head('Page')

	main = make_main(title,desc,readme)
	h    = make_header(owner.name)
	pg = generate_page(head,h,main,projects_sidebar)
	pg = str(pg).replace('&lt;',"<").replace('&gt;','>')
	f = open('generated_pages/test.html','w')
	f.write(str(pg)) # python will convert \n to os.linesep
	f.close() 

make_project_page(repo)
