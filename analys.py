import pandas as pd
from tqdm import tqdm
import matplotlib.pyplot as plt
from wedge import self_trend
import matplotlib.ticker as ticker
import pickle
import argparse

def file_filter(data: any):
    return data


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--trend', type=int, default=0)
    parser.add_argument('--situ', type=int, default=0)
    opt = parser.parse_args()
    trend = opt.trend
    situ = opt.situ
    
    tf = open('./data/result/trump_trend.pkl', 'rb+')
    gf = open('./data/result/global.pkl', 'rb+')
    trends = pickle.load(tf)
    confirms = pickle.load(gf)
    tf.close()
    gf.close()
    self_trend(trends, confirms, trend, situ)
    

if __name__ == '__main__':
    main()
        
        