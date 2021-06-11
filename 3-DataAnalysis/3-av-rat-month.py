import justpy as jp
import pandas
from datetime import datetime
from pytz import utc

data = pandas.read_csv("3-DataAnalysis/reviews.csv", parse_dates=['Timestamp'])
data['Month'] = data['Timestamp'].dt.strftime('%Y-%m')
month_average = data.groupby(['Month']).mean()

charts_def = """
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
    pointFormat: '{point.y}'
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
"""

def app():
    wp = jp.QuasarPage() # create variable with QuasarPage()
    h1 = jp.QDiv(
        a=wp,   # need to state to which variable we want to add this div
        text="Analysis of Course Reviews",
        classes="text-h3 text-center q-pa-md"   # classes are on https://quasar.dev/style/
    ) # creating divs like in html
    p1 = jp.QDiv(
        a=wp,
        text="These graphs represent course review analysis"
    )

    hc = jp.HighCharts(a=wp, options=charts_def)
    hc.options.xAxis.categories = list(month_average.index)
    hc.options.series[0].data = list(month_average['Rating'])

    return wp

jp.justpy(app)