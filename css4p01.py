#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 14:59:38 2024

@author: wonder
"""

import pandas as pd 

movie_data = pd.read_csv('movie_dataset.csv', index_col=0)
df = pd.DataFrame(movie_data)
print(df)

#df = df.dropna()
#print(df)

#pd.set_option('display.max_row', None)

#print(df)

#print(df['Genre'])

duplicates = df.duplicated()

duplicate_row = df[df.duplicated()]

null_value_check = df.isnull()

null_rows = df[df.isnull().any(axis=1)]


#print(duplicate_row)
#print(duplicates)

print(df.isnull())

print(null_rows)

df = df.dropna()
df = df.reset_index(drop=True)

#df['Year'] = pd.to_datetime(df['Year'])
#print(df['Metascore'].min())
#print(df['Metascore'].max())
#print(df['Metascore'].mean())
#df.rename(columns={'Revenue(Millions)': 'Revenue'}, inplace=True)

#drop_null_values = df.drop

#average_metascore = df['Metascore'].mean

#df['Metascore'].fillna(average_metascore)

#print(df)

highest_rating = df['Rating'].max()
highest_rated_movie = df[df['Rating']==highest_rating]
print('highest rated movie is:', highest_rated_movie)

highest_revenue = df['Revenue (Millions)'].max()
print('highest revenue is:', highest_revenue)
highest_revenue_movie = df[df['Revenue (Millions)']==highest_revenue]
print('highest revenue movie is:', highest_revenue_movie)

average_movies_revenue = df['Revenue (Millions)'].mean()
print('average movie revenue is:', average_movies_revenue)

#print(df.columns)

#range_year = pd.date_range(start='2015', end='2017', freq='Y').year
#print(range_year)

#import numpy as np 

filter_by_year = df[(df['Year'] >= 2015) & (df['Year'] <= 2017)]
print(filter_by_year)

average_revenue_for_date_filtered = filter_by_year['Revenue (Millions)'].mean()
print(average_revenue_for_date_filtered)

movies_in_2016 = movie_data[(movie_data['Year'] == 2016)]
movies_in_2016 = movies_in_2016.reset_index(drop=True)

number_in_2016 = len(movies_in_2016)

print(movies_in_2016, number_in_2016)

movie_nolan = movie_data[(movie_data['Director'] == 'Christopher Nolan')]
num_nolan =len(movie_nolan)
print(movie_nolan, num_nolan)
nolan_rating = movie_nolan['Rating'].mean()
print('average rating is:', nolan_rating)

movie_rating = movie_data[(movie_data['Rating'] >= 8.0)]
num_rating =len(movie_rating)
print(movie_rating, num_rating)

max_rating = movie_data['Rating'].max()
print('max rating is:', max_rating)
year_max_rating = movie_data[(movie_data['Rating'] == max_rating)]
print('year of max rating is:', year_max_rating)

movies_2006 = movie_data[(movie_data['Year'] == 2006)]
num_movies_2006 = len(movies_2006)
print('number of movies in 2006 is:', num_movies_2006)
print(movies_2006)

movies_2007_2016 = movie_data[(movie_data['Year'] >= 2006) & (movie_data['Year'] <= 2016)]
num_movies_2007_2016 = len(movies_2007_2016)
print('number of movies from 2007 to 2016 is:', num_movies_2007_2016)
print(movies_2007_2016)


percentage_increase = ((num_movies_2007_2016 - num_movies_2006) / num_movies_2006) * 100
print(percentage_increase)