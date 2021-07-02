import plotly.express as px
import csv
"""
#ice cream vs temp
with open("./Ice-Cream vs Cold-Drink vs Temperature - Ice Cream Sale vs Temperature data.csv")as f:
    df1 = csv.DictReader(f)#₹
    figure1 = px.scatter(df1,x = "Temperature",y = "Ice-cream Sales( â‚¹ )")
    figure1.show()
"""
#coffee vs sleep
with open("./cups of coffee vs hours of sleep.csv")as g:
    df2 = csv.DictReader(g)
    figure2 = px.scatter(df2,x = "Coffee in ml",y = "sleep in hours",color = "week")
    figure2.show()

"""
A correlation of 1 means the two datasets are closely correlated. This will be a rising graph where the data points are close to a central line.
A correlation of -1 means that the two data sets are inversely correlated. This will be a falling graph where the data points are close to a central line.
A correlation of 0 means that the two data sets are not correlated at all! The data points will be scattered on the graph.
Correlation always lies between -1 and 1
"""

