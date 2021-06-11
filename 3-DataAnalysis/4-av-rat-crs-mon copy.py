import justpy as jp
import pandas
from datetime import datetime
from pytz import utc

data = pandas.read_csv("3-DataAnalysis/reviews.csv", parse_dates=['Timestamp'])
data['Month'] = data['Timestamp'].dt.strftime('%Y-%m')
month_average_course = data.groupby(['Month', 'Course Name']).mean().unstack()

charts_def = """
{
    chart: {
        type: 'spline'
    },
    title: {
        text: 'Average fruit consumption during one week'
    },
    legend: {
        layout: 'vertical',
        align: 'left',
        verticalAlign: 'top',
        x: 150,
        y: 100,
        floating: false,
        borderWidth: 1,
        backgroundColor: '#FFFFFF'
    },
    xAxis: {
        categories: [
            'Monday',
            'Tuesday',
            'Wednesday',
            'Thursday',
            'Friday',
            'Saturday',
            'Sunday'
        ]
    },
    yAxis: {
        title: {
            text: 'Fruit units'
        }
    },
    tooltip: {
        shared: true,
        valueSuffix: ' units'
    },
    credits: {
        enabled: false
    },
    plotOptions: {
        areaspline: {
            fillOpacity: 0.5
        }
    },
    series: [{
        name: 'John',
        data: [3, 4, 3, 5, 4, 10, 12]
    }, {
        name: 'Jane',
        data: [1, 3, 4, 3, 3, 5, 4]
    }]
}
"""

def app():
    wp = jp.QuasarPage() # create variable with QuasarPage()
    h1 = jp.QDiv(
        a=wp,   # need to state to which variable we want to add this div
        text="Analysis of Course Reviews",  # creating divs like in html
        classes="text-h3 text-center q-pa-md")   # classes are on https://quasar.dev/style/ 
    p1 = jp.QDiv(
        a=wp,
        text="These graphs represent course review analysis")

    hc = jp.HighCharts(a=wp, options=charts_def)
    hc.options.xAxis.categories = list(month_average_course.index)
    
    hc_data = [{"name":v1, "data":[v2 for v2 in month_average_course[v1]]} for v1 in month_average_course.columns]
    
    hc.options.series = hc_data

    return wp

jp.justpy(app)