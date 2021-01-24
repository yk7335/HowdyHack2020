# HowdyHack2020

## Inspiration
- We have always found the act of making and curating your playlists tedious and inefficient. It would be great if a single desktop app could curate and add to several playlists overtime dedicated to a particular mood

## What it does
 - for this project, our goal was to prove this idea and narrow our scope to processing user data in the form of entries and develop a method that would gauge the overall mood/tone of the user journal entry. We did this using the Microsoft Azure Analytical API. We then take in an artist suggestion and use the lyrics genius API to look for songs that fit the same overall tone and mood as the entry and recommend that song.

## How We built it
- we developed this project in python 3. using mostly Microsoft's Azure anylytical API and Genius Lyrics API to predict the user's mood, take artist suggestion, and then recommend a song to them that best fits their mood. Our gui was made from the Tkinter library and we imported numpy arrays to hold artists and song lyrics. 

## Challenges We ran into
- What we soon realized as a team is the act of trying to process natural language is really hard. While we did have some issues working with and testing out different API we found that processing the user data to be the biggest challenge. Next was the issue of developing some consistent way of gauging the tone/mood for a given entry. we needed to develop a systematic way of accessing tone in a way that wasn't arbitrary. 

## What We learned & What's next
- Throughout this project, we gained a deeper understanding of APIs and the value some open-source ones can bring to your project. We also noted that while some ideas may be easily explained, the act of processing user data is a very challenging task. On that note, we still plan on completing this project with a different strategy in both distribution and problem approach. Throughout the day we realized that this should be a mobile app, not a desktop one, and overall a different framework is needed to really have the UIX we where striving to achieve.
