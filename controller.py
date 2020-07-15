from flask import render_template
from config import app



def main():
    print("*"*40)
    return render_template("main.html")

def cont_grid():
    return render_template("containers_grids.html")

def fake_blog():
    return render_template("fake_blog.html")

def text():
    return render_template("text_typography.html")

