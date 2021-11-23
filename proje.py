import pandas as pd
import plotly.figure_factory as pf
import statistics 
import random
import plotly.graph_objects as pg
import csv


df=pd.read_csv("P/data.csv")
data=df["Math_score"].tolist()
mean=statistics.mean(data)
stdev=statistics.stdev(data)

def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index= random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

meanlist=[]
for i in range(0,1000):
    setofmean=random_set_of_mean(100)
    meanlist.append(setofmean)

std_deviation=statistics.stdev(meanlist)
first_std_deviation_start, first_std_deviation_end = mean-std_deviation, mean+std_deviation
second_std_deviation_start, second_std_deviation_end = mean-(2*std_deviation), mean+(2*std_deviation)
third_std_deviation_start, third_std_deviation_end = mean-(3*std_deviation), mean+(3*std_deviation)


graph=pf.create_distplot([meanlist],["student marks"],show_hist=False)
graph.add_trace(pg.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
graph.add_trace(pg.Scatter(x=[first_std_deviation_end,first_std_deviation_end],y=[0,0.17],mode="lines",name="stdev first end"))
graph.add_trace(pg.Scatter(x=[second_std_deviation_end,second_std_deviation_end],y=[0,0.17],mode="lines",name="stdev second end"))
graph.add_trace(pg.Scatter(x=[third_std_deviation_end,third_std_deviation_end],y=[0,0.17],mode="lines",name="stdev third end"))


'''def showgraph(mean):
    graph=pf.create_distplot([mean],["temp"],show_hist=False)
    graph.add_trace(pg.Scatter(x=[mean,mean],y=[0,1],mode="lines",name="MEAN"))'''
graph.show()