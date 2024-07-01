from flask import Flask, render_template, request
import requests


app= Flask(__name__)

def get_weather_data(city):
   APY_KEY ='e046257c07a0053d2e28ef4fb10d967f'
   url= f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&lang=es&appid={APY_KEY}'
   r = requests.get(url).json()
   return r

@app.route("/", methods=['POST', 'GET'])
def index():
  if request.method == 'POST':
      ciudad=str(request.form.get('txtciudad'))
      if ciudad:
       data=get_weather_data(ciudad)
      return render_template('index.html', context = data)
  return render_template('index.html')
 
 
@app.route("/CV")
def defaz():
    return render_template('CV.html')


@app.route("/login", methods=['POST', 'GET'])
def login():
   if request.method == 'POST':
      USUARIO='ADMIN@ADMIN.COM'
      PASSWORD='ADMIN'
      user= request.form.get("txtemail")
      password= request.form.get("txtpassword")
      if USUARIO == user and PASSWORD == password:
        return render_template('index.html')
      else:
          return render_template('login.html', error=True)
   return render_template('login.html')

@app.route("/registro", methods=['POST', 'GET'])
def registro():
   return render_template('registro.html')

@app.errorhandler(404)
def not_found(error):
   return render_template('error.html'), 404


if __name__ == "__main__":
   app.run(debug = True)


