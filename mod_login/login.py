from flask import Blueprint, render_template
bp_login = Blueprint('login', __name__, url_prefix="/login", template_folder='templates')

''' rotas dos formulários '''

@bp_login.route('/', methods=['GET', 'POST'])
def formLogin():
    return render_template('formLogin.html')
