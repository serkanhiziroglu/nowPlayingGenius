## NowPlayingGenius

NowPlayingGenius is a simple script that can automatically display lyrics of the currently playing song on Spotify. GeniusAPI has access to lesser-known/indie song lyrics, making it a better alternative in some cases, compared to Spotify's built-in lyrics service.

## Running & Authentication

You can simply run the script to make it work. However, you need to edit some variables specified for you to get access to Spotify and Genius API. 
Four variables required are in authentication.py file.
After acquiring an access token, Spotify ends it after 1 hour. To solve this issue, I have used refresh token provided by Spotify and script requires a new refresh token everytime. You can skip calling refresh() function if you don't want to do this.
Keep in mind that while acquiring access tokens, you need to give access to the script. 

## Dependencies & Libraries

NowPlayingGenius gets help from LyricsGenius, which is a Python client for the Genius.com API. You can visit their website from here: (https://lyricsgenius.readthedocs.io/en/master/#).

## Future support

1. Some song lyrics can't be found even though they exist in the API. I will solve this problem.
2. UI support