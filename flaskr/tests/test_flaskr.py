import json
import unittest
#import conversation_api.app as app
from flaskr.conversation_api import app
#set our application to testing mode
app.testing = True
import time
import ast
from flask import request
from multiprocessing import Process
import datetime


class TestApi(unittest.TestCase):

    def test_home(self):
            '''
            Test home page
            '''
            
            client= app.test_client()
            result = client.get(
                    '/home')
            
            self.assertEqual(result.status_code, 200)


    def test_put(self):
            '''
            Test put method . This should abort 
            '''
            
            client= app.test_client()
            result = client.put(
                    '/receivedata?message=I want to cancel my order&timestamp=10/12/2089')

            sent = {"message": "I want to cancel my order","timestamp": "10/01/2089"}

            self.assertEqual(result.status_code, 405)
           

    def test_main(self):
            '''
             Test for when the message body is empty
            '''
            client= app.test_client()
            result = client.post('/receivedata')
            sent =  {'message': "", 'timestamp': ""}
            
            
            self.assertEqual(result.status_code, 200)
            self.assertEqual(ast.literal_eval(result.data.decode('utf-8'))['timestamp'], sent['timestamp'])
            self.assertEqual(ast.literal_eval(result.data.decode('utf-8'))['message'], sent['message'])

    def test_get_method_empty_message(self):
            '''
             Test get method
            '''
            client= app.test_client()
            result = client.get('/receivedata?message=&timestamp=10/12/2089')
            values = ''
    
            self.assertEqual(result.status_code, 200)
            self.assertEqual(ast.literal_eval(result.data.decode('utf-8'))['prediction_confidence'], values)
            self.assertEqual(ast.literal_eval(result.data.decode('utf-8'))['prediction'], values)
            self.assertEqual(ast.literal_eval(result.data.decode('utf-8'))['order_id'], values)
            self.assertEqual(ast.literal_eval(result.data.decode('utf-8'))['suggested_message'], values)
            self.assertEqual(ast.literal_eval(result.data.decode('utf-8'))['order_id'], values)
            self.assertEqual(ast.literal_eval(result.data.decode('utf-8'))['account_number'], values)

    def test_post_method_empty_message(self):
            '''
             Test get method
            '''
            client= app.test_client()
            sent = {"message": "","timestamp": "25/01/2017 10:10:05"}
            result = client.post('/receivedata?', data=json.dumps(sent), 
                     content_type='application/json' ,follow_redirects=True)
            values = ''
    
            self.assertEqual(result.status_code, 200)
            self.assertEqual(ast.literal_eval(result.data.decode('utf-8'))['prediction_confidence'], values)
            self.assertEqual(ast.literal_eval(result.data.decode('utf-8'))['prediction'], values)
            self.assertEqual(ast.literal_eval(result.data.decode('utf-8'))['order_id'], values)
            self.assertEqual(ast.literal_eval(result.data.decode('utf-8'))['suggested_message'], values)
            self.assertEqual(ast.literal_eval(result.data.decode('utf-8'))['order_id'], values)
            self.assertEqual(ast.literal_eval(result.data.decode('utf-8'))['account_number'], values)

    def test_get_empty(self):
            '''
             Test get method
            '''
            client= app.test_client()
            result = client.get('/receivedata?')
            
            values = ''
            
            self.assertEqual(result.status_code, 200)
            


    def test_get_method(self):
            '''
             Test get method
            '''
            client= app.test_client()
            result = client.get('/receivedata?message=I want to cancel my order&timestamp=10/12/2089')
            sent =  {'message': 'I want to cancel my order', 'timestamp': '10/12/2089'}
            
            
            self.assertEqual(result.status_code, 200)
            self.assertEqual(ast.literal_eval(result.data.decode('utf-8'))['message'], sent['message'])
            self.assertEqual(ast.literal_eval(result.data.decode('utf-8'))['timestamp'], sent['timestamp'])


    def test_post_method(self):
            '''
             Check the post method

            '''
            client= app.test_client()
        
            # send data as POST form to endpoint
            time.sleep(0.9)
            
            sent = {"message": "I want to cancel order","timestamp": "25/01/2017 10:10:05"}
            result = client.post(
                    '/receivedata', data=json.dumps(sent), content_type='application/json' ,follow_redirects=True)

            # check that the response status is ok
            
            #self.assertEqual(result.status_code, 200)
            #self.assertEqual(ast.literal_eval(result.data.decode('utf-8'))['message'], sent['message'])
            #self.assertEqual(ast.literal_eval(result.data.decode('utf-8'))['timestamp'], sent['timestamp'])


