Script Name: wikiWebCrawler.py
Initial Date: 09/02/2017

This is a Python based program that crawles through a start Wiki page, picking up the first URL seen in the article.
This is done in a loop until one of the below occurs:

1) The program has picked 25 URLs already.
2) The program has reached a target URL (specified in the code)
3) The program detects a loop, i.e, it comes across a URL that was already picked before.

The Start URL and the Target URL can be specified within the code on the below variables:
start_url  -- for the start URL
target_url -- for the target URL


