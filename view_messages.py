# coding: utf-8

import ui

class MessagesController(object):
	def __init__(self):
		self.view = ui.load_view('view_messages.pyui')
		self.bt_set_mode(None)
		self.view['mode_segmentedcontrol'].action = self.bt_set_mode
	
	def bt_set_mode(self,sender):
		modesc = self.view['mode_segmentedcontrol']
		try:
			self.mode = modesc.segments[modesc.selected_index]
		except IndexError:
			self.mode = None

if __name__ == '__main__':  # pragma: no cover
	MessagesController().view.present(hide_title_bar=True)
