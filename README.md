# Tamil songs_search_engine
![GitHub repo size](https://img.shields.io/github/repo-size/Archulan/Tamil_songs_search_engine?color=red&style=plastic)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/Archulan/Tamil_songs_search_engine?style=plastic)
![GitHub language count](https://img.shields.io/github/languages/count/Archulan/Tamil_songs_search_engine?color=brightgreen&style=plastic)
![GitHub top language](https://img.shields.io/github/languages/top/Archulan/Tamil_songs_search_engine?color=blueviolet&style=plastic)

This Repository includes the implementaion for a search query.
The search engine could be used after configuring elastcisearch.
After configruing the elasticsearch, the sample search engine is used to try the query searches.

Description
---
There are about three thousand song data collected from 'https://www.tamilpaa.com'. The data is available in Song data/Web scraped raw data.csv. These songs have nine metadata such as movie, song name, music, song lyrics, song singers, year, actors, rating and song_full_lyrics. There is a search engine developed by using Elastic Search and Kibana.

Demo
---
* Install ElasticSearch 
* Add 'Analyzers' folder in config of Elasticsearch
* Run ElasticSearch
* Run 'Index adder.py' to add index
* Add the data by 200 record due to the max cap
* Go to http://localhost/5601
* Go to Web tools
* Search for Lyrics

Sample queries
---

* Search for all the songs from a movie(all songs in an album)
```
GET /songs_db/_search
{
   "query": {
       "multi_match": {
           "fields":["movie"],
           "query" : "தம்பி",
           "fuzziness": "AUTO"
       }
   }
}
```

* Search for songs released within a time period
```
GET/songs_db/songs/search?filter_path=hits.hits._source.song name,hits.hits._source.திரைப்படம்,hits.hits._source.year
{
   "size" : 10,
    "sort" : [
       { "மதிப்பீடு" : {"order" : "desc"}}
   ],
   "query": {
       "range" : {
           "வருடம்" : {
               "gte" : "2005",
               "lte" :  "2020"
           }
       }
   }
}
```

* Search for songs related to an artist
```
GET /songs_db/songs/_search
{
    "query": {
        "multi_match" : {
            "query" : "ஹஷ்ரி ஜெராயஜ்",
            "fuzziness": "AUTO"
        }
    }
}
```

* Search by keywords
```
GET /songs_db/_search
{
  "query": {
    "multi_match" : {
      "query":    "கனவு",
      "fuzziness": "AUTO"
    }
  }
}
```

* Search for songs by Yuvan Shankar Raja in 2010
```
GET /song_index/_search
{
  "query": {
    "bool": {
      "should": [
        {
          "bool": {
            "must": [
              { "match": { "music":"யுவன்சங்கர்ராஜா" } },
              { "match": { "year":"2010}}
            ]
          }
        }
      ]
    }
  }
}
```

* Search for songs by A.R Rahman or Ilaiyaraaja
```
GET /song_index/_search
{
  "query": {
    "bool": {
      "should": [
        {
          "bool": {
            "must": [
              { "match": { "music":"இளையராஜா" } }
            ]
          }
        },
        {
          "bool": {
            "must": [
              { "match": { "music":"ஏ.ஆர்.ரஹ்மான்" } }
            ]
          }
        }
      ]
    }
  }
}
```

* Delete a record from song data
```
POST /song_index/_delete_by_query
{
 "query": {
   "bool": {
      "must": [
        { "match": { "movie":"தெனாலி" } },
        { "match": { "song":"ஆலங்கட்டி மழ" }}
      ]
    }
  }
}
```

* Update a record in song data
```
{
  "script": {
    "source": "ctx._source.application = 'insight'",
    "lang": "painless"
  },
  "query": {
    "bool": {
      "must": [
        {
          "term": {
            "indexType.keyword": "ARCHITECTURE_MATURITY_INDEX"
          }
        },
        {
          "term": {
            "timestamp": "2019-10-28"
          }
        }
      ]
    }
  }
}
```
