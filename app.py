import webapp2

class MainPage(webapp2.RequestHandler):
	def get(self):
		self.response.write('WELCOME TO MY PAAS WEB APP'"<br />")
		self.response.write('Name: Adrian Oh Wei Hao'"<br />")
		self.response.write('SUSS ID: E1711467'"<br />")
		self.response.write('Course Code: ICT335'"<br />")

app = webapp2.WSGIApplication([('/', MainPage),
								],
								debug=True)