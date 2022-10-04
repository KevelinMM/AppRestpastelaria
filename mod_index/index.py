from flask import Blueprint, render_template
bp_index = Blueprint('index', __name__, url_prefix="/", template_folder='templates')

''' rota index '''
@bp_index.route('/')
def formIndex():
    return render_template('formIndex.html'), 200