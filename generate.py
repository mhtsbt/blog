from jinja2 import Environment, PackageLoader, select_autoescape
env = Environment(
    loader=PackageLoader("blog_generator"),
    autoescape=select_autoescape()
)

template = env.get_template("mytemplate.html")

output = template.render(the="variables", go="here")

myfile = open("output/index.html", 'w')
myfile.write(output)
myfile.close()
