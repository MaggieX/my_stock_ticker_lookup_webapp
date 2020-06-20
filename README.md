# Stock Ticker Application 

This TDI onboarding project shows a [web app](https://zhuyun-maggie-xiao-stockticker.herokuapp.com/index) that displays user requested stock information. It ties together some important concepts and technologies from the 12-day course, including Git, Flask, JSON, Pandas, Requests, Heroku, and Bokeh for visualization.

## Flask on Heroku Project steps

## Step 1: Get data from API and put it in pandas
- Use the `requests` library to grab some data from a public API -- [Alpha Vantage API](https://www.alphavantage.co/documentation/#). The data is in JSON format, in which case `simplejson` will be useful.
- Build in some interactivity by having the user submit a form which determines which data is requested.
- Create a `pandas` dataframe with the data.

## Step 2: Use Bokeh to plot pandas data/ Use Flask for web development
- Create a Bokeh plot from the dataframe.
- Consult the Bokeh [documentation](http://bokeh.pydata.org/en/latest/docs/user_guide/embed.html)
  and [examples](https://github.com/bokeh/bokeh/tree/master/examples/embed).
- Make the plot visible on your website through embedded HTML or other methods - this is where Flask comes in to manage the interactivity and display the desired content.
- Some good references for Flask: [This article](https://realpython.com/blog/python/python-web-applications-with-flask-part-i/), especially the links in "Starting off", and [this tutorial](https://github.com/bev-a-tron/MyFlaskTutorial).
