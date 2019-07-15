from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet


class ActionCheckCancelDetails(Action):
	def name(self):
		return 'action_check_cancel_details'

	def run(self, dispatcher, tracker, domain):

		#prod = tracker.get_slot('product')
		order = tracker.get_slot('order')
		account = tracker.get_slot('account')


		#confirmationNumber = 123456 #later generate through some process

		response = """Your account {} is being  verified.  Your order {} has been cancelled.""".format(order,account)

		dispatcher.utter_message(response)
		return [SlotSet('order',order),SlotSet('account',account)]

class ActionCheckOrderDetails(Action):
	def name(self):
		return 'action_check_order_details'

	def run(self, dispatcher, tracker, domain):

		#prod = tracker.get_slot('product')
		order = tracker.get_slot('order')
		account = tracker.get_slot('account')


		#confirmationNumber = 123456 #later generate through some process

		response = """Your account {} is being  verified.  Your order {} order status will be mailed to your account right away.""".format(order,account)

		dispatcher.utter_message(response)
		return [SlotSet('order',order),SlotSet('account',account)]