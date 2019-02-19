# -*- coding: utf-8 -*-

# Note: import the app of what you are working on
from vis_line_chart import app
# from exercise1 import app
# from exercise2 import app
# from exercise2 import app

server = app.server

if __name__ == '__main__':
    # start the Dash app
    app.run_server(debug=True)



