from flask import Flask, url_for, redirect
app = Flask(__name__)

# add an admin route
@app.route('/')
def hello_world():
    return "Hello World"

# add a guest route
@app.route('/guest/<guest>')
def hello_guest(guest):
    # check for admin then redirect
    if guest == 'admin':
        return redirect('/', code=303)
    # otherwise use guest
    return 'Hello %s as Guest' % guest

# run the application
if __name__ == '__main__':
 app.run()