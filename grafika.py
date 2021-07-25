from pylab import rcParams
rcParams['figure.figsize'] = 6,3
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv('C:/Users/user/Desktop/Нетология/01. Подготовка/ds3-spring-2018/1. Intro to Data Science/1.2 Python_vis/video_games_sales.csv')

df = df.dropna()

print([x for x in df.columns if 'Sales' in x])

df1 = df[[x for x in df.columns if 'Sales' in x] + ['Year_of_Release']]\
    .groupby('Year_of_Release').sum()

#df1[list(filter(lambda x: x != 'Global_Sales', df1.columns))]\
#    .plot(kind='bar', rot=45, stacked=True)

#df1[list(filter(lambda x: x != 'Global_Sales', df1.columns))]\
#    .plot(kind='area', rot=45, stacked=False)

#df.Critic_Score.hist(bins=45)
#dx = df.Critic_Score.hist(bins=60)
#dx.set_title('Critic Score distribution')
#dx.set_xlabel('critic score')
#dx.set_ylabel('games')
#df1.plot(kind='bar', rot=45)

#plt.show()

top_developers_df = df.groupby('Developer')[['Global_Sales']].sum()\
    .sort_values('Global_Sales', ascending=False).head(10)

top_developers_df.style.bar()

plt.show()
