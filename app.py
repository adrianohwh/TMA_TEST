import webapp2

class MainPage(webapp2.RequestHandler):
	def get(self):
		self.response.write("WELCOME TO MY PAAS WEB APP")
		self.response.writelines("Name: Adrian Oh Wei Hao")
		self.response.writelines("SUSS ID: E1711467")
		self.response.writelines("Course Code: ICT335")

app = webapp2.WSGIApplication([('/', MainPage),
								],
								debug=True)