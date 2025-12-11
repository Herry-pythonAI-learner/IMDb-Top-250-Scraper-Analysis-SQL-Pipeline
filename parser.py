import os
from bs4 import BeautifulSoup
import pandas as pd
import datetime


#1. Defining the function to parse the moviesn data
def Movies_parser():
    try:
     if not os.path.exists('MoviesCache.html'):
        print('Cache file not found.Please check if the Scraper has run successfully')
        return None
     with open('MoviesCache.html', 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'lxml')
    #Creating the empty list to store the data 
        Movies_list =[]
        print("Parsing the movies data...")
    # Parsing the data by using select and fin methods
        movies = soup.select("li.ipc-metadata-list-summary-item")
        for movie in movies:
            Title = movie.find("h3",class_='ipc-title__text ipc-title__text--reduced').get_text().strip()
            AboutMovies = movie.find_all("span",class_='sc-b4f120f6-7 hoOxkw cli-title-metadata-item')
            Year =AboutMovies[0].get_text().strip()
            Duration = AboutMovies[1].get_text().strip()
            Content_rating =AboutMovies[-1].get_text().strip()
            User_rating = movie.find("span",class_='ipc-rating-star--rating').get_text().strip()
            #APPENDING THE DATA TO THE LIST
            Movies_list.append({
                'Title': Title,
                'Year': Year,
                'Duration': Duration,
                'Content_Rating': Content_rating,
                'User_rating': User_rating

            })
            #Creating the dataframe from the list
        movies_df =pd.DataFrame(Movies_list)
        return movies_df
        
    except Exception as e:
      print(f'An error occured while parsing the data: {e}')

if __name__== "__main__":
    df=Movies_parser()
    print(f'data has been parsed and stored in data frame as follows:\n {df.head()}')

            
