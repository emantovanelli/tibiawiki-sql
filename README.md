**This project is in early development**

# tibiawiki-sql
Script that generates a sqlite database for the MMO Tibia.

Inspired in [Mytherin's Tibiaylzer](https://github.com/Mytherin/Tibialyzer) TibiaWiki parsing script.

This script fetches data from TibiaWiki via its API, compared to relying on [database dumps](http://tibia.wikia.com/wiki/Special:Statistics)
that are not updated as frequently. By using the API, the data obtained is always fresh.

This script is not intended to be running constantly, it is meant to be run once, generate a sqlite database and use it 
externally.

## Requirements

* Python 3.6 or higher
    * **requests** module

## Database contents
* Creatures
* Items
* Creature drop statistics
    
Planned:
* NPCs
* NPC offers
* Spells and runes
* Houses
* Achievements
* Quests
* *and more...* 
    
## Database schema
*Coming soon*

