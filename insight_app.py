import pandas as pd
from sklearn.linear_model import LogisticRegression
from imblearn.over_sampling import SMOTE
import numpy as np
from datetime import date
import streamlit as st

st.header("Court Report")

# current year

current_year = date.today().year

# loading the player_injury dataset 

df_player_injury = pd.read_csv('df_player_injury.csv')

# 1 means injured and 0 means not-injured
    
df_player_injury['injury_10'] = df_player_injury.injury_18.apply(lambda x: 1 if x>0 else 0)
df_player_injury['injury_11'] = df_player_injury.injury_18.apply(lambda x: 1 if x>0 else 0)
df_player_injury['injury_12'] = df_player_injury.injury_18.apply(lambda x: 1 if x>0 else 0)
df_player_injury['injury_13'] = df_player_injury.injury_18.apply(lambda x: 1 if x>0 else 0)
df_player_injury['injury_14'] = df_player_injury.injury_18.apply(lambda x: 1 if x>0 else 0)
df_player_injury['injury_15'] = df_player_injury.injury_18.apply(lambda x: 1 if x>0 else 0)
df_player_injury['injury_16'] = df_player_injury.injury_18.apply(lambda x: 1 if x>0 else 0)
df_player_injury['injury_17'] = df_player_injury.injury_18.apply(lambda x: 1 if x>0 else 0)
df_player_injury['injury_18'] = df_player_injury.injury_18.apply(lambda x: 1 if x>0 else 0)

# filtering for players who played in 2018 

df_player_injury = df_player_injury[df_player_injury['played_18'] == 1]

x = df_player_injury[['height', 'weight', 'G_position', 'F_position', 'C_position', \
                             'years_played_before_2010', 'age_at_2010', 'injury_10', \
                             'injury_11', 'injury_12', 'injury_13', 'injury_14', 'injury_15', \
                             'injury_16', 'injury_17', 'played_10', 'played_11', 'played_12', \
                             'played_13', 'played_14', 'played_15', 'played_16', \
                             'played_17']]
    
# labels column

y = df_player_injury['injury_18']

#Normalizing the data 

#scaler = StandardScaler()

#x = scaler.fit_transform(x)

oversample = SMOTE()

x, y = oversample.fit_resample(x, y)

# Training the model
        
model = LogisticRegression(solver = 'lbfgs')
model.fit(x, y)

# inputs from the user 

num_players = st.number_input('Enter the number of players for whom you want to compare the risk of knee injury', 
                                              min_value = 2, max_value = 10, value = 2, step = 1)

def height_input(i):
    
    height = st.number_input('Eneter the height of player #'+str(i+1), 
                             min_value = 0, max_value = 300, value = 170, step = 1)
    
    return height

def weight_input(i):
    
    weight = st.number_input('Eneter the weight of player #'+str(i+1), 
                             min_value = 0, max_value = 300, value = 80, step = 1)
    
    return weight

def position_input(i):
    
    position = st.radio('Enter the position for player #'+str(i+1),
                        ['Gaurd', 'Forward', 'Center'], 0)
    
    return position

def birth_input(i):
    
    birth = st.number_input('Eneter the birth year of player#'+str(i+1), 
                             min_value = 1950, max_value = 2022, value = 2000, step = 1)
    
    return birth

def start_input(i):
    
    start = st.number_input('Eneter the year that player#'+str(i+1)+' started his career', 
                             min_value = 1950, max_value = 2022, value = 2014, step = 1)
    
    return start

def injury_input(i):
    
    st.write('Enter the history of injuries for player #'+str(i+1))
    
    one = st.checkbox('Player #'+str(i+1)+' had at least one knee injury in year '+str(current_year-8))
    two = st.checkbox('Player #'+str(i+1)+' had at least one knee injury in year '+str(current_year-7))
    three = st.checkbox('Player #'+str(i+1)+' had at least one knee injury in year '+str(current_year-6))
    four = st.checkbox('Player #'+str(i+1)+' had at least one knee injury in year '+str(current_year-5))
    five = st.checkbox('Player #'+str(i+1)+' had at least one knee injury in year '+str(current_year-4))
    six = st.checkbox('Player #'+str(i+1)+' had at least one knee injury in year '+str(current_year-3))
    seven = st.checkbox('Player #'+str(i+1)+' had at least one knee injury in year '+str(current_year-2))
    eight = st.checkbox('Player #'+str(i+1)+' had at least one knee injury in year '+str(current_year-1))
    
    injury_lst_raw = [one, two, three, four, five, six, seven, eight]
    
    injury_lst_processed = [1 if item == True else 0 for item in injury_lst_raw ]
    
    return injury_lst_processed

# organizing the inputs 

full_lst = []

for i in range(num_players):
    
    single_lst = [0] * 23
    
    single_lst[0] = height_input(i)
    
    single_lst[1] = weight_input(i)
    
    position = position_input(i)
    
    if position == 'Gaurd':
        
        single_lst[2] = 1
        
    elif position == 'Forward':
        
        single_lst[3] = 1
        
    else:
        
        single_lst[4] = 1
        
    start = start_input(i)
    
    if start < (current_year - 8):
    
        single_lst[5] = (current_year - 8) - start
        
    single_lst[6] = (current_year - 8) - birth_input(i)
    
    injury_lst = injury_input(i)
    
    single_lst[7: 15] = injury_lst
    
    if start <= (current_year - 8):
        
        single_lst[15: 23] = [1 for i in range(8)]
    
    elif start > (current_year - 8):
        
        diff = start - (current_year - 8)
        
        single_lst[15 + diff: 23] = [1 for i in range(8-diff)]
        
    full_lst.append(single_lst)
    

# calculating probabilities with logistic regression 

calc = st.button('Compute relative probabilities of injury')

if calc:
    
    prob_lst = []
    
    for player_input in full_lst:
        
        probability = model.predict_proba(np.array(player_input).reshape(1, -1))
        
        prob_lst.append(round(probability[0][1], 3))
    
    
    st.write('The following is the list of the players and the estemated relative risk of injury:')
    
    for i in range(num_players):
        
        st.write('Player #'+str(i+1)+' : '+str(prob_lst[i]*100))
