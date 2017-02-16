render = web.template.render('templates/')

def GET(self):
    return render.index()
