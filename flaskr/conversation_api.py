#############################################################################################################
# important imports
from flask import request  
import datetime
from flask import Flask,abort, render_template,redirect,url_for,session, flash,jsonify
import re
import os

# imports for chatbox
from flaskr.models.intentclassifier import rasamodel # to classifier cancel or order status intent.
from flaskr.models.dialogsystem.dialog import train_dialogue 
from rasa.core.interpreter import RasaNLUInterpreter
import asyncio
from rasa.core.agent import Agent
import nltk

### find root . Useful for loading models
SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
#############################################################################################################



#############################################################################################################
# flask configurations 
__author__ = "@olagoke_lukman"
app = Flask(__name__)
#app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False
#############################################################################################################



#############################################################################################################
# This block contains python class that holds a python class variable
@app.before_first_request
class checkers():
    '''
    This class  defines a class variable that will persistent
    globally across different request. It will hold the messsage content
    and will only change when a new message is received.
    
    This variable is linked to the jquery script in the webpage. 
    The jquery automatically check for change in this variable and update it on web page

    '''
    def __init__(self):
        checkers.checker = None  # this is the class variable. It is initialised to none here

    #############################################################################################################
    # define a static method for setting class variable value
    @staticmethod
    def datac(data):
        '''
        Functon to set the new value of the class variable

        input : new message from a post
        output : class variable


        '''
        #print(data)
        checkers.checker = data # assign class variable to new value
        return checkers.checker  # return class variable

#############################################################################################################
# these 2 functions call the class above to set or get its class variable. They are the setters and getters for the class variable
def set_v(data):
    '''
    set the value for the class avriable
    input : data
    '''
    checkers.datac(data)
def get_v():
    '''
    input: nill
    output : class variable checkers.check
    '''
    return checkers.checker

# declare the intent classifier class here 
intentClassifier = rasamodel()
## path to saved intent classifier
model_save= os.path.join(SITE_ROOT, "models/intents/nlu/Intentnlu/")
dialogue_save = os.path.join(SITE_ROOT, "models/dialogsystem/models/dialogue")
## Instantiate dialogue system
def suggestedMessage(model_save,dialogue_save,text):
    '''
    Function to return suggested message from Bot
    '''
    asyncio.set_event_loop(asyncio.new_event_loop())
    loop = asyncio.get_event_loop() # call asyncio
    #asyncio.set_event_loop(loop)
    
    #train_dialogue()
    interpreter = RasaNLUInterpreter(model_save) # interpreter is the intent classifier
    agent = Agent.load(dialogue_save, interpreter = interpreter) # load dialogue agent
    botMessage = loop.run_until_complete(agent.handle_text(text)) # test agent response agent.handle_text(text)#
    #print(botMessage) # print response
    loop.close() # close loop
    return botMessage
#############################################################################################################



#############################################################################################################
# route directory. This redirects to Home
@app.route("/")
def reset():
    '''
    the root directors redirects to home page
    '''
    return redirect(url_for('template_test'))

# Home directory 
@app.route("/home")
def template_test():
    '''
    this defines home page. The main page of the web interface
    '''
    #print('session data',get_v())
    if get_v() is not None: # check that the class variable is not None. None would mean no message has been received
         dataSend = jsonify(message = get_v()) # jsonify the data. chnage to json format
    else:
         dataSend = jsonify(message='null') # if none, set message to null
    return render_template('index.html', data=dataSend) # render the page
#############################################################################################################


#############################################################################################################
# the function to handle messages received
# messages can be received through get or post methods
@app.route('/receivedata', methods = ['GET','POST'])
def sharedata():
    '''
    This class handles the messages received . And also return new messages to jquery in index.html
    The jquery update the message and response

    datetime stamp format to be used {:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())

    '''
    requestType = request.method # get the method type
    

    if requestType == 'POST' or requestType == 'GET': # if method is post ot get 

        #############################################################################################################
        # this block handles the post and get request separately

        if requestType == 'POST': # if post request handle it here
            content = request.get_json() # get the json data in the post method. Note this will default to None of no data is sent
            if content is not None:
                messages = str(content['message'])
                timestamps = content['timestamp']
                if not messages:
                    predictions , predictions_confidence= '', ''
                    order_id , account_number='', ''
                    suggested_message = ''
                else:
                    # suggest a message
                    suggested_message = suggestedMessage(model_save,dialogue_save,messages)
                    
                    suggested_message = suggested_message[0]['text']
                    # predictions
                    predictions , predictions_confidence = intentClassifier.run_nlu(model_save,messages,train =False)

                    # tokenize text and extarct order id or account number 
                    text_ = nltk.word_tokenize(messages)
                    order_id = [ s for s in text_  if re.match('^(?=.*[0-9]$)(?=.*[a-zA-Z])', s)  ]
                    account_number = [ s for s in text_  if s.isdigit() ]

                content = dict(message =messages, timestamp= timestamps, prediction = predictions , 
                                prediction_confidence = predictions_confidence,
                                suggested_message=suggested_message,order_id=order_id, account_number = account_number ) # put the data received in dictionary
            else:
                predictions , predictions_confidence = '', ''
                messages,timestamps= '',''
                order_id,suggested_message = '',''
                account_number = ''
                content = dict(message =messages, timestamp= timestamps, prediction = predictions , 
                                prediction_confidence = predictions_confidence , suggested_message = suggested_message, order_id = order_id, account_number = account_number) # put the data received in dictionary


        else: # if it is a get method handle it below
            if  request.args.get('message') is not None: # ensure it is not none
                messages = str(request.args['message']) # get the parameters received
                timestamps = request.args['timestamp'] # get the timestamp received
                if not messages:
                    predictions  = ''
                    predictions_confidence =  ''
                    suggested_message = ''
                    account_number = ''
                    order_id = ''
                    
                else:
                    suggested_message = suggestedMessage(model_save,dialogue_save,messages)
                    suggested_message = suggested_message[0]['text']
                    predictions , predictions_confidence = intentClassifier.run_nlu(model_save,messages,train =False)

                    text_ = nltk.word_tokenize(messages)
                    order_id = [ s for s in text_  if re.match('^(?=.*[0-9]$)(?=.*[a-zA-Z])', s)  ]
                    account_number = [ s for s in text_  if s.isdigit() ]
                
                content = dict(message =messages, timestamp= timestamps, prediction = predictions , 
                            prediction_confidence = predictions_confidence,suggested_message=suggested_message, 
                            order_id = order_id, account_number = account_number ) # put the data received in dictionary


            else: # if the argument in the request is None , Important for synchronization with jquery reques
                content = None # set this to None because the jquery script. Otherwise no value will be displayed 
    
        #############################################################################################################    

        #############################################################################################################
        # this block processes the variable content receivec in the previous block
        # the processing depends on whether it is None or not

        if content is not None: # if content variable is not None. Meaning a new data arrived
        
            set_v(content) # set the value of the class variable to the new data
            #print('I am set', get_v())
            #print('I am here ',session['data'])

            
            return jsonify(content) # jsonify the content
        else: # if content is None. Not data received
             
             #print('first test',get_v())
             if get_v() is not None: # check if the class variable is not None. If it is not None , this means a previous message
                                     # is existing. Thus keep displaying this message
                #print('I got it')
                return jsonify(get_v()) # jsonify the previous message
             else:
                return 'ok'#jsonify(device='null')  print ok . This will not be displayed in the browser
        #############################################################################################################
    else :
        return abort(405) #  request is not the right type (post or get) then abort
#############################################################################################################


#if __name__ == '__main__': 
#    app.run(host='0.0.0.0', port= 5000,debug=True)