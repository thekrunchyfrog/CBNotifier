# CBNotifier
Get a notification when a certain model is on cam.

This is slowly turning in to a REST API for chaturbate.
It's using flask to run a service and mechanize and beautifulsoup4 behind the scenes.


POST: /modes/followed/online

Request Example:

'''json
{"username": "user", "password": "password"}
'''

Response Example: 

'''json
{
  "online": [
    {
      "name": "ashleylove13",
      "thumbnail": "https://cdn-s.highwebmedia.com/uHK3McUtGCG3SMFcd4ZJsRv8/roomimage/ashleylove13.jpg",
      "timeOnline": "182 mins",
      "url": "https://chaturbate.com/ashleylove13"
    },
    {
      "name": "femmexfatale",
      "thumbnail": "https://cdn-s.highwebmedia.com/uHK3McUtGCG3SMFcd4ZJsRv8/roomimage/femmexfatale.jpg",
      "timeOnline": "177 mins",
      "url": "https://chaturbate.com/femmexfatale"
    }
  ]
}
'''

