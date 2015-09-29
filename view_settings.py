# coding: utf-8

import ui

class SettingsController(object):
	def __init__(self):
		self.view = ui.load_view('view_settings.pyui')
		self.scroll = self.view['settings_scrollview']

if __name__ == '__main__':  # pragma: no cover
	SettingsController().view.present(hide_title_bar=True)
