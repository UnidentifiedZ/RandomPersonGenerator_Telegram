# RandomPersonGenerator_Telegram
Script for generating virtual personalities in Telegram.

At the specified timeout, photos of non-existent people are set as an avatar (https://thispersondoesnotexist.com/), the name and surname are changed to random. Since there is no API or gender determination on the above site, unisex names are used.

### Requirements

* Python 3.*
* Pyrogram
* Requests

### How to use
1. Install Requirements

```pip install -r requirements```

2. Get your own Telegram API key from https://my.telegram.org/apps

3. Open config.py and paste the received data. Optionally, change the timeout (default, 3 minutes)

Run main.py.
