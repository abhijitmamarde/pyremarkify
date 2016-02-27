usage_str = """
pyremarkify filename.md
---------------------

coverts input file which is in markdown in set of presentation slides using remarkjs.
"""

template_html = """<!DOCTYPE html>
<html>
  <head>
    <title>%(page_title)s</title>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>
    <link rel='stylesheet' href='css/remark.css'/>
    <link rel='stylesheet' href='css/darkly.min.css'/>
  </head>
<body>
<textarea id="source">

class: center, middle

# %(slide_title)s

---

%(markdown_content)s

</textarea>
    <script src="js/remark.min.js" type="text/javascript">
    </script>
    <script type="text/javascript">
      var slideshow = remark.create({
        ratio: '16:9'
      });
    </script>
  </body>
</html>

"""

known_keywords = [
	'page_title', 
	'slide_title', 
	'last_slide', 

	'markdown_content',

	'thankyou_slide_title',
	'thankyou_slide',
	]

default_keys_dir = {
	'page_title' : "Presentation", 
	'slide_title': "Presentation Title",

	'thankyou_slide_title' : "Default Thank",
	'thankyou_slide'       : "no",
}

found_keys_dir = {}

import zipfile
import os
import shutil

def print_usage():
	print(usage_str)

def create_html_file(content, out_filename):
	zipfile.ZipFile('./files.zip').extractall()
	out_folder = out_filename[:-5] + "_presentation"
	shutil.move('files', out_folder)
	open(os.path.join(out_folder, out_filename), "w").write(content)
	print("HTML file created: %s" % os.path.join(out_folder, out_filename))


def add_thankyou_slide(markdown_content):
	if 'thankyou_slide' in found_keys_dir and found_keys_dir['thankyou_slide'].lower().startswith("y"):
		new_markdown_content = [
			'\n',
			'---\n',
			'class: center, middle\n',
			'# %s\n' % found_keys_dir['thankyou_slide_title'],
			]
		markdown_content += new_markdown_content

def render_file(inp_filename):
	markdown_content = []

	# Fetches keywords and contents from file
	file_content = open(inp_filename).readlines()
	for line in file_content:
		if line.startswith('#~'):
			tline = line.split()
			key, value = tline[1], " ".join(tline[2:])
			if key in known_keywords:
				found_keys_dir[key] = value
		else:
			markdown_content.append(line)

	add_thankyou_slide(markdown_content)
	markdown_content = "".join(markdown_content)
	found_keys_dir['markdown_content'] = markdown_content


	# merge the default values
	for key in known_keywords:
		if (key in default_keys_dir) and (key not in found_keys_dir):
			found_keys_dir[key] = default_keys_dir[key]

	# write the file with content
	out = template_html % dict(found_keys_dir)
	out_filename = found_keys_dir['page_title'].replace(' ', '_').lower() + ".html"
	create_html_file(out, out_filename)
	

def render(argv):
	inp_filename = "" if len(argv) < 2 else argv[1]
	if inp_filename:
		print("Rendering file: %s" % inp_filename)
		render_file(inp_filename)
	else:
		print_usage()