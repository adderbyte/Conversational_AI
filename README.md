

-------------------------------------

          Requirement installation
------------------------------------

* There is the requirement file. 
* To install the required modules using the requirement file :


`pip install -r requirements.txt`

-------------------------------------

          Install Application
-------------------------------------

*  Then to install the  applicaion :
*  clone the repo and from command line type :

`pip  install -e .`

-------------------------------------

       Running Application
-------------------------------------

*  to launch application

`python run_application.py`

* to run coverage and unit testing

`coverage run -m py.test test_coverage.py `




-------------------------------------

       Good to know things 
-------------------------------------

*  To update any package in case you might need to :
`
pip install package_name -U
`


*  to check what version of a package one currently as : 
`pip freeze | grep package_name`



---------------------------
#### Conversational AI
---------------------------
* Uses :

          * Flask
          * NLTK
          * server API
          * Client API
          * RASA NLU
          * RASA Core 

