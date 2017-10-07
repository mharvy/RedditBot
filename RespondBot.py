# This script peruses subreddits and posts a comments to all posts with a given string in its title, then searches again
# Fastest way to post replies to lots of posts at the same time

# File that clears every time
# For loop that runs through amount of reddit posts, if it finds one with key=comment, then it posts and returns to zero


import praw
import time


reddit = praw.Reddit("bot1")
history_text_name = "replied_to2.txt"


def big_post_reply(sub, key, comment, lim):

    subreddit = reddit.subreddit(sub)
    for post in subreddit.new(limit=lim):

        if key in post.title:

            post.reply(comment)
            print("Replied to " + post.id + "\n")
            time.sleep(30)  # Needs to wait 30 seconds in order to be a 'legal' bot

    return 0


def main():

    sub = input("Subreddit to look through:\n>   ")
    key = input("Keyword to look for in post titles:\n>   ")
    comment = input("Comment to reply with:\n>   ")
    lim = input("Limit of posts to search through:\n>   ")
    big_post_reply(sub, key, comment, int(lim))


if __name__ == "__main__":

    main()
