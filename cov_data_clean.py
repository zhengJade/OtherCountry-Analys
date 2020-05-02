import pandas as pd
import pickle
from tqdm import tqdm
import ast
from wedge import time_str, date_format2
        
def other_pickle(path: str):
    other_data = pd.read_csv(path, keep_default_na=False)
    other_dict = {}
    dim = other_data.shape[0]
    pre_date = ''
    for line, cov in tqdm(other_data.iterrows(), total=dim, ncols=80):
        date = cov['date']
        date = date_format2(date)
        if time_str(date, '01-23') != 1 or time_str(date, '03-30') != -1:
            continue
        confirm = cov['Total confirmed cases']
        dead = cov['Total deaths']
        if dead == '':
            dead = 0
        else:
            dead = int(dead)
        if date == pre_date:
            daily_situation = other_dict[date]
            daily_situation['confirmed'] += confirm
            daily_situation['dead'] += dead
            other_dict[date] = daily_situation
        else:
            init_day = {'confirmed': confirm, 'dead': dead}
            other_dict[date] = init_day
            pre_date = date
    
    print(other_dict)        
    with open('./data/result/other_countery.pkl', 'wb+') as f:
        pickle.dump(other_dict, f)
        

    
def china_pickle(path: str):
    china_data = pd.read_csv(path, keep_default_na=False)
    china_dict = {}
    dim = china_data.shape[0]
    pre_date = ''
    for line, cov in tqdm(china_data.iterrows(), total=dim, ncols=80):
        date = cov['updateTime']
        confirmed = cov['confirmedCount']
        dead = cov['deadCount']
        date = date_format2(date)
        if time_str(date, '01-23') != 1 or time_str(date, '03-30') != -1:
            continue
        if date != pre_date:
            unit_dict = {'confirmed': confirmed, 'dead': dead}
            china_dict[date] = unit_dict
            pre_date = date
        else:
            continue
    print(china_dict)
    
    with open('./data/result/china.pkl', 'wb+') as f:
        pickle.dump(china_dict, f)
        
def global_pickle(china_path: str, other_path: str, globel_path: str):
    with open(china_path, 'rb+') as cf, open(other_path, 'rb+') as of, open(globel_path, 'wb+') as gf:
        china_dict = pickle.load(cf)
        other_dict = pickle.load(of)
        global_dict = {}
        for date in china_dict.keys():
            china_unit = china_dict[date]
            other_unit = other_dict[date]
            global_unit = {'confirmed': china_unit['confirmed'] + other_unit['confirmed'], 'dead': china_unit['dead'] + other_unit['dead']}
            global_dict[date] = global_unit
        
        print(global_dict)
        pickle.dump(global_dict, gf)

def italy_pickle(italy_path: str):
    italy_data = pd.read_csv(italy_path, keep_default_na=False)
    italy_dict = {}
    dim = italy_data.shape[0]
    start_day = ''
    for line, cov in italy_data.iterrows():
        country = cov['Country/Territory/Area']
        if country != 'Italy':
            continue
        start_day = date_format2(cov['date']) 
        break
        
    for line, cov in tqdm(italy_data.iterrows(), total=dim, ncols=80):
        date = cov['date']
        date = date_format2(date)
        if time_str(start_day, date) == 1 or time_str(date, '01-23') != 1 or time_str(date, '03-30') != -1:
            init_day = {'confirmed': 0, 'dead': 0}
            italy_dict[date] = init_day
            continue
        
        country = cov['Country/Territory/Area']
        if country != 'Italy':
            continue
         
        confirm = cov['Total confirmed cases']
        dead = cov['Total deaths']
        if dead == '':
            dead = 0
        else:
            dead = int(dead)
            
        init_day = {'confirmed': confirm, 'dead': dead}
        italy_dict[date] = init_day
    
    print(italy_dict)        
    with open('./data/result/Italy.pkl', 'wb+') as f:
        pickle.dump(italy_dict, f)
    
def main():
    other_path = './data/2019CoV/data-who.csv'
    global_path = './data/2019CoV/DXYOverall.csv'
    china_path = './data/2019CoV/DXYOverall.csv'
    #other_pickle(other_path)
    #china_pickle(china_path)
    #global_pickle('./data/result/china.pkl', './data/result/other_country.pkl', './data/result/global.pkl')
    #italy_pickle(other_path)
    '''
    with open('./data/result/Italy.pkl', 'rb+') as f:
        italy_dict = pickle.load(f)
        temp = italy_dict['03-20']
        italy_dict['03-20'] = italy_dict['03-18']
        italy_dict['03-18'] = temp
        pickle.dump(italy_dict, f)
        print(italy_dict)
        
    ''' 

if __name__ == '__main__':
    main()