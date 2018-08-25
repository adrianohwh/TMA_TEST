import webapp2

class MainPage(webapp2.RequestHandler):
	def get(self):
		self.response.write("WELCOME TO MY PAAS WEB APP""\n")
		self.response.write("Name: Adrian Oh Wei Hao""\n")
		self.response.write("SUSS ID: E1711467""\n")
		self.response.write("Course Code: ICT335""\n")

app = webapp2.WSGIApplication([('/', MainPage),
								],
								debug=True)