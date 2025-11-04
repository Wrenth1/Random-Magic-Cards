You'll first need to download **https://data.scryfall.io/default-cards/default-cards-20251103222953.json** and save it as "cards.json"

After that, run the cardDownload deduper.py, which removes duplicates (otherwise you WILL see a lot of basic lands) as well as trying to parse out UB cards, because I don't like them. You are welcome to alter that code if you want them included.
Then, run the fromFile.py script, and there's your random set of 50 cards.
