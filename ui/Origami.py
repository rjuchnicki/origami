import sublime
import sublime_plugin
import commands
from shutil import copy

def execute(command):
	return commands.getstatusoutput(command)

filename = 'slideshow.txt'
prev = None

compiler = '/Users/tommychen/anaconda/python.app/Contents/MacOS/python'
command = compiler + ' build.py'
class AddCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		global prev
		path = open(filename, 'ab')
		selection = sublime.Region(0, self.view.size())
		if len(self.view.sel()) == 1:
			selection = self.view.sel()[0]
		code = self.view.substr(selection)
		if code != prev:
			path.write('\n--------\n')
			path.write(code)
			path.write('\n--------\n')
			path.close()
			prev = code
		execute(command)

class CleanCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		open(filename, 'wb').close()

class OpenCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		sublime.active_window().open_file(filename)

class PowerpointCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		execute('/Users/tommychen/anaconda/python.app/Contents/MacOS/python build.py')
		execute('open slideshow.pptx')

class DropboxCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		copy('slideshow.pptx', '/Users/tommychen/Dropbox/slideshow.pptx')
		self.view.insert(edit, 0, '# The link to your powerpoint is: https://www.dropbox.com/s/f4fzv3pd4vl5p55/slideshow.pptx\n\n')
		execute('open slideshow.pptx')