# My Stock-Ticker Application 

https://zhuyun-maggie-xiao-stockticker.herokuapp.com/index

This project shows a [web app](https://zhuyun-maggie-xiao-stockticker.herokuapp.com/index) that displays user requested stock time series. 
It ties together some important concepts and technologies from the 12-day course, including Git, Flask, JSON, Pandas, Requests, Heroku, and Bokeh for visualization.

## Step 1: Get data from API and put it in pandas
- Use the `requests` library to grab JSON formatted data from a public API -- [Alpha Vantage API](https://www.alphavantage.co/documentation/#). 
- Build in some interactivity by having the user submit a form which determines which data is requested.
- Create a `pandas` dataframe with the data.

## Step 2: Used Bokeh to plot pandas data/ Use Flask for web development
- Created a Bokeh plot to show stock trends.
```
.
├── Procfile
├── README.md
├── __pycache__
│   ├── app.cpython-37.pyc
│   ├── forms.cpython-37.pyc
│   ├── key.cpython-37.pyc
│   └── stocks_data.cpython-37.pyc
├── app.py
├── forms.py
├── key.py
├── requirements.txt
├── runtime.txt
├── stocks_data.py
├── templates
│   ├── graph.html
│   ├── index.html
│   └── structure.html
└── test.ipynb

 ```
