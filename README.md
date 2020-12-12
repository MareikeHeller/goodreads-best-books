## Table of Contents
1. [Installation](#installation)
2. [Project Motivation](#project-motivation)
    * [Questions of Interest](#questions-of-interest)
3. [File Descriptions](#file-descriptions)
4. [Results](#results)
5. [Licensing, Authors, Acknowledgements](#licensing-authors-acknowledgements)

## Installation
The code was developped using Python 3.7.9. Necessary packages are:
- glob
- time
- random
- functools
- pandas
- numpy
- seaborn
- matplotlib
- scikit-learn

The environment can be recreated using the **requirements.txt** or **environment.yml** file in this repository.

## Project Motivation
Using data of a well-know social cataloging web application (Goodreads) on the best books ever according to users' votings, I was interested in the following questions:

### Questions of Interest
1. Is there a shift in popularity measures over time? Are books from certain time periods generally more popular?
2. What genres are most popular and how did genre popularity develop over time?
3. Are readers' ratings on books reflected in winning an award granted by a committee?
4. How well can we predict whether a book will be award winning or not by publicly available data from a social cataloging web application?

## File Descriptions
The jupyter notebook **[best-books-prediction.ipynb]**(https://github.com/MareikeHeller/goodreads-best-books/blob/main/best-books-prediction.ipynb) contains the project code, visualizations and results. 

The input data is provided in an own folder **input_data/goodreads_books_chunk_*** split into 5 .csv files.

## Results
The results to the questions of interest in this project are contained in the respective sections of the [jupyter notebook](https://github.com/MareikeHeller/goodreads-best-books/blob/main/best-books-prediction.ipynb) and further described in this [medium blog post]().
- striking: most books are recent books with a peak around 2013 (mode)
- how reliable are ratings when any user, whether they read the book or not could rate?
- variation reduction by looking at the creme de la creme

## Licensing, Authors, Acknowledgements
The data used in this project is publicly available on [kaggle.com](https://www.kaggle.com/austinreese/goodreads-books) (License: CC0: Public Domain). The data on kaggle was originally scraped from [this Goodreads list](https://www.goodreads.com/list/show/1.Best_Books_Ever). I would like to acknowledge the Stack Overflow community that pushed my learning process. 
