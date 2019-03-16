## Tweepy

This programme uses Tweepy to access the Twitter API. Tweepy documentation and API reference pages can be found here: http://docs.tweepy.org/en/v3.5.0/api.html#api-reference

## Credentials & Authentication

In order to authenticate, you will need to get your credentials from developer.twitter.com (under the 'Keys and tokens' tab once you have selected your app).

1. Input each one of your four keys and tokens in the `credentials_example.txt` file after the `=` symbol (with no quotation marks).

2. Rename `credentials_example.txt` to `credentials.txt`

3. Don't forget to create a `.gitignore` file in your repository and add `credentials.txt` to avoid pushing your keys and tokens to GitHub.

## Run the application

Once you you've saved your credentials (see above) you can run this application by navigating to this directory in your command line and run: `python tweet.py`

This will run your application locally, at port 5000: simply open up your browser and type `http://localhost:5000/`

You can now access the latest Tweets on your timeline and Tweet something.

In order to quit the application, go back to your command line and type `CTRL+C` (Mac).