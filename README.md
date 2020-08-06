# Exploratory Analysis of the Studio Ghibli Movies

## Contents
* [Introduction](#intro)
* [Data Collection](#collect)
* [Data Exploration](#explor)

## <a name="intro"></a> Introduction

The Studio Ghibli films have always been many of my favourites, and so I have been eager to create some visualisations of the ratings for these films.

This project has been an opportunity for me to learn how to use an API to query data, so this project is a relatively short one.

The score rating featured from the API is the RT score (Rotten Tomatoes score).
In general, the Tomatometer score represents the percentage of professional critic reviews that are positive for a given film or television show.
More information about this can be [found here.](https://en.wikipedia.org/wiki/Rotten_Tomatoes#Critic_aggregate_score)

## <a name="collect"></a> Data Collection

Data has been collected from the API: https://ghibliapi.herokuapp.com/

Please refer to the [data collection section](https://github.com/nerusn/studio_ghibli_eda/blob/master/collecting_films_data.py) for quering data from the API.

The available columns from the API are 'id', 'title', 'description', 'director', 'producer', 'release_date' and 'rt_score'. However, the 'id' column and 'description' column is not useful here.

## <a name="explor"></a> Data Exploration
