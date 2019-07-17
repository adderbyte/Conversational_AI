## story_001
* greet
   - utter_greet
* order_status
   - utter_ask_account_number_order_id
* order_status[order=BEDSW912]
   - slot{"order": "BEDSW912"}
   - action_check_order_details
* order_status[account=09128342]
   - slot{"account": "09128342"}
   - action_check_order_details
* report_status
   - action_check_order_details
* goodbye
   - utter_goodbye
## story_002
* greet
   - utter_greet
* cancel_order
   - utter_ask_account_number_order_id
* cancel_order[order=BEDSW912]
   - slot{"order": "BEDSW912"}
   - action_check_cancel_details
* cancel_order[account=09128342]
   - slot{"account": "09128342"}
   - action_check_cancel_details
* report_status
   - action_check_cancel_details
* goodbye
   - utter_goodbye
## story_003
* greet
   - utter_greet
* cancel_order
   - utter_ask_account_number_order_id
* cancel_order[order=BEDSW912]
   - slot{"order": "BEDSW912"}
   - action_check_cancel_details
* cancel_order[account=09128342]
   - slot{"account": "09128342"}
   - action_check_cancel_details
* report_status
   - action_check_cancel_details
* goodbye
   - utter_goodbye
## story_004
* greet
   - utter_greet
* order_status
   - utter_ask_account_number_order_id
* order_staus[order=987yh512]
   - slot{"order": "987yh512"}
   - action_check_order_details
* order_staus[account=32430984]
   - slot{"account": "32430984"}
   - action_check_order_details
* report_status
   - action_check_order_details
* goodbye
   - utter_affirm
## story_005
* greet
   - utter_greet
* order_status
   - utter_ask_account_number_order_id
* order_staus[order=A8B9V1E9]
   - slot{"order": "A8B9V1E9"}
   - action_check_order_details
* order_staus[account=32430984]
   - slot{"account": "87630823"}
   - action_check_order_details
* report_status
   - action_check_order_details
* goodbye
   - utter_goodbye
## story_006
* greet
   - utter_greet
* cancel_order
   - utter_ask_account_number_order_id
* cancel_order[order=A8B9V1E9]
   - slot{"order": "A8B9V1E9"}
   - action_check_cancel_details
* cancel_order[account=87630823]
   - slot{"account": "87630823"}
   - action_check_cancel_details
* report_status
   - action_check_cancel_details
* goodbye
   - utter_goodbye
## story_007
* greet
   - utter_greet
* cancel_order
   - utter_ask_account_number_order_id
* cancel_order[order=BSD932X0]
   - slot{"order id": "BSD932X0"}
   - action_check_order_details
* cancel_order[account=09832453]
   - slot{"account": "09832453"}
   - action_check_order_details
* report_status
   - action_check_order_details
* goodbye
   - utter_goodbye
