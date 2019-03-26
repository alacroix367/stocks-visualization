#Load the packages
import pandas as pd
from flask import Flask, render_template
from bokeh.embed import components 
from bokeh.models import HoverTool
from bokeh.plotting import figure

#Connect the app
app = Flask(__name__)

#Helper function
def get_plot(df):
    #Make plot and customize
    xdata = df['sepal_length']
    ydata = df['sepal_width']
    plo = figure(plot_width=400, plot_height=400,title="Sepal width vs. length")
    plo.circle(xdata, ydata)
    plo.xaxis.axis_label = "Sepal Length [cm]"
    plo.yaxis.axis_label = "Sepal Width [cm]"
    plo.title.text_font_size = '16pt'
    plo.add_tools(HoverTool()) #Need to configure tooltips for a good HoverTool

    #Return the plot
    return plo

@app.route('/')
def homepage():

    #Get the data, from somewhere
    df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data',names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'])

    #Setup plot    
    testplot = get_plot(df)
    script, div = components(testplot)

    #Render the page
    return render_template('home_BFHT.html', script=script, div=div)    

if __name__ == '__main__':
    app.run(debug=True) #Set to false when deploying