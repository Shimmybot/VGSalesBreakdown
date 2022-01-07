# %% [markdown]
# Looking at the top 20 best selling video games, clearly the secret of having a best selling Video game is just be Nintendo. However, what if you're not?

# %% [code] {"_kg_hide-input":true,"execution":{"iopub.status.busy":"2022-01-07T01:04:47.135483Z","iopub.execute_input":"2022-01-07T01:04:47.135866Z","iopub.status.idle":"2022-01-07T01:04:47.222748Z","shell.execute_reply.started":"2022-01-07T01:04:47.135820Z","shell.execute_reply":"2022-01-07T01:04:47.221728Z"}}
# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python Docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load
import ipykernel
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import os

# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os
for dirname, _, filenames in os.walk('./'):
    for filename in filenames:
        print(os.path.join(dirname, filename))


filepath = 'vgsales.csv'
#read csv and drop everything after the first 500 entries
vgdata = pd.read_csv(filepath)
vgdata = vgdata.drop(index=vgdata.index[500:])
vgdata[20:]

# %% [code] {"execution":{"iopub.status.busy":"2022-01-07T01:04:47.224972Z","iopub.execute_input":"2022-01-07T01:04:47.225216Z","iopub.status.idle":"2022-01-07T01:04:47.232773Z","shell.execute_reply.started":"2022-01-07T01:04:47.225188Z","shell.execute_reply":"2022-01-07T01:04:47.231643Z"}}
#Genres
genreList = []
#go through set and make a list of genres to refrence later
for x in vgdata['Genre']:
    if x not in genreList:
        genreList.append(x)
        
print(genreList)

#broken up so you can see the list of genres in order

# %% [code] {"execution":{"iopub.status.busy":"2022-01-07T01:04:47.234411Z","iopub.execute_input":"2022-01-07T01:04:47.235274Z","iopub.status.idle":"2022-01-07T01:04:47.251606Z","shell.execute_reply.started":"2022-01-07T01:04:47.235222Z","shell.execute_reply":"2022-01-07T01:04:47.250930Z"}}
genreSets = []
i = 0
while i < len(genreList):
    #break up the set into sub sets based on genre
    genreSets.append(vgdata.loc[(vgdata['Genre'] == genreList[i])])
    i+= 1
genreSum = []
for x in genreSets:
    genreSum.append(len(x))

# %% [markdown]
# Breaking down the best selling games by Genre 21% of them are Action Games, shooters being the runner up

# %% [code] {"execution":{"iopub.status.busy":"2022-01-07T01:04:47.252828Z","iopub.execute_input":"2022-01-07T01:04:47.253608Z","iopub.status.idle":"2022-01-07T01:04:47.505679Z","shell.execute_reply.started":"2022-01-07T01:04:47.253567Z","shell.execute_reply":"2022-01-07T01:04:47.504774Z"}}
colors = sns.color_palette('muted')

plt.figure(figsize=(16,8))
plt.pie(genreSum, labels = genreList, colors = colors, autopct='%.0f%%',shadow = True)

plt.show()
plt.savefig('Pie-chart-showing-genres')

# %% [code] {"execution":{"iopub.status.busy":"2022-01-07T01:04:47.508189Z","iopub.execute_input":"2022-01-07T01:04:47.508462Z","iopub.status.idle":"2022-01-07T01:04:47.920235Z","shell.execute_reply.started":"2022-01-07T01:04:47.508413Z","shell.execute_reply":"2022-01-07T01:04:47.919346Z"}}
plt.figure(figsize=(16,8))
sns.set_theme(style='darkgrid')
sns.countplot(data=genreSets[0],x=vgdata['Genre'], palette="muted").set(title="Number of Games per Genre")
plt.savefig('Bar-chart-showing-genres')

# %% [markdown]
# Unshockingly, If you're developing for North America or Europe, **Action** and **Shooters** are the genres you'll want to make.
# 
# If you're in Japan, **Role Playing** games are the big winner despite making up 15% of the total pie

