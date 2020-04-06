from flask import Response, request
from flask import Flask
from flask import render_template, make_response, redirect, url_for
from flask import flash
from flask import g

# Rendering a Page Template
app = Flask(__name__,
            template_folder='templates')


# defining routing
@app.route('/')
def home():
    """Serve homepage template."""
    return render_template('index.html',
                           title='Flask-Login Tutorial',
                           body='You are now logged in')


# HTTP Methods
@app.route('/api/v1/users', methods=['GET', 'POST', 'PUT'])
def users():
    return 'Users'


# Making a Response Object
@app.route('/api/v2/test_response')
def users2():
    headers = {'Content-Type': 'application/json'}
    return make_response(Response('Test worked', headers=headers), 200)


# Route variable Rules
@app.route('/user/<username>')
def profile(username):
    return username


@app.route('/date/<int:year>/<int:month>/<title>')
def article(year, month, title):
    return f'{year}/{month}: {title}'


# Redirecting Users
@app.route('/dashboard')
def dashboard_url():
    return redirect('/dashboard.html')


@app.route('/login')
def login():
    # accepts the name of a route function
    return redirect(url_for('dashboard_url'))


# The Request Object -> Example(not working)
@app.route('/signup', methods=['GET', 'POST'])
def signup_page():
    """User sign-up page."""
    signup_form = SignupForm(request.form)
    # POST: Sign user in
    if request.method == 'POST':
        if signup_form.validate():
            # Get Form Fields
            name = request.form.get('name')
            email = request.form.get('email')
            password = request.form.get('password')
            website = request.form.get('website')
            existing_user = User.query.filter_by(email=email).first()
            if existing_user is None:
                user = User(name=name,
                            email=email,
                            password=generate_password_hash(password, method='sha256'),
                            website=website)
                db.session.add(user)
                db.session.commit()
                login_user(user)
                return redirect(url_for('main_bp.dashboard'))
            flash('A user already exists with that email address.')
            return redirect(url_for('auth_ap.signup_page'))
    # GET: Serve Sign-up page
    return render_template('/signup.html',
                           title='Create an Account | Flask-Login Tutorial',
                           form=SignupForm(),
                           template='signup-page',
                           body='Sign up for a user account.')   


# The g Object
@app.route('/test_value/get')
def get_test_value():
    if 'test_value' not in g:
        g.test_value = 'This is a value'
    return g.test_value


@app.route('/test_value/pop')
def remove_test_value():
    test_value = g.get('test_value', '')
    return test_value


# Error Routes
@app.errorhandler(404)
def notfound():
    """Serve 404 template."""
    return make_response(render_template('404.html'), 404)


if __name__ == '__main__':
    app.run(debug=True)