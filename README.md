# Clearcode
Tasks for Python internship

1. CSV Report Processing
   Script which transform input data into desirable format.
   
   Critical errors:
   - 'Impressions' column is not integer type (there could not exist for example: '9' or 9.9 impressions)
   - if there is more than 50% of missing data in any column whole the data is not usable
   
   
2. WebCrawler
   To use site_map function it is needed to:
    - remove urls.json file if it exist in WebCrawler directory,
    - set the name of mapping website (url adress) in WebCrawler/spiders/urls.py into 
      start_urls = ['name of your domain'] and domain = ['name of your domain'] 
    - in command prompt go to the WebCrawler directory,
    - in command prompt write and execute: scrapy crawl urls -o urls.json
    
   Then you can use site_map() :)
   If you want to map another site you have to do all steps from list above.
