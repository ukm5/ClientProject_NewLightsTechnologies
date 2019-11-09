import GetOldTweets3 as got
import codecs


def get_tweets(date_start, date_end, city, base_name):

    tweet_criteria = got.manager.TweetCriteria()\
        .setSince(date_start)\
        .setUntil(date_end)\
        .setNear(city)\
        .setWithin("150mi")

    file_name = ''.join(['../data/', base_name, '.csv'])
    output_file = codecs.open(file_name, "w+", "utf-8")
    output_file.write(
        'username;;date;;retweets;;favorites;;text;;geo;;mentions;;hashtags;;id;;permalink'
    )
    print(f'Retrieving {base_name} tweets...\n')

    def receive_buffer(tweets):
        for t in tweets:
            output_file.write(('\n%s;;%s;;%d;;%d;;"%s";;%s;;%s;;%s;;"%s";;%s' % (
            t.username, t.date.strftime("%Y-%m-%d %H:%M"), t.retweets, t.favorites,
            t.text, t.geo, t.mentions, t.hashtags, t.id, t.permalink)))
        output_file.flush()
        print('%d more saved on file...\n' % len(tweets))

    got.manager.TweetManager.getTweets(tweet_criteria, receive_buffer)
    output_file.close()


disaster_list = [
    ['2017-09-03', '2017-09-09', 'Cudjoe Key,Florida', 'hurricane_irma_pre'],
    ['2017-09-10', '2017-09-17', 'Cudjoe Key,Florida', 'hurricane_irma_post'],
    ['2017-08-18', '2017-08-24', 'Houston,TX', 'hurricane_harvey_pre'],
    ['2017-08-25', '2017-09-01', 'Houston,TX', 'hurricane_harvey_post'],
    ['2017-09-13', '2017-09-19', 'Puerto Rico', 'hurricane_maria_pre'],
    ['2017-09-20', '2017-09-27', 'Puerto Rico', 'hurricane_maria_post'],
    ['2018-11-01', '2018-11-07', 'Chico,California', 'wildfire_campfire_pre'],
    ['2018-11-08', '2018-11-15', 'Chico,California', 'wildfire_campfire_post'],
    ['2018-11-01', '2018-11-07', 'Thousand Oaks,California', 'wildfire_woolseyfire_pre'],
    ['2018-11-08', '2018-11-15', 'Thousand Oaks,California', 'wildfire_woolseyfire_post'],
    ['2018-07-16', '2018-07-22', 'Redding,California', 'wildfire_carrfire_pre'],
    ['2018-07-23', '2018-07-30', 'Redding,California', 'wildfire_carrfire_post'],
    ['2011-10-29', '2011-11-05', 'Prague,Oklahoma', 'prague_2011_earthquake_pre'],
    ['2011-11-06', '2011-11-13', 'Prague,Oklahoma', 'prague_2011_earthquake_post'],
    ['2014-08-17', '2014-08-23', '38.22,-122.31', 'north_bay_2014_earthquake_pre'],
    ['2014-08-24', '2014-08-30', '38.22,-122.31', 'north_bay_2014_earthquake_post'],
]

for disaster in disaster_list:
    get_tweets(disaster[0], disaster[1], disaster[2], disaster[3])