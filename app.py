from flask import Flask, render_template, request, redirect
import requests

from datetime import datetime
import pandas as pd
from pandas import DataFrame, Series

import numpy as np

import bokeh
from bokeh.embed import components
from bokeh.plotting import figure, output_file, show
#link Pandas’ DataFrame with Bokeh visualizations
# Bokeh Object ColumnDataSource accepts DataFrame, pass to glyph 
from bokeh.models import ColumnDataSource
from bokeh.models.tools import HoverTool

from key import key # API Key
import pprint

import stocks_data
##TODO: Fix Hover

# Create an application instance
app = Flask(__name__)
app.vars = {} # dictionary for storing and accessing variables
#===========================================#
@app.route('/')
def main():
    return redirect('/index')

@app.route('/index', methods = ['GET', 'POST'])
def index():
  if request.method == 'GET':
      return render_template('index.html')
  else:
      # request was a POST
      ticker = request.form["ticker"].upper()
      # Create data frame for the ticker (request with API key)
      df = stocks_data.stock_info(ticker)
      # TODO: handle invalid inputs
      # if df is None:
      # return render_template('index.html', error=error)

      # for request sent from checkboxes
      open = request.form.get("open")
      print('open=', open)
   
      inputs = {}
      variables = []
      for checkbox in 'open', 'high', 'low', 'close', 'adjusted_close', 'volume', 'daily_return':
        value = request.form.get(checkbox)
        if value:
          inputs[checkbox] = checkbox
          variables.append(checkbox)
      variables = list(set(variables))
      columns = [inputs[checkbox] for checkbox in variables] 
     
      script, div = stocks_data.plot1(df, ticker, columns)
      
      column = request.form["column"]
      # If none of the checkbox is selected
      if not variables:
        if column not in ('open', 'high', 'low', 'close', 'adjusted_close', 'volume', 'daily_return'):
          return render_template('index.html')
        # for request sent from drop-down menu
        # ticker = request.form["ticker"].upper()
        # Get the selected column from drop-down
        # column = request.form["column"]
        #df = stock_info(ticker)
        else:
          script, div = stocks_data.plot2(df, ticker, column)      
      return render_template('graph.html', script = script, div = div, ticker = ticker)
      
        

'''
@app.route('/test')
def trial():
  names = {'name' : 'Maggie'}
  items = [{'text' : 'First'}, {'text' : 'Second'}, {'text' : 'Third'}, {'text': 'Fourth'}]
  return render_template('layout.html', names = names, language = 'Python', lang = True, framework = 'Flask', items = items)
'''

if __name__ == '__main__':
  #app.run(debug = True)
  app.run(port=33507)
