from config import app
from controller import main, cont_grid, fake_blog, text 


app.add_url_rule("/", view_func=main)
app.add_url_rule("/containers_grids", view_func=cont_grid)
app.add_url_rule("/fake_blog", view_func=fake_blog)
app.add_url_rule("/typography", view_func=text)
