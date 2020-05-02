import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.ticker as ticker
from wedge.tools import time_str
from scipy.interpolate import make_interp_spline
import numpy as np


plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False

def self_trend(trends: any, confirms: any, trend: int, situ: int):
    x_time = []
    y_trend = []
    y_confirm = []
    y_dead = []
    trends_dict = {0:"消极占比", 1:"中性占比", 2:"积极占比"}
    situation_dict = {0: "confirmed", 1: "dead"}
    for one_trends in trends:
        x_time.append(one_trends[3])
        if (one_trends[0]+one_trends[1]+one_trends[2]) == 0:
            y_trend.append(0)
        else:
            y_trend.append(one_trends[trend]/(one_trends[0]+one_trends[1]+one_trends[2]))
        
        if time_str(one_trends[3], '01-24') == -1:
            y_confirm.append(0)
            y_dead.append(0)
            continue
        
        value = confirms[one_trends[3]]
        y_confirm.append(value['confirmed'])
        y_dead.append(value['dead'])
        
    
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    tick_spacing = 5
    ax1.plot(x_time, y_trend, 'g', label=trends_dict[trend])
    ax1.set_ylabel('情感倾向', fontsize=14)
    ax1.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
    ax2 = ax1.twinx()
    ax2.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
    ax2.plot(x_time, y_confirm, 'r', label=situation_dict[situ])
    ax2.set_ylabel('疫情情况', fontsize=14)
    ax1.legend()
    ax2.legend()
    plt.show()