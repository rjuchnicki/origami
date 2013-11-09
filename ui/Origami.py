import sublime, sublime_plugin
from commands import getstatusoutput

command1 = '/Users/tommychen/anaconda/python.app/Contents/MacOS/python create.py'
command2 = 'open /Users/tommychen/Desktop/bah.pptx'

def generate():
	return getstatusoutput(command1)

def editor():
	return getstatusoutput(command2)

SLIDE = 1

class OrigamiCommand(sublime_plugin.TextCommand):
	def __init__(self, view):
		self.view = view
	def run(self, view):
		global SLIDE
		code = self.view.substr(sublime.Region(0, self.view.size()))
		open('%d.txt' % SLIDE, 'wb').write(code)
		a, b = generate()
		print b
		SLIDE += 1
		print SLIDE

class BahCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		editor()