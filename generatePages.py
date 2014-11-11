from github import Github
from html_template import *
from base64 import b64decode


supported_img_types =  ['.png','.jfif','.jfi','.jpg','.JPG','.jpeg','.jpe','.jif']

g = Github("jacksonhenry3", "Ffa7ace35")

repos = g.get_user().get_repos()
repo_name_list = []

for r in repos:
	repo_name_list.append([r.name+'.html',r.name.replace('_',' ')])

repo_name_list = []

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
	try:
		readme_path = repo.get_readme().path
		readme = get_file_contents(repo,readme_path)
	except:
		readme = ''

	projects_sidebar = make_projects_side_bar(repo_name_list)

	head         = make_head(title)
	main_img_url = find_img_in_repo(repo,'')
	zip_link     = repo.get_archive_link('zipball')
	tar_link     = repo.get_archive_link('tarball')
	github_link  = repo.clone_url
	main         = make_main(title,desc,readme,main_img_url)
	h            = make_header(owner.name,zip_link,tar_link,github_link)
	pg           = generate_page(head,h,main,projects_sidebar)
	pg           = str(pg).replace('&lt;',"<").replace('&gt;','>')
	f            = open('generated_pages/'+name+'.html','w')
	f.write(str(pg)) # python will convert \n to os.linesep
	f.close() 



#search through the directories to find an image
def find_img_in_repo(repo,path):
	files = repo.get_dir_contents(path)
	img_url = ''
	for f in files:
		if str(f.type)=='dir':
			path = f.path
			sub_img_url = find_img_in_repo(repo,path)
			if sub_img_url != '':
				return(sub_img_url)
		else:
			for extension in supported_img_types:
				if extension in f.name:
					img = f
					img_url =  img.html_url.replace('https://github.com/','https://raw.githubusercontent.com/').replace('/blob','')
	return(img_url)

#make a page for all projects
for repo in repos:
	print('making '+repo.name+'.html')
	make_project_page(repo)