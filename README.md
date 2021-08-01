# JW Book Extractor

## General description

This repository provides a standardized crawler to extract monolingual and bilingual data from the [JW](https://www.jw.org/) website and particulary published books. The main interest is the large number of languages covered by the website making a major provider of textual data for Low Ressource Languages (LRL).

LRL have been lagging behind the advancement of Natural Language Processing (NLP).
Indeed, LRL are under-represented in the Global DataSpheere and are sometimes characterized by a decreasing or very low number of native speakers.
As a result, NLP tasks such as supervised Machine Translation are currently unable to deal with a large number of LRL.
There are several initiatives accross the world to build larger datasets for LRL. This repository is a contribution to that work.

[JW](https://www.jw.org/) have been a major source for building LRL datasets. The so-called [JW300](https://opus.nlpl.eu/JW300.php) corpus covering more than 300 languages is an example.
However, the large number of languages covered by the JW300 limits its update frequency to account for novel textual data from the JW website.

I built a standadized scraper to get monolingual and/or bilingual data from the JW website. Particularly, the crawler is built to extract sentences from books published on the website. You just have to provide links of source and/or target languages books/magazines in the *book_urls.csv* files. Book urls can be found [here](https://www.jw.org/en/library/books/) for English. You just need to change the page language to get the equivalent page for another language: [here](https://www.jw.org/fon/nus%C9%9Bxwet%C9%9Bn/wema-l%C9%9B/) is the equivalent version for Fon. To get the link of a given book, you just have to right click on it and click on *copy link address*. 

Future versions would include a function to automatically extract book links from a given page. 

Scraped data are saved by default in the folder *data* in two different files (one for source language and the second for target language). You can customize the saving directory and file names in *parameters.json*.

## Launching the crawler

### Getting Monolingual data

You have to provide, in *book_urls.csv* file, book links in the *source_url* column and run the following code: 

python getmonolingual.py

### Getting bilingual data

You have to provide, in *book_urls.csv* file,  book links in the *source_url* column and their equivalent in the target language and run the following code: 

python getmonolingual.py

Sentences from both languages are automatically aligned. If source-target shapes are not matched for a given book, no data is saved as thy wouldn't be aligned. 

 
