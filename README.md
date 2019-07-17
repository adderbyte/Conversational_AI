---------------------------
#### Conversational AI
---------------------------
The aim of this project is to deploy a conversational AI developed using the [RASA library](https://rasa.com/docs/rasa/core/slots/)
in  [Flask microframework](http://flask.pocoo.org/).  The models are pretrained and are loaded  in flask api to power the conversation. Using this approach queries from the web interface are answered by the Flask API using the pretrained model. The pretrained model could then be made trained locally conveniently.

---------------------------
#### Conversational AI
---------------------------
* Uses :

          * rasa==1.1.6
          * rasa-core==0.14.5
          * rasa-core-sdk==0.14.0
          * rasa-nlu==0.15.1
          * rasa-sdk==1.1.0
          * Flask==1.1.0
          * nltk==3.2.5
          * spacy==2.0.11
          
        

         

-------------------------------------

         Requirement installation
------------------------------------

* There is the requirement file. 
* To install the required modules using the requirement file :


`pip install -r requirements.txt`

-------------------------------------

          Install Application
-------------------------------------

*  To install the  applicaion 
*  clone the repo and from command line type :

`pip  install -e .`

-------------------------------------

       Running Application
-------------------------------------

*  to launch application

`python run_application.py`

* to run coverage and unit testing

`coverage run -m py.test test_coverage.py `

* to run custom action sever

`cd custom_action_server`

`python -m rasa_sdk.endpoint --actions actions`

*  to retrain the model

       *  `cd flaskr/models/dialogsystem`
       *  Uncomment these 2 lines  at the bottom of the script:
                  `#if __name__ == '__main__':`  and   `#agent = train_dialogue() `
    
-------------------------------------

       Good to know things 
-------------------------------------

*  To update any package in case you might need to :
`
pip install package_name -U
`


*  to check what version of a package one currently has : 
`pip freeze | grep package_name`





