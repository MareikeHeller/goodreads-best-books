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

The environment can be recreated using the [requirements.txt](https://github.com/MareikeHeller/goodreads-best-books/blob/main/requirements.txt) or [environment.yml](https://github.com/MareikeHeller/goodreads-best-books/blob/main/environment.yml) file in this repository.

## Project Motivation
Using data of a well-know social cataloging web application (Goodreads) on the best books ever according to users' votings, I was interested in the following questions:

### Questions of Interest
1. Are books from certain time periods generally more popular?
2. What genres are most popular (over time)?
3. Are readers' ratings on books reflected in winning an award?
4. How well can we predict whether a book will be award winning or not?

## File Descriptions
The jupyter notebook [best-books-classification.ipynb](https://github.com/MareikeHeller/goodreads-best-books/blob/main/best-books-classification.ipynb) contains the project code, visualizations and results. 

The input data is provided in a separate folder [input_data/goodreads_books_chunk_1(-5)](https://github.com/MareikeHeller/goodreads-best-books/tree/main/input_data) split into 5 .csv files.

## Results
The results to the questions of interest in this project are contained in the respective sections of the [jupyter notebook](https://github.com/MareikeHeller/goodreads-best-books/blob/main/best-books-classification.ipynb) and further described in this [medium blog post](https://mareikeheller.medium.com/this-is-how-book-awards-and-book-ratings-are-not-the-same-a720be77404e).

However, it is worthy of note that the underlying dataset already contains the best rated books. Thus, this project looks at a very selective sample with reduced variation. 

## Licensing, Authors, Acknowledgements
The data used in this project is publicly available on [kaggle.com](https://www.kaggle.com/austinreese/goodreads-books) (License: CC0: Public Domain). The data on kaggle was originally scraped from [this Goodreads list](https://www.goodreads.com/list/show/1.Best_Books_Ever). I would like to acknowledge the Stack Overflow community that pushed my learning process. 
