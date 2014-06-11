from pyhtml import *
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


def make_head(pg_title,favico_url = '',stylesheet = 'main.css'):
	h = head(
		title(pg_title),
		meta(charset='UTF-8'),
		meta(name="viewport", content="width=device-width, height=device-height"),
		meta(content='width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=0', name='viewport'),
		link(rel="shortcut icon", href=favico_url),
		link(rel='stylesheet', href=stylesheet),
	)
	return(h)

def make_projects_side_bar(project_list):
	projects = []
	for project in project_list:
		projects.append(li(a(project)))

	project_ul = ul(
		projects
	)
	sidebar = div(id = 'sidebar')(
		project_ul
		)
	return(sidebar)

def make_main(title,subtitle,content,img_src):
	d = div(id = 'main_container')(div(id = 'main')(
		img(src = img_src),
			h1(a(title)),
			h3(subtitle),
			p(content)
		))
	return(d)

def make_header(name):
	h = header(id = 'header')(
		h2(name+"'s github projects")
		)
	return(h)

# project_list = [
# "Abstract Art Project","AutoGenerateProjectPages","cipherTyper","cloudSimulator","github","graphingCalculator","jacksonhenry3.github.io","kinematics_Solver","newMediaPlayground","PythonRSAtesting","quantumTicTacToe","Recipe_book","sierpinskiTriangle","to_print","ulamSpiral","UtTotum","vector_field","TEST","UtTotemCS"]
# projects_sidebar = make_projects_side_bar(project_list)

# head = make_head('Test Page')

# main = make_main()
# h    = make_header('Jackson Henry')
# generate_page()
