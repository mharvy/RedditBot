import praw


reddit = praw.Reddit('bot1')
subreddit = reddit.subreddit("testingground4bots")


for submission in subreddit.new(limit=10):
    print("Title: " + submission.title)
    print("Score: " + str(submission.score))
    print("Upvotes/Downvotes: " + str(submission.ups) + "/" + str(submission.downs) + "\n\n")


