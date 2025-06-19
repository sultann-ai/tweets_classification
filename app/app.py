from flask import Flask, jsonify

app = Flask(__name__)

# Sample tweet data for each category
sample_tweets_categorization_data = {
    "sportsTweets": [
        {"tweetText": "The tennis match today was intense! #USOpen", "username": "@john_sports"},
        {"tweetText": "Football season is back! Who's ready? #NFL", "username": "@sportsfan23"},
        {"tweetText": "Just finished a marathon in under 4 hours! #running", "username": "@fast_runner"},
        {"tweetText": "Great performance by the basketball team tonight!", "username": "@hoopking"},
        {"tweetText": "The World Cup qualifiers are heating up! #soccer", "username": "@soccerfan_22"},
        {"tweetText": "Breaking: Serena Williams wins the match!", "username": "@tennis_fan88"},
        {"tweetText": "Congrats to the Chicago Cubs on their win today!", "username": "@baseball_lover"},
        {"tweetText": "The new NBA draft picks look promising!", "username": "@nbafan22"},
        {"tweetText": "Tennis star Federer announces retirement. #goodbye", "username": "@sportsbuzz"},
        {"tweetText": "Watching the Olympics and seeing incredible athletes! #Tokyo2020", "username": "@olympicfan"},
        {"tweetText": "Who is your favorite basketball team? Mine is Lakers! #NBA", "username": "@lakersfan123"},
        {"tweetText": "Marathon training starts tomorrow! Let’s do this!", "username": "@marathonprep"},
        {"tweetText": "Big game tonight! Go team!", "username": "@sports_fan123"},
        {"tweetText": "Cricket World Cup starts soon! Who will take the trophy?", "username": "@cricketguru"},
        {"tweetText": "Huge win for the Golden State Warriors tonight!", "username": "@warriorfan"},
        {"tweetText": "Excited for the next Formula 1 race!", "username": "@f1fanatic"},
        {"tweetText": "Amazing comeback by the football team in the last quarter!", "username": "@gamechanger22"},
        {"tweetText": "Astonishing results in the Tour de France!", "username": "@cycling_fan"},
        {"tweetText": "New tennis records set at Wimbledon this year!", "username": "@tennisupdate"},
        {"tweetText": "Who else is excited about the next sports season? #sportsfanatic", "username": "@fanatic_sports"}
    ],
    "newsTweets": [
        {"tweetText": "Breaking news: Global stock market crashes today.", "username": "@newswire"},
        {"tweetText": "The president announced a new economic policy today.", "username": "@world_news"},
        {"tweetText": "Protests erupt over new government regulations.", "username": "@dailyupdates"},
        {"tweetText": "The latest climate change report is alarming.", "username": "@climatenews"},
        {"tweetText": "NASA launches a new mission to Mars.", "username": "@space_explorer"},
        {"tweetText": "Scientists discover a new species in the Amazon rainforest.", "username": "@eco_news"},
        {"tweetText": "Breaking: New trade agreement signed between the US and China.", "username": "@globalnews"},
        {"tweetText": "Massive wildfire continues to rage in California.", "username": "@weathernews"},
        {"tweetText": "The UN holds an emergency meeting on global health issues.", "username": "@internationalnews"},
        {"tweetText": "Tensions rise in the Middle East as diplomatic talks stall.", "username": "@foreign_affairs"},
        {"tweetText": "New legislation to combat online hate speech is being debated.", "username": "@politics_today"},
        {"tweetText": "Economy faces challenges as inflation hits new highs.", "username": "@economy_watch"},
        {"tweetText": "The latest report on global poverty reveals concerning statistics.", "username": "@global_issues"},
        {"tweetText": "China announces plans to expand its space station program.", "username": "@spacenews"},
        {"tweetText": "Massive earthquake strikes in the Pacific Ocean.", "username": "@earthquake_alert"},
        {"tweetText": "Stock market sees an unexpected recovery today.", "username": "@business_news"},
        {"tweetText": "A breakthrough in cancer research announced by a leading university.", "username": "@healthreport"},
        {"tweetText": "The government imposes new travel restrictions amid rising COVID cases.", "username": "@healthupdates"},
        {"tweetText": "Tensions between countries escalate due to ongoing border dispute.", "username": "@worldaffairs"},
        {"tweetText": "Authorities investigate a cyber attack on major corporations.", "username": "@techreport"}
    ],
    "technologyTweets": [
        {"tweetText": "Excited about the new iPhone release today! #Apple", "username": "@techie_girl"},
        {"tweetText": "AI is the future, and we’re just scratching the surface! #machinelearning", "username": "@ai_enthusiast"},
        {"tweetText": "Google introduces new features in Android 12. #technews", "username": "@gadget_fan"},
        {"tweetText": "Just built a new gaming PC, and it's a beast! #gaming", "username": "@gamerlife"},
        {"tweetText": "The latest VR technology is mind-blowing! #VirtualReality", "username": "@tech_explorer"},
        {"tweetText": "Elon Musk’s SpaceX successfully launches another satellite.", "username": "@spacetech"},
        {"tweetText": "5G is finally here, and it’s faster than ever!", "username": "@technewsdaily"},
        {"tweetText": "Can’t wait to see what’s next in autonomous vehicle tech.", "username": "@selfdriving"},
        {"tweetText": "The rise of blockchain is something to watch closely.", "username": "@cryptocurrencyfan"},
        {"tweetText": "Artificial intelligence will disrupt every industry.", "username": "@futuretech"},
        {"tweetText": "Big Data is the new oil in the tech industry.", "username": "@datatrends"},
        {"tweetText": "Cloud computing continues to transform businesses globally.", "username": "@cloudtech"},
        {"tweetText": "New software update for Windows 11 is packed with new features.", "username": "@windowsfan"},
        {"tweetText": "Tech companies are racing to develop quantum computing.", "username": "@technews101"},
        {"tweetText": "Tesla’s latest update adds new autopilot features.", "username": "@tesla_enthusiast"},
        {"tweetText": "The impact of 5G on IoT will be revolutionary.", "username": "@techgurus"},
        {"tweetText": "Blockchain is set to disrupt the financial sector. #cryptos", "username": "@blockchainfan"},
        {"tweetText": "Today’s smartphones are as powerful as some desktop computers!", "username": "@techlover"},
        {"tweetText": "Augmented Reality is taking retail shopping to a new level!", "username": "@ar_enthusiast"},
        {"tweetText": "Amazon Web Services continues to dominate the cloud space.", "username": "@aws_lover"}
    ],
    "healthTweets": [
        {"tweetText": "Exercise is the best way to maintain mental health.", "username": "@health_guru"},
        {"tweetText": "Eating a balanced diet is key to overall well-being!", "username": "@nutrition_expert"},
        {"tweetText": "Mindfulness and meditation can reduce stress levels significantly.", "username": "@mentalhealthadvocate"},
        {"tweetText": "Stay hydrated! Drinking water is essential for your health.", "username": "@healthtips"},
        {"tweetText": "New study shows the benefits of plant-based diets.", "username": "@healthy_eating"},
        {"tweetText": "It’s important to take mental breaks during work hours.", "username": "@workplacewellness"},
        {"tweetText": "Vaccines save lives. Stay protected and get vaccinated.", "username": "@vaccineswork"},
        {"tweetText": "The benefits of a good night’s sleep cannot be overstated.", "username": "@sleepwell"},
        {"tweetText": "Physical activity is a game-changer for overall health.", "username": "@fitlife"},
        {"tweetText": "Preventive care is essential for a long, healthy life.", "username": "@healthyliving"},
        {"tweetText": "COVID-19 has shown us the importance of healthcare systems.", "username": "@globalhealth"},
        {"tweetText": "Mental health matters just as much as physical health.", "username": "@mentalwellbeing"},
        {"tweetText": "The new health app helps track your daily workouts and diet.", "username": "@healthtech"},
        {"tweetText": "The rise of telemedicine is changing healthcare access.", "username": "@digitalhealth"},
        {"tweetText": "A healthy gut is the key to better immunity!", "username": "@gut_health"},
        {"tweetText": "Stop smoking today! It's never too late to improve your health.", "username": "@quit_smoking"},
        {"tweetText": "Get moving! Even 10 minutes of exercise daily is beneficial.", "username": "@fitnessmotivation"},
        {"tweetText": "Don’t skip your annual health check-ups.", "username": "@preventivecare"},
        {"tweetText": "Self-care is not selfish; it's necessary for good health.", "username": "@selfcareadvocate"},
        {"tweetText": "Don’t forget your mental health – it’s as important as physical health.", "username": "@mindfulness_matters"}
    ],
    "fashionTweets": [
        {"tweetText": "Loving the new summer collection! #fashionista", "username": "@stylequeen"},
        {"tweetText": "Bold colors and unique designs are in this season!", "username": "@fashionlover"},
        {"tweetText": "Just got my hands on the latest Gucci sneakers. #style", "username": "@sneakerhead"},
        {"tweetText": "The 90s fashion is making a huge comeback! #throwback", "username": "@retro_fashion"},
        {"tweetText": "Minimalism is trending in fashion this year. #lessismore", "username": "@simple_style"},
        {"tweetText": "Street style is on point this season! #urbanfashion", "username": "@streetwearfan"},
        {"tweetText": "Blazers are back in fashion for the fall season.", "username": "@fashionguide"},
        {"tweetText": "The new handbag collection is stunning!", "username": "@accessorieslover"},
        {"tweetText": "This year’s fashion trends are all about comfort.", "username": "@casualstyle"},
        {"tweetText": "Bags are getting bigger and bolder. #fashiontrends", "username": "@baglover"},
        {"tweetText": "Athleisure is not just for the gym anymore! #fashionforward", "username": "@athleisurefan"},
        {"tweetText": "Sustainable fashion is the way to go. #ecofriendly", "username": "@sustainablefashion"},
        {"tweetText": "Looking forward to the fashion week in Paris!", "username": "@fashionweekfan"},
        {"tweetText": "The power of accessories to complete an outfit is real.", "username": "@accessoryaddict"},
        {"tweetText": "I can’t stop wearing oversized jackets! #fashionstyle", "username": "@oversizedfashion"},
        {"tweetText": "Floral patterns are everywhere this season.", "username": "@floralfashion"},
        {"tweetText": "The capsule wardrobe trend is saving my closet space!", "username": "@minimalistfashion"},
        {"tweetText": "Hats are having a big moment in fashion right now.", "username": "@hatlover"},
        {"tweetText": "Trying out a new color palette for my wardrobe this season!", "username": "@colorfulfashion"},
        {"tweetText": "Denim jackets are back in style this fall!", "username": "@denimfan"}
    ]
}
sample_tweets_analysis_data = {
  "analysis": {
    "sports": "Tweets in the sports category focus on various popular sports like tennis, football, basketball, and more. Key themes include major sporting events such as the US Open, World Cup qualifiers, and the Olympics. The tweets often express excitement and appreciation for athletes, teams, and upcoming events, showcasing a high level of enthusiasm for both professional and amateur sports.",
    "news": "The news category includes tweets related to global current events, such as stock market fluctuations, political developments, natural disasters, and global health issues. Key topics are economic changes, environmental concerns, and international relations. The tweets often highlight breaking news, providing followers with immediate updates on critical situations.",
    "technology": "Tweets in the technology category focus on the latest advancements in tech, such as new smartphone releases, AI developments, VR, and blockchain technology. Many tweets mention new product releases or updates from major tech companies like Apple, Google, and Tesla. The tweets reflect excitement about innovations that will shape the future of technology.",
    "health": "Health-related tweets cover a range of wellness topics, including exercise, diet, mental health, and healthcare systems. The tweets often promote healthy living habits, emphasize the importance of mental well-being, and discuss global health trends such as COVID-19 and vaccination efforts. The tweets provide practical advice and support for maintaining a healthy lifestyle.",
    "fashion": "Tweets about fashion highlight seasonal trends, new collections, and fashion movements. Themes include minimalism, street style, sustainability, and accessories. Users share excitement about their purchases and upcoming fashion events like Paris Fashion Week. The tweets reflect an appreciation for stylish, trendy, and eco-conscious clothing choices, offering a glimpse into current fashion interests."
  }
}

@app.route("/hello", methods=["GET"])
def hello():
    return "Hello, World!"

@app.route('/api/tweets/categories', methods=['GET'])
def get_all_categories():
    return jsonify(sample_tweets_categorization_data)
    

@app.route('/api/tweets/<category>', methods=['GET'])
def get_tweets(category):
    if (category+"Tweets") in sample_tweets_categorization_data:
        return jsonify(sample_tweets_categorization_data[category+"Tweets"])
    else:
        return jsonify({"error": "Category not found!"}), 404

@app.route('/api/analysis/<category>', methods=['GET'])
def get_analysis(category):
    if category in sample_tweets_analysis_data["analysis"]:
        return jsonify({category: sample_tweets_analysis_data["analysis"][category]})
    else:
        return jsonify({"error": "Category not found!"}), 404

if __name__ == '__main__':
    app.run(port=3000)