# %% [code] {"execution":{"iopub.status.busy":"2022-01-07T01:04:47.921390Z","iopub.execute_input":"2022-01-07T01:04:47.921641Z","iopub.status.idle":"2022-01-07T01:04:48.386071Z","shell.execute_reply.started":"2022-01-07T01:04:47.921611Z","shell.execute_reply":"2022-01-07T01:04:48.385479Z"}}
genreSales = []
i = 0
while i < len(genreSets):
    #create an array to concat into later
    tmpFrame = pd.DataFrame.from_dict({'Genre': genreList[i],
                                       'North America':[genreSets[i]['NA_Sales'].sum()],
                                       'EU':[genreSets[i]['EU_Sales'].sum()],
                                       'Japan':[genreSets[i]['JP_Sales'].sum()],
                                       'Other':[genreSets[i]['Other_Sales'].sum()]})
    genreSales.append(tmpFrame)
    i+=1
#combine frames into one
combinedGenreSales = pd.concat([genreSales[0].set_index('Genre'),
                                genreSales[1].set_index('Genre'),
                                genreSales[2].set_index('Genre'),
                                genreSales[3].set_index('Genre'),
                                genreSales[4].set_index('Genre'),
                                genreSales[5].set_index('Genre'),
                                genreSales[6].set_index('Genre'),
                                genreSales[7].set_index('Genre'),
                                genreSales[8].set_index('Genre'),
                                genreSales[9].set_index('Genre'),
                                genreSales[10].set_index('Genre'),
                                genreSales[11].set_index('Genre')])

combinedGenreSales.plot.bar(title='Regional Game Sales by Genre',figsize=(16,8),ylabel='Sales(In Millions)')
plt.show()
plt.savefig('regional-sales-per-genre')

# %% [code] {"jupyter":{"outputs_hidden":false},"execution":{"iopub.status.busy":"2022-01-07T01:04:48.387281Z","iopub.execute_input":"2022-01-07T01:04:48.388148Z","iopub.status.idle":"2022-01-07T01:04:48.745669Z","shell.execute_reply.started":"2022-01-07T01:04:48.388104Z","shell.execute_reply":"2022-01-07T01:04:48.744766Z"}}
genreSalesGlobal = []
averageGenreSales = []
i = 0
while i < len(genreSets):
    #get global sales 
    tmpFrame = pd.DataFrame.from_dict({'Genre': genreList[i],'Global':[genreSets[i]['Global_Sales'].sum()]})
    genreSalesGlobal.append(tmpFrame)
    #averaging for later chart multiply by 1 million to make scale look better
    avg = (tmpFrame.iloc[0]['Global']/len(genreSets[i]['Name'].sum()))*1000000
    tmpSales = pd.DataFrame.from_dict({'Genre':genreList[i],'Average_Sales':[avg]})
    averageGenreSales.append(tmpSales)
    i+=1
    

combinedGenreSalesGlobal = pd.concat(
    [genreSalesGlobal[0].set_index('Genre'),
     genreSalesGlobal[1].set_index('Genre'),
     genreSalesGlobal[2].set_index('Genre'),
     genreSalesGlobal[3].set_index('Genre'),
     genreSalesGlobal[4].set_index('Genre'),
     genreSalesGlobal[5].set_index('Genre'),
     genreSalesGlobal[6].set_index('Genre'),
     genreSalesGlobal[7].set_index('Genre'),
     genreSalesGlobal[8].set_index('Genre'),
     genreSalesGlobal[9].set_index('Genre'),
     genreSalesGlobal[10].set_index('Genre'),
     genreSalesGlobal[11].set_index('Genre')])


combinedGenreSalesGlobal.plot.bar(figsize=(16,8),ylabel='Sales(In Millions)',title='Global Game Sales by Genre')
plt.show()
plt.savefig('Global-game-sales-by-genre')

# %% [code] {"jupyter":{"outputs_hidden":false},"execution":{"iopub.status.busy":"2022-01-07T01:04:48.747309Z","iopub.execute_input":"2022-01-07T01:04:48.747687Z","iopub.status.idle":"2022-01-07T01:04:49.110380Z","shell.execute_reply.started":"2022-01-07T01:04:48.747629Z","shell.execute_reply":"2022-01-07T01:04:49.109567Z"}}

combinedAvgGenreSalesGlobal = pd.concat(
    [averageGenreSales[0].set_index('Genre'),
     averageGenreSales[1].set_index('Genre'),
     averageGenreSales[2].set_index('Genre'),
     averageGenreSales[3].set_index('Genre'),
     averageGenreSales[4].set_index('Genre'),
     averageGenreSales[5].set_index('Genre'),
     averageGenreSales[6].set_index('Genre'),
     averageGenreSales[7].set_index('Genre'),
     averageGenreSales[8].set_index('Genre'),
     averageGenreSales[9].set_index('Genre'),
     averageGenreSales[10].set_index('Genre'),
     averageGenreSales[11].set_index('Genre')])

