# trendy
server that lists trending topics, given a set of RSS feed urls

If you want to use Google Language API to determine topics, follow Step 1 outlined [here](https://cloud.google.com/natural-language/docs/quickstart-client-libraries?authuser=1#before-you-begin)

Save the credentials in your `/app` directory as `trendy-creds.json`

Once this is done, you can set `USE_LANGUAGE_API` to `true` in `docker-compose.yml`

Otherwise, the topics are determined using regex

assuming you have docker, docker-compose 3.6,
to spin up the server you should be able to just run `Make serve` _(works on my machine!)_

If I had more time, I would:
- write tests!!
- split parsing topics out of `Feed` class into its own class
- add more error handling, useful logging

If I had a LOT more time, I might:
- focus on how best to display and determine the trending topics (neither regex nor the language API are ideal)
- add a cache in front of feed retrieval and topic parsing (trending topics change a few times an hour at most)
- consider adding a background worker process that runs every few minutes, gets feeds, determines topics,
and updates a store shared with the API server
