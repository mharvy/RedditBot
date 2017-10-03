import praw

# New bot instance
reddit = praw.Reddit('bot1')


# Grabs quan amount of posts from sub subreddit, prints their titles, scores, and up/downs
def show_new_posts(sub, quan):
    subreddit = reddit.subreddit(sub)
    print("\n\n")
    for submission in subreddit.new(limit=int(quan)):
        print("Title: " + submission.title)
        print("Score: " + str(submission.score))
        print("Upvotes/Downvotes: " + str(submission.ups) + "/" + str(submission.downs) + "\n\n")


a = input("Enter subreddit:\n>   ")
b = input("Enter quantity of posts:\n>   ")
show_new_posts(a, b)