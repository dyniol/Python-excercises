import justpy as jp
import pandas
from datetime import datetime
from pytz import utc
import matplotlib.pyplot as plt

data = pandas.read_csv('3-DataAnalysis/reviews.csv', parse_dates=['Timestamp'])     # reading data from .csv file, more explanation on jupyter notebook
data['Day'] = data['Timestamp'].dt.date
day_average = data.groupby(['Day']).mean()

chart_def = """
{
  chart: {
    type: 'spline',
    inverted: false
  },
  title: {
    text: 'Atmosphere Temperature by Altitude'
  },
  xAxis: {
    reversed: false,
    title: {
      enabled: true,
      text: 'Date'
    },
    labels: {
      format: '{value}'
    },
    maxPadding: 0.05,
    showLastLabel: true
  },
  yAxis: {
    title: {
      text: 'Average Rating'
    },
    labels: {
      format: '{value}'
    },
    lineWidth: 2
  },
  legend: {
    enabled: false
  },
  tooltip: {
    headerFormat: '<b>{series.name}</b><br/>',
    pointFormat: '{point.x} {point.y}'
  },
  plotOptions: {
    spline: {
      marker: {
        enable: false
      }
    }
  },
  series: [{
    name: 'Average Rating',
    data: [[0, 15], [10, -50], [20, -56.5], [30, -46.5], [40, -22.1],
      [50, -2.5], [60, -27.7], [70, -55.7], [80, -76.5]]
  }]
}
""" # importing a HighCharts into a python file

def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(
        a=wp,
        text="Analysis of Course Reviews",
        classes="text-h3 text-center q-pa-md"
    )
    p1 = jp.QDiv(
        a=wp,
        text="These graphs represent course review analysis"
    )
    hc = jp.HighCharts(     # creating a HighCarts object within our 'wp' page, its a js library
        a=wp,
        options=chart_def
    )
    hc.options.title.text = "Average Rating by Day" # we can change everything from the imported graph by accessing values as shown here
    
    hc.options.xAxis.categories = list(day_average.index) # adding categories value to the xAxis and passing the day_average.index to be the xAxis indicator
    hc.options.series[0].data = list(day_average['Rating']) # adding day_average['Rating'] as y Axis
                                                            # those two need to be converted as a list, otherwise program will not work

    return wp
jp.justpy(app)