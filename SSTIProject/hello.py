from flask import Flask,render_template_string,request
app = Flask(__name__)

@app.route('/',methods=['GET'])
def home():
	temp = {'name':'Rahul','password':'12345678'}
	if request.args.get('name'):
		temp['name'] = request.args.get('name')
	template = '<h2>Hey %s </h2>' %temp['name']
	return render_template_string(template,temp=temp)