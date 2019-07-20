----------------
### Flask Application
-----------------

The main control logic for thr web template and API interation is the `conversation_api.py` file.  

The intent classifier is trained separately from the dialogue generator. The dialogue generator uses the prediction of the intent classifier to give a response.