combinedAvgGenreSalesGlobal.plot.bar(figsize=(16,8),ylabel='Sales',title='Average Game Sales by Genre')
plt.show()
plt.savefig('Average-game-sales-by-genre')
combinedAvgGenreSalesGlobal

# %% [markdown]
# When it comes to the average sales per game though, Action is one of the loss leaders.
# Barely able to break 250 thousand per game

# %% [code] {"execution":{"iopub.status.busy":"2022-01-07T01:04:49.111532Z","iopub.execute_input":"2022-01-07T01:04:49.111756Z","iopub.status.idle":"2022-01-07T01:04:49.581804Z","shell.execute_reply.started":"2022-01-07T01:04:49.111727Z","shell.execute_reply":"2022-01-07T01:04:49.580970Z"}}
action = genreSets[9]
plt.figure(figsize=(16,8))
sns.set_theme(style='darkgrid')
sns.countplot(data=action,x=action['Platform'], palette="muted").set(
    title='Number of Action Games per System')
plt.savefig('Action-games-per-system')

# %% [markdown]
# Playstation 2 was very popular console for Action games

# %% [markdown]
# looking at 20 publishers with the most games on the list

# %% [code] {"execution":{"iopub.status.busy":"2022-01-07T01:04:49.583055Z","iopub.execute_input":"2022-01-07T01:04:49.583281Z","iopub.status.idle":"2022-01-07T01:04:49.963110Z","shell.execute_reply.started":"2022-01-07T01:04:49.583252Z","shell.execute_reply":"2022-01-07T01:04:49.962254Z"}}
ps2Action = action.loc[action['Platform'] =='PS2']
ps2ActionPublish = ps2Action['Publisher'].to_frame()
ps2ActionSum = ps2ActionPublish.groupby(['Publisher']).size()
ps2ActionSum = ps2ActionSum.to_frame(name='Total_Games').reset_index()
ps2ActionSum.sort_values(by=['Total_Games'],ascending=False,inplace=True)
plt.figure(figsize=(10,5))
sns.set_theme(style='darkgrid')
sns.barplot(x="Total_Games",y="Publisher", data= ps2ActionSum).set(
            title='Publishers of PS2 Action Games')
plt.savefig('PS2-Action-game-Publishers')

# %% [code] {"execution":{"iopub.status.busy":"2022-01-07T01:04:49.964112Z","iopub.execute_input":"2022-01-07T01:04:49.964310Z","iopub.status.idle":"2022-01-07T01:04:49.992555Z","shell.execute_reply.started":"2022-01-07T01:04:49.964284Z","shell.execute_reply":"2022-01-07T01:04:49.991728Z"}}
ps2Action[:20]

# %% [markdown]
# Take Two Interactive:

# %% [code] {"execution":{"iopub.status.busy":"2022-01-07T01:04:49.993779Z","iopub.execute_input":"2022-01-07T01:04:49.994025Z","iopub.status.idle":"2022-01-07T01:04:50.005885Z","shell.execute_reply.started":"2022-01-07T01:04:49.993997Z","shell.execute_reply":"2022-01-07T01:04:50.004995Z"}}
ps2ActionTT = ps2Action.loc[ps2Action['Publisher'] == 'Take-Two Interactive']
ps2ActionTTSample = ps2ActionTT['Name'].to_frame()
ps2ActionTTSample

# %% [markdown]
# Activision:

# %% [code] {"execution":{"iopub.status.busy":"2022-01-07T01:04:50.007367Z","iopub.execute_input":"2022-01-07T01:04:50.007623Z","iopub.status.idle":"2022-01-07T01:04:50.020310Z","shell.execute_reply.started":"2022-01-07T01:04:50.007595Z","shell.execute_reply":"2022-01-07T01:04:50.019736Z"}}
ps2ActionActiv = ps2Action.loc[ps2Action['Publisher'] == 'Activision']
ps2ActionActivSample = ps2ActionActiv['Name'].to_frame()
ps2ActionActivSample

# %% [markdown]
# Sony Computer Entertainment:

