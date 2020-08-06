# Exploratory Analysis of the Studio Ghibli Movies

## Contents
* [Introduction](#intro)
* [Data Collection](#collect)
* [Data Exploration](#explor)

## <a name="intro"></a> Introduction

The Studio Ghibli films have always been many of my favourites, and so I have been eager to create some visualisations of the ratings for these films.

This project has mainly been an opportunity for me to learn how to use an API to query data, so this project is a relatively short one.

The score rating featured from the API is the RT score (Rotten Tomatoes score).
In general, the Tomatometer score represents the percentage of professional critic reviews that are positive for a given film or television show.
More information about this can be [found here.](https://en.wikipedia.org/wiki/Rotten_Tomatoes#Critic_aggregate_score)

## <a name="collect"></a> Data Collection

Data has been collected from the API: https://ghibliapi.herokuapp.com/

Please refer to the [data collection section](https://github.com/nerusn/studio_ghibli_eda/blob/master/collecting_films_data.py) for querying data from the API.

The dataset collected has only 20 rows, since this the number of Studio Ghibli movies.

The available columns from the API are 'id', 'title', 'description', 'director', 'producer', 'release_date' and 'rt_score'. However, the 'id' column and 'description' column is not useful here.

## <a name="explor"></a> Data Exploration

Looking at the scores in descending order, we see that there are two movies with a RT score of 100, decreasing steadily until 75 for the rest of the movies. The lowest rated RT score is 41, which is significantly different from the rest of the scores.

![alt text](https://user-images.githubusercontent.com/60940406/89565760-efaa0a80-d816-11ea-9c60-d2624398d2b4.png)

Now taking a look at the scores, but based on ascending date order. We see that the scores do not show any significant trends over the years, as the scores seem to fluctuate. However, up to the 90s, there is a consistent score above 90.

![alt text](https://user-images.githubusercontent.com/60940406/89565770-f46ebe80-d816-11ea-8d06-ee7e4b701c8f.png)

As an extra, we now look at the distribution of films of different directors. It is clear that Hayao Miyazaki indeed has a largest influence on the Studio Ghibli movies.

![alt text](https://user-images.githubusercontent.com/60940406/89565776-f6d11880-d816-11ea-90c9-259e277037b6.png)
