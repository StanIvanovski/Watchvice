#!/usr/bin/env python
# coding: utf-8

# In[110]:


import pandas as pd
realdata = pd.read_csv('../data/mega_cluster_by_movie.csv',sep=",")
realdata

# In[111]:


tagrelevance = pd.read_csv(r'C:\Users\johan\OneDrive\Bureau\ml-25m\genome-scores.csv',sep=",")
df = pd.read_csv(r'C:\Users\johan\OneDrive\Bureau\ml-25m\tags.csv',sep=",")
taglinks = pd.read_csv(r'C:\Users\johan\OneDrive\Bureau\ml-25m\genome-tags.csv',sep=",")
tagrelevance= pd.merge(tagrelevance, taglinks, on=['tagId'])
df_merged = pd.merge(df, tagrelevance, on=['movieId', 'tag'])
df_sorted = df_merged.sort_values('relevance', ascending=False)

# Tri du DataFrame par 'movieId' et 'relevance'
df_sorted = df_sorted.sort_values(by=['movieId', 'relevance'], ascending=[True, False])

# Définition d'une fonction pour obtenir le top 10 des tags
def top_10_tags(group):
    return group.head(10)

# Application de la fonction pour obtenir le top 10 des tags pour chaque 'movieId'
tagstomerge = df_sorted.groupby('movieId').apply(top_10_tags)

# On retire l'index de niveau supérieur créé par groupby
tagstomerge.reset_index(drop=True, inplace=True)

grouped_tags = tagstomerge.groupby('movieId')['tag'].apply(lambda x: ', '.join(x)).reset_index()
realdata = pd.merge(realdata, grouped_tags, on='movieId')


# In[112]:


df


# In[113]:


import streamlit as st
import pandas as pd

# On charge un dataset fictif avec 10 clusters et 3 films par cluster

#example = pd.read_csv(r'C:\Users\johan\OneDrive\Bureau\Example.csv',sep=";")
#example


realdata['MegaCluster']=realdata['mega_label']
realdata['MicroCluster']=realdata['cluster']
realdata['Score']=realdata['coef_age']
realdata['Reco']=realdata['title']
realdata['Tags']=realdata['tag']
realdata.drop(['mega_label','cluster','coef_age','title','centroid','rating','movieId'],axis=1,inplace=True)
realdata = realdata[['Reco', 'Score','Tags','MegaCluster','MicroCluster','popularity']]
example = realdata
#example


# In[114]:


#example[example['Reco']=='Aladdin (1992)']


# In[ ]:





# In[115]:


# On prend le film de chaque cluster ayant le meilleur Score

TopMovies = example.loc[example.groupby('MegaCluster')['popularity'].idxmax()]
#TopMovies


# In[116]:


# On isole la colonne des films

RecommendedMovies = TopMovies['Reco']
RecommendedMovies = RecommendedMovies.reset_index(drop=True)
#RecommendedMovies


# In[117]:


#TopMovies2 = example.loc[example.groupby('MicroCluster')['popularity'].idxmax()]
#TopMovies2


# In[118]:


# On affiche une checkbox qui renvoie un dataframe filtré sur le cluster

st.write("Bonjour monsieur l'utilisateur, veuillez sélectionner votre film préféré dans cette liste et nous vous en suggérerons d'autres similaires.")


for i in range(0, 10):
    if st.checkbox(RecommendedMovies[i]):
        filtereddf = example[example['MegaCluster']==(example[example['Reco'] == RecommendedMovies[i]]['MegaCluster'].values[0])]
        TopMoviesByMicroCluster = (filtereddf.loc[filtereddf.groupby('MicroCluster')['popularity'].idxmax()]).reset_index(drop=True)
        for j in range(len(TopMoviesByMicroCluster)):
            if st.checkbox('    ' + TopMoviesByMicroCluster.iloc[j]['Reco'],key=f'42_{j}'):
                reco_finales = example[example['MicroCluster']==(example[example['Reco'] == TopMoviesByMicroCluster.iloc[j]['Reco']]['MicroCluster'].values[0])]
                st.dataframe(reco_finales.sort_values(by='Score',ascending=False).head(10)) #.iloc[1:11]


# In[ ]:





# In[ ]:





# In[ ]:




