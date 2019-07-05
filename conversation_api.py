#############################################################################################################
# important imports
from flask import request  
from flask import Flask,abort, render_template,redirect,url_for,session, flash,jsonify
#############################################################################################################

#############################################################################################################
# flask configurations 
__author__ = "@olagoke_lukman"
app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
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
         dataSend = jsonify(device = get_v()) # jsonify the data. chnage to json format
    else:
         dataSend = jsonify(device='null') # if none, set message to null
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
    

    '''
    requestType = request.method # get the method type
    

    if requestType == 'POST' or requestType == 'GET': # if method is post ot get 

        #############################################################################################################
        # this block handles the post and get request separately

        if requestType == 'POST': # if post handle it here
            content = request.get_json() # get the json data in the post method. Note this will default to None of no data is sent
            
        else: # if it is a get method handle it below
            if  request.args.get('device') is not None: # ensure it is not none
                devices = request.args['device'] # get the parameters received
                internets = request.args['value'] # get the parameters received
                timestamps = request.args['timestamp'] # get the timestamp received
                content = dict(device =devices, value =internets, timestamp= timestamps ) # put the data received in dictionary
            else: # if the argument in the request is None 
                content = None  # set content to None
    
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

if __name__ == '__main__': 
    app.run(host='0.0.0.0', port= 8090,debug=True)