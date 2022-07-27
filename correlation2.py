import csv
import plotly.express as px
import numpy as np
def plotFigure(datapath):
    with open('cups of coffee vs hours of sleep.csv') as e:
        reader=csv.DictReader(e)
        line=px.scatter(reader,x='Coffee in ml',y='sleep in hours')
        line.show()
def getDataSource(datapath):
    cupsofcoffee=[]
    hoursofsleep=[]
    with open(datapath) as e:
        reader=csv.DictReader(e)
        for r in reader:
            cupsofcoffee.append(float(r['Coffee in ml']))
            hoursofsleep.append(float(r['sleep in hours']))
    return {"x":cupsofcoffee,"y":hoursofsleep}
def findCorrelation(datasource):
    calcu=np.corrcoef(datasource["x"],datasource["y"])
    print(calcu[0,1])
datapath='cups of coffee vs hours of sleep.csv'
datasource=getDataSource(datapath)
plotFigure(datapath)
findCorrelation(datasource)