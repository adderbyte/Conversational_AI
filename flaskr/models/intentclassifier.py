from rasa.nlu.training_data import load_data
#from rasa_nlu.config import RasaNLUModelConfig
from rasa.nlu.model import Trainer
from rasa.nlu import config
from rasa.nlu.model import Metadata, Interpreter
import json
class rasamodel():
	'''
    intent classifier using rasa linraries

    input : data, configuration, model_directory
    output : model_directory, prediction_confidence , intent

	'''
	def __init__(self):
		# this flag checks that we really want to train
		rasamodel.Train = True
	@staticmethod
	def train_nlu(data, configuration, model_dir,train):
		'''
		
        input : 
        		data: training data, in json format
        		configuration: configuration file
        		model_dir: where to save model after training
        		train : flag, to check that we really want to train

        output: 
        		model_directory : where the output model will be saved
		'''
		rasamodel.Train = train
		assert rasamodel.Train ==True
		training_data = load_data(data)
		trainer = Trainer(config.load(configuration))
		trainer.train(training_data)
		model_directory = trainer.persist(model_dir, fixed_model_name = 'Intentnlu')
		return model_directory
	@staticmethod
	def run_nlu(model_directory, input, train ):
		'''
		
        input : 
        		mpodel_directory : directory where trained model was saved
        		train : flag, to check that we really want to test the model.
        		        set this flag to false for testing

        output: 
        		intent : predicted intent
        		confidence: the confidence of such prediction
		'''
		rasamodel.Train = train
		assert rasamodel.Train ==False
		#interpreter = Interpreter.load('./models/nlu/default/customernlu', RasaNLUModelConfig('config_spacy.yml'))
		interpreter = Interpreter.load(model_directory)
		results=interpreter.parse(input)
		#print(results['intent']['confidence'],results['intent']['name'])
		return [ results['intent']['name'] , results['intent']['confidence']]




#### uncomment to run script and test model
#data_path = './data/file.json'
#config_path = 'config_spacy.yml'
#model_save = './intents/nlu/Intentnlu/'
#train = rasamodel()

input = "Guys, I ordered something from you a month ago and nothing has arrived yet, do you have a good reason for this?"
# if you want to train
#model_direc= train.train_nlu(data_path,config_path,model_save)
# if you want to test
#train.run_nlu(model_save,input,train =False)