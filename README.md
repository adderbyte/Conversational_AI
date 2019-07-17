---------------------------
#### Conversational AI
---------------------------
The aim of this project is to deploy a conversational AI in flask AI such that the models are pretrained. The pretrained models are preloaded in flask api and are used to answer posted queries (post or get method)

---------------------------
#### Conversational AI
---------------------------
* Uses :

          * Flask
          * NLTK
          * RASA NLU
          * RASA Core 
          

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





