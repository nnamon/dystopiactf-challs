from bottle import get, post, request, run # or route

FLAG = "flag{I_l15t3n_2_d3bu55y}"

def check_login(username, password):
    if username != "iwantacookie":
        return False
    if password != "subAt0micH4mst3rs":
        return False
    return True

@get('/') # or @route('/login')
def login():
    return '''
        <form action="/" method="post">
            Username: <input name="username" type="text" />
            Password: <input name="password" type="password" />
            <input value="Login" type="submit" />
        </form>
    '''

@post('/') # or @route('/login', method='POST')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    if check_login(username, password):
        return "<p>Here's a cookie for you: %s</p>" % FLAG
    else:
        return "<p>Login failed. I'm sorry</p>"

run(port=6669)
