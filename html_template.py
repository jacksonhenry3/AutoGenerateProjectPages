
#uses pyhtml to generate the code for the webpage
from pyhtml import *

#this is the main funciton, it generates the entir template
def generate_page(head,h,main,projects_sidebar):
	page = html(
			head,
			body(
				h,
				div(id = 'all')(
					main,
					projects_sidebar
				)
			)
	)

	return(page)

#this generates the elements inside the head element
def make_head(pg_title,favico_url = '',stylesheet = 'main.css'):
	h = head(
		title(pg_title+' Project Page'),
		meta(charset='UTF-8'),
		meta(name="viewport", content="width=device-width, height=device-height"),
		meta(content='width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=0', name='viewport'),
		link(rel="shortcut icon", href=favico_url),
		link(rel='stylesheet', href=stylesheet),
	)
	return(h)

#this generates the sidebar with all projects
def make_projects_side_bar(project_list):
	projects = []
	for project in project_list:
		projects.append(li(a(href = project[0])(project[1])))

	project_ul = ul(
		projects
	)
	sidebar = div(id = 'sidebar')(
		h2('Other Projects'),
		project_ul
		)
	return(sidebar)

def make_main(title,subtitle,content,img_src):
	d = div(id = 'main_container')(div(id = 'main')(
			image(img_src),
			h1(a(title)),
			h3(subtitle),
			div(content)
		))
	return(d)

def image(img_src):
	if img_src != '':
		return(img(src = img_src))
def make_header(name,zip_link,tar_link,github_link):
	h = header(id = 'header')(
		a(href = zip_link)('.zip'),
		a(href = tar_link)('.tar.gz'),
		a(href = github_link)('github')
		)
	return(h)