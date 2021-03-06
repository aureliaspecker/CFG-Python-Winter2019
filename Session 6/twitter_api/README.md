## Tweepy

This programme uses Tweepy to access the Twitter API. Tweepy documentation and API reference pages can be found here: http://docs.tweepy.org/en/v3.5.0/api.html#api-reference

## Credentials & Authentication

In order to authenticate, you will need to get your credentials from https://developer.twitter.com/en/apps You can access these under the 'Keys and tokens' tab, once you have selected what app to work with. If you don't yet have any apps, you can create one using the 'Create an app' button at the top-right hand corner of the page.

1. Input each one of your four keys and tokens in the `credentials_example.txt` file after the `=` symbol (with no quotation marks).

2. Rename `credentials_example.txt` to `credentials.txt`

3. Don't forget to create a `.gitignore` file in your repository and add `credentials.txt` to avoid pushing your keys and tokens to GitHub.

## Run the application

Once you've saved your credentials (see steps outlined above), you can run this application by navigating to the `twitter_api` directory in your command line. 

From there, run: `python tweet.py`

This will run your application locally, at port 5000: simply open up your browser and type `http://localhost:5000/`

You can now access the latest Tweets on your timeline and Tweet something.

In order to quit the application, go back to your command line and type `CTRL+C` (Mac).
