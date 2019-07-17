---------------------------
#### Conversational AI
---------------------------
The aim of this project is to deploy a conversational AI developed using RASA library in  flask environment.  The models are pretrained and are loaded  in flask api to power the conversation. Using this approach queries from the web interface are answered.

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
          * 
community@rasa.com!          

         

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
`
cd path_to_this_folder
`
`
python -m rasa_sdk.endpoint --actions actions
`




-------------------------------------

       Good to know things 
-------------------------------------

*  To update any package in case you might need to :
`
pip install package_name -U
`


*  to check what version of a package one currently has : 
`pip freeze | grep package_name`





