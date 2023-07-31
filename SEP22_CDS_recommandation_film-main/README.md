## Explications et Instructions

Ce repository contient les fichiers nécessaires à l'initialisation d'un projet fil-rouge dans le cadre de votre formation [DataScientest](https://datascientest.com/).

Il contient principalement le présent fichier README.md et un template d'application [Streamlit](https://streamlit.io/).

**README**

Le fichier README.md est un élément central de tout repository git. Il permet de présenter votre projet, ses objectifs, ainsi que d'expliquer comment installer et lancer le projet, ou même y contribuer.

Vous devrez donc modifier différentes sections du présent README.md, afin d'y inclure les informations nécessaires.

- Complétez **en anglais** les sections (`## Presentation` et `## Installation` `## Streamlit App`) en suivant les instructions présentes dans ces sections.
- Supprimer la présente section (`## Explications et Instructions`)

**Application Streamlit**

Un template d'application [Streamlit](https://streamlit.io/) est disponible dans le dossier [`streamlit_app`](streamlit_app). Vous pouvez partir de ce template pour mettre en avant votre projet.

## Presentation



This repository contains the code for our project **WATCHVICE**, developed during our [Data Scientist training](https://datascientest.com/en/data-scientist-course) at [DataScientest](https://datascientest.com/).

The goal of this project is to **Recommend Movie to a user**

This project was developed by the following team :

- Johann Schwaller
- Celine Boutry 

You can browse and run the [notebooks](./notebooks). You will need to install the dependencies (in a dedicated environment) :

The notebook are as following :
- WATCHVICE_exploration is the exploration files with the visualisations.
- Watchvice Johann - Reco Final is Clustering based on a genre-based precut, leading to a one-movie recommandation
- reco2_proportionnelle is a clustering based on the Movie tag relevances with 200 clusters to show an example of the researsh to optimize the model
- reco_propor_recent is clustering based on the Movie tag relevances with 100 clusters and a recommendation based on the repartition of the favorites clusters of the users. Recommandation of 5 classic movies (best rated movies of the cluster) and 5 recent movies.
- Watchvice Fusion Reco CélineXJohann is a fusion of the recommendation from Watchvice Johann - Reco Final and reco_propor_recent



```
pip install -r requirements.txt
```

## Streamlit App

**Add explanations on how to use the app.**
1) Scroll down until you reach the checkbox menu
2) Pick your favorite movie
3) A new checkbox menu will load - pick your favorite movie again from that list
4) Movie recommandations are displayed, ranked by quality-relevance score
5) Watch the first movie on the list that you haven't see yet

To run the app :

```shell
cd streamlit_app
conda create --name my-awesome-streamlit python=3.9
conda activate my-awesome-streamlit
pip install -r requirements.txt
streamlit run app.py
```

The app should then be available at [localhost:8501](http://localhost:8501).
