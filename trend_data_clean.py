from wedge import date_format1
import pandas as pd
from tqdm import tqdm
import argparse
import pickle

def italy_filter(data: str):
    erea = data.split(',')
    country = erea[len(erea)-1].strip()
    if country != 'Italy':
        return True
    else:
        return False
    
def mask_filter(content: str):
    # or ('Mask' in content) or ('Masks' in content)
    if ('Trump' in content) or ('trump' in content):
        return False
    else:
        return True
    
    
def file_load(path: str):
    cov_data = pd.read_csv(path, sep='\t', low_memory=False)
    data = cov_data.drop_duplicates(['Title'])
    #data = data.dropna(subset=["ActionGeo_FullName"])
    data = data.dropna(subset=["Content"])
    positive, normal, negtive = 0, 0, 0
    dim = data.shape[0]
    for cov_line, cov in tqdm(data.iterrows(), total=dim, ncols=80):
        trend = cov['AvgTone']
        country = cov['Actor2Name']
        action_geo = cov['ActionGeo_FullName']
        content = cov['Content']
        
        if mask_filter(content):
            continue
        
        if trend < -2:
            negtive += 1
        if -2 <= trend <=2:
            normal += 1
        if 2 < trend:
            positive += 1
    time = '{}-{}'.format(path[17:19], path[19:21])
    print(negtive, normal, positive, time)
    return (negtive, normal, positive, time)

def the_trend(save_name: str):
    trends = []
    for month in range(1, 4):
        if month == 2:
            days = 30
        else:
            days = 32
        for day in range(1,days):
            path = date_format1(month, day)
            #trends.append(file_load(path))
            
            try:
                trends.append(file_load(path))
            except:
                print("时间无效")
            
    print(trends)
    save_path = './data/result/{}.pkl'.format(save_name)
    with open(save_path, 'wb+') as f:
        pickle.dump(trends, f)
        
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--path_name', type=str, default="global_trend")
    opt = parser.parse_args()
    the_trend(opt.path_name)
    
if __name__ == '__main__':
    main()