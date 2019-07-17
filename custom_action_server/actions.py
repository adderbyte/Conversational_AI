from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

#from rasa_core.actions.action import Action
#from rasa.core.events import SlotSet
from rasa_sdk import Action
#from rasa_sdk import SlotSet
import nltk 
import re 

from rasa_core_sdk.events import SlotSet


class ActionCheckCancelDetails(Action):
    def name(self):
        return 'action_check_cancel_details'

    def run(self, dispatcher, tracker, domain):

        #prod = tracker.get_slot('product')
        order = tracker.get_slot('order')
        account = tracker.get_slot('account')
        

        #confirmationNumber = 123456 #later generate through some process
        print('####........####', tracker.latest_message.get("text"),tracker.slots)

        ################ If model is not detecting the slots inputed. uncomment this line  to use NLTK ###############################
        mesg = tracker.latest_message.get("text")
        text = nltk.word_tokenize(mesg)
        order = [ s for s in text if re.match('^(?=.*[0-9]$)(?=.*[a-zA-Z])', s)  ]
        account = [ s for s in text if s.isdigit() ]
        #################################################################################################################################
        if not order:
            response = """Please provide a valid order id for verification. The order id is not supplied"""
        elif not account:
            response = """Please provide a valid account number for verification. The account number   is not supplied"""
        elif order and account :
            response = """Your account {} is being  verified.  Your order {} is being cancelled.""".format(account[0],order[0])
         
        dispatcher.utter_message(response)
        return [SlotSet('order',order),SlotSet('account',account)]

class ActionCheckOrderDetails(Action):
    def name(self):
        return 'action_check_order_details'

    def run(self, dispatcher, tracker, domain):

        #print('..........................', 'I am checking')


        # to confirm information in the slot. check this print message. It is for diagnosis purposes
        print('####........####', tracker.latest_message.get("text"),tracker.slots)

        ################ If model is not detecting the slots inputed. uncomment this line  to use NLTK ###############################
        mesg = tracker.latest_message.get("text") # get the message 
        text = nltk.word_tokenize(mesg) # split message into words 
        order = [ s for s in text if re.match('^(?=.*[0-9]$)(?=.*[a-zA-Z])', s)  ] # order id should be alpha  numeric
        account = [ s for s in text if s.isdigit() ] # account number should be digit. Estract the digit from the text
        #################################################################################################################################
        if not order:
            response = """Please provide a valid order id . The order is not supplied"""
        elif not account:
            response = """Please provide a valid account number. The account number  is not supplied"""
        elif order and account :
            response = """Your account {} is being  verified.  Your order {} status is being updated .""".format(account[0],order[0])

        #response = """Your account {} is being  verified.  Your order {} order status will be mailed to your account right away.""".format(order,account)

        dispatcher.utter_message(response)
        return [SlotSet('order',order),SlotSet('account',account)]