# %% [code] {"execution":{"iopub.status.busy":"2022-01-07T01:04:50.022713Z","iopub.execute_input":"2022-01-07T01:04:50.023458Z","iopub.status.idle":"2022-01-07T01:04:50.037285Z","shell.execute_reply.started":"2022-01-07T01:04:50.023402Z","shell.execute_reply":"2022-01-07T01:04:50.036468Z"}}
ps2ActionSCE = ps2Action.loc[ps2Action['Publisher'] == 'Sony Computer Entertainment']
ps2ActionSCESample = ps2ActionSCE['Name'].to_frame()
ps2ActionSCESample

# %% [markdown]
# 

# %% [code] {"execution":{"iopub.status.busy":"2022-01-07T01:04:50.038580Z","iopub.execute_input":"2022-01-07T01:04:50.038880Z","iopub.status.idle":"2022-01-07T01:04:50.285957Z","shell.execute_reply.started":"2022-01-07T01:04:50.038826Z","shell.execute_reply":"2022-01-07T01:04:50.285365Z"}}
ps2TTSales= pd.DataFrame.from_dict({'North America':[ps2ActionTT['NA_Sales'].sum()],
                                    'EU':[ps2ActionTT['EU_Sales'].sum()],
                                    'Japan':[ps2ActionTT['JP_Sales'].sum()],
                                    'Other':[ps2ActionTT['Other_Sales'].sum()]})
sns.set_theme(style="darkgrid")
plt.figure(figsize=(12,6))
plt.xlabel("region",fontsize=12)
plt.ylabel("Sales Figures(in millions)", fontsize=12)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
sns.barplot(data=ps2TTSales,palette='muted').set(title='Take-Two Interactive PS2 Action Games Sales by Region')
plt.savefig('Take-Two-ps2-action-game-sales')

# %% [code] {"execution":{"iopub.status.busy":"2022-01-07T01:04:50.287161Z","iopub.execute_input":"2022-01-07T01:04:50.287625Z","iopub.status.idle":"2022-01-07T01:04:50.750520Z","shell.execute_reply.started":"2022-01-07T01:04:50.287589Z","shell.execute_reply":"2022-01-07T01:04:50.749725Z"}}
actionPublish = action.groupby(['Publisher']).size()
actionPublishSum = actionPublish.to_frame(name='Total_Games').reset_index()
actionPublishSum.sort_values(by=['Total_Games'],ascending=False,inplace=True)
actionPublishSum = actionPublishSum.drop(index=actionPublishSum.index[20:])
plt.figure(figsize=(10,5))
sns.set_theme(style='darkgrid')
sns.barplot(x="Total_Games",y="Publisher", data= actionPublishSum).set(
            title='Top Publishers of Action Games')
plt.savefig('Action-Game-Publishers')

# %% [markdown]
# Once again, we find Nintendo as a Leader

# %% [code] {"_kg_hide-input":true,"execution":{"iopub.status.busy":"2022-01-07T01:04:50.751816Z","iopub.execute_input":"2022-01-07T01:04:50.752031Z","iopub.status.idle":"2022-01-07T01:04:50.765139Z","shell.execute_reply.started":"2022-01-07T01:04:50.752006Z","shell.execute_reply":"2022-01-07T01:04:50.764382Z"}}
nintendo = vgdata.loc[vgdata['Publisher'] == 'Nintendo']
ninAction = nintendo.loc[nintendo['Genre'] == 'Action']
titleCount = len(ninAction)
ninActionSample = ninAction['Name'].to_frame()
ninActionSample[:20]

# %% [code] {"jupyter":{"outputs_hidden":false},"execution":{"iopub.status.busy":"2022-01-07T01:04:50.766275Z","iopub.execute_input":"2022-01-07T01:04:50.766536Z","iopub.status.idle":"2022-01-07T01:04:51.108187Z","shell.execute_reply.started":"2022-01-07T01:04:50.766508Z","shell.execute_reply":"2022-01-07T01:04:51.107477Z"}}
ninActionSales= pd.DataFrame.from_dict({'North America':[ninAction['NA_Sales'].sum()],
                                        'EU':[ninAction['EU_Sales'].sum()],
                                        'Japan':[ninAction['JP_Sales'].sum()],
                                        'Other':[ninAction['Other_Sales'].sum()]})

sns.set_theme(style="darkgrid")
plt.figure(figsize=(12,6))
plt.xlabel("region",fontsize=12)
plt.ylabel("Sales Figures(in millions)", fontsize=12)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
sns.barplot(data=ninActionSales,palette='muted').set(title='Nintendo Action Games Sales by Region')
plt.savefig('Nintendo-Action-Game-Sales')