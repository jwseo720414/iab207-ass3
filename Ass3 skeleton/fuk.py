from flask import Flask, request, session

app = Flask(__name__)
app.debug = False
app.secret_key = '123209808'

@app.route('/')
# def landing(name): 
#     # print(request.headers)
#     # print(request.args.get('name'))
#     return '<h1>Hello world ' + name + '</h1>'
def landing():
    # print("Printing the request headers: ")
    # print(request.headers)
    # print("Printing the request argumenets: ")
    # print(request.args)
    return '<h1> hello </h1>'

@app.route('/login')
def set_session():
    session['user']='kermit'
    return '<h1> session has been set </h1>'

@app.route('/checkuser')
def check_session():
    if 'user' in session:
        return '<h1> {} has logged in </h1>'.format(session['user'])
    
    return '<h1>No user has logged in'

@app.route('/logout')
def drop_session():
    if 'user' in session:
        session.pop('user')
    return 'logged out user'

#@app.errorhandler(500)
#def handle_internal_error(error):
#    return '<H1> Sorry your request cannot be processed because of an error</H1>', 500


app.run()