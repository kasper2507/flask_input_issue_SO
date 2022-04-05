from flask import Flask, render_template
from udlaan import UdlaanForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'nogethemmeligt'

@app.route('/', methods=['GET', 'POST'])
def start():
    uform =  UdlaanForm()
    print('Running')
    
    if uform.validate_on_submit():
        print('Validated')
        print(uform.errors)


    print(uform.errors) 
    print('ending')
    return render_template('start.html', form = uform)
    
if __name__ == '__main__':
    app.run(host='127.0.0.1', port='5000', debug=True)


