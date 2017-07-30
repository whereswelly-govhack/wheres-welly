<p align="center">
  <a href=https://drive.google.com/drive/u/2/folders/0B3SjqsAKahBWd2hpeVdxYUNIUTQ>
    <img src="https://raw.githubusercontent.com/whereswelly-govhack/wheres-welly/master/imgs/wswLogo_s.jpg" width=120 height=120>
  </a>
  <h2 align="center">Where's Welly</h2>
  <p align="center">
    Awesome travel time visualisation of Wellington, courtesy of Govhack 2017.
    <br>
    <a href="https://whereswelly-govhack.github.io/"><strong>Visit our Website &raquo;</strong></a>
    <br>
    <br>
    <a href="https://drive.google.com/drive/u/2/folders/0B3SjqsAKahBWd2hpeVdxYUNIUTQ">Check out our Google Drive</a>
    &middot;
    <a href="https://youtube.com">Watch Our Youtube Video</a>
    &middot;
    <a href="https://govhack.org.nz/wellington/">Vote for us on Govhack 2017</a>
  </p>
</p>

<br>


## Table of contents

- [Introduction](#introduction)
- [Demonstration](#demonstration)
  - [Looking for Home](#looking-for-home)
  - [Looking for Work](#looking-for-work)
- [For Developers](#for-developers)
  - [Datasets](#datasets)
- [Future Goals](#future-goals)
- [Creators](#creators)

## Introduction
Wellington is a complicated city. Threaded with narrow, winding roads and tunnels looping through hilly terrain, it can be difficult for new-comers (and old timers!) to wrap their heads around the cities, suburbs and the connections inbetween.

Where's Wally is a tool to help current and prospective Wellingtonians plan where to live and explore in the windy city. If you are planning on moving in and want somewhere close to work, you can use Where's Wally to help you find where is best for you.

## Demonstration

At [Where's Welly](http://mapsnz.link/index.php?id=19), users can mark their work and home locations, and gain useful statistics about travel times by vehicle, by foot as well as recent rent statistics, courtesy of MBIE. Regions are mapped to indicate 5, 10 and 15 minute travel time from the work location.

### Looking for Home
Users with a fixed work location who are looking for where to live can set their markers like this. Khandallah (marked "H" on the map) might look close on the map, but in terms of travel time you would be better of further away.

[Where's Welly](http://mapsnz.link/index.php?id=19) also calculates the following:
- Travel time by foot, bicycle or vehicle
- Basic accomodation, fuel and parking costs for getting to and from your work location

![imagetitle](./imgs/khandallah.png?raw=true "Optional Title")

It is also possible to plot regions based on walking distance. If you simply want to take a walk and see how far is too far, Where's Wally will help you do that too.

<p align="center">
  <img src="https://raw.githubusercontent.com/whereswelly-govhack/wheres-welly/master/imgs/hataitai_small.png">
</p>

### Looking for Work
For users with a fixed home or school location who are looking for work in Wellington can set their markers like this. This way, the tool will tell you which parts of Wellington are most accessible (and cheap!) from where you live.

![imagetitle](./imgs/petone.png?raw=true "Optional Title")

## For Developers

Where's Wally was developed in JavaScript using the [HERE API](https://developer.here.com/), and a considerable amount of open government data, provided by [Stats NZ](https://stats.govt.nz), [Ministry of Business, Innovation and Employment](http://www.mbie.govt.nz/) (MBIE).

The source code is provided here with a Something-or-other License. Our datasets are also provided for the benefit of developers as well. They have been collected from various open data sources, and are in /data in raw and edited form.

### Datasets
A more detailed breakdown of the datasets used is here:
- HERE API
  - Mapping System
- Stats NZ
  - New Zealand regional and area unit maps
- MBIE
  - Median rental costs by area unit

## Future Goals
Future development goals include:
- Better capturing public transport options 
- Adding more layers of services
- Building on the happiness and self-assessed health scores from the Human Health Survey 
- Adjusting the scale to match commuting preferences
- Integrating with existing rental and house sales websites so that their information is more useful. 


## Creators
**Mark Otto**

- <https://twitter.com/mdo>
- <https://github.com/mdo>

**Jacob Thornton**

- <https://twitter.com/fat>
- <https://github.com/fat>

Our tool also can help with:
Visitors to Wellington booking their accommodation [ask backpacker to use outside station
Renters new to town who don’t have a car
Retirees wanting to live where they don’t have to drive [
Planning exercise routes [someone dressed for jogging]
And in law enforcement [cops and robbers?]



