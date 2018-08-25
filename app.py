import webapp2

class MainPage(webapp2.RequestHandler):
	def get(self):
		self.response.write("WELCOME TO MY PAAS WEB APP")

app = webapp2.WSGIApplication([('/', MainPage),
								],
								debug=True)