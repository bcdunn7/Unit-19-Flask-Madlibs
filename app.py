from typing import Text
from flask import Flask, request, render_template

from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

from stories import story

@app.route('/')
def index():
    """Return homepage."""
    
    return render_template("base.html", prompts=story.prompts)

@app.route('/story')
def show_story():
    """Show created madlib"""

    text = story.generate(request.args)

    return render_template("story.html", text=text)