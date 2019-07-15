from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging
import asyncio


from rasa.core.agent import Agent
from rasa.core.run import serve_application
from rasa.core import config
import rasa.core
from rasa.utils.endpoints import EndpointConfig
#from rasa_core.channels.console import ConsoleInputChannel
from rasa.core.interpreter import RegexInterpreter
from rasa.core.policies.keras_policy import KerasPolicy
from rasa.core.policies.memoization import MemoizationPolicy
from rasa.core.interpreter import RasaNLUInterpreter
from rasa.core.featurizers import MaxHistoryTrackerFeaturizer, BinarySingleStateFeaturizer

#from rasa_core.train import online
#rasa_core.run.serve_application(agent ,channel='cmdline')
logger = logging.getLogger(__name__)
#@asyncio.coroutine
def train_dialogue(domain_file = 'customer_domain.yml',
                    model_path = './models/dialogue',
                    training_data_file = 'stories.md'):
    '''
    This function uses the intent clasifier to build responses to sent messages

    input : 
          domain_file : containing the actions, templates , entities necessary for underdtanding the dialogue.The file
                        is located in the dialogue system
          model_path  : directory for saving trained dialogue system 
          training_data_file :  contains the story file. It is training file needed to train rasa core dialogue system   


    '''
    featurizer = MaxHistoryTrackerFeaturizer(BinarySingleStateFeaturizer(), max_history=5) # define featurizer  for learning
    # define a bot agent 
    agent = Agent(domain_file, policies = [MemoizationPolicy(), KerasPolicy(featurizer, epochs=300, batch_size=10)])
    
    # asyncio is needed for concurrent wait during training
    loop = asyncio.get_event_loop() # define asyncio
    data = loop.run_until_complete( agent.load_data(training_data_file )) # embedded data in asyncio
    
    # let agent train
    agent.train(
                data, validation=0.2)
    # persistent saving of model
    agent.persist(model_path)
    # return agent
    return agent
#####uncomment to run script as is or test model
#if __name__ == '__main__':
     #agent = train_dialogue() # train a model
     #loop = asyncio.get_event_loop() # call asyncio
    
     #interpreter = RasaNLUInterpreter('../intents/nlu/Intentnlu/') # interpreter is the intent classifier

     #agent = Agent.load('./models/dialogue', interpreter = interpreter) # load dialogue agent

     #b = loop.run_until_complete(agent.handle_text('Hello! How can I help?')) # test agent response
   
   
     #print(b) # print response
     #loop.close() # close loop
   