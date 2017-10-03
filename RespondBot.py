import os
import praw
import time


reddit = praw.Reddit("bot1")
history_text_name = "replied_to.txt"


# Checks if history file is already made, if not it makes a new one.
# Reads file and compares each line to the current post's id
# Returns True if post's id is in file, and False if not
def is_already_posted(post):
    if not os.path.isfile(history_text_name):
        f = open(history_text_name, "x")
        f.close()
    else:
        with open(history_text_name, "r") as f:
            list_posted = f.read()
            list_posted = list_posted.split("\n")
            list_posted = list(filter(None, list_posted))
        print(post.id)
        print(list_posted)
        print("\n")
        if post.id in list_posted:
            return True
    return False


# Checks if string is within a post's title
# True if it is in file, False if not
def is_word_in_title(post, string):
    if string.lower() in post.title.lower():
        return True
    return False


# Checks a certain quantity (quan) of posts' titles within a certain subreddit (sub) for a keyword (key), and
# then replies a comment (comment) if the keyword is found.
def post_comment(sub, key, comment, quan):
    subreddit = reddit.subreddit(sub)
    for post in subreddit.new(limit=int(quan)):
        if not(is_already_posted(post)) and is_word_in_title(post, key):
            post.reply(comment)
            print("Bot replied to: " + post.id)
            f = open(history_text_name, "a")
            f.write(post.id + "\n")
            f.close()


# Runs post_comment() but makes it active for a certain duration of time (time_to_monitor), and has it check every
# specified amount of time (frequency_for_checking)
def monitor_and_post(sub, key, comment, quan, time_to_monitor, frequency_for_checking):
    end_time = time.time() + float(time_to_monitor)
    print("\nMonitoring reddit.com/r/" + sub)
    print("for posts with key='" + key + "'")
    print("to post '" + comment + "'")
    print("for " + str(time_to_monitor) + " seconds...")
    while time.time() < end_time:
        post_comment(sub, key, comment, quan)
        time.sleep(frequency_for_checking)
    print("\nDone monitoring")
    return 0


cur_sub = input("\nWhat subreddit to comment in:\n>   ")
cur_key = input("\nWhat filter to use when searching for posts to reply to (keyword):\n>   ")
cur_comment = input("\nWhat comment to reply to posts with:\n>   ")
cur_quan = input("\nWhat quantity of new posts to search through\n>   ")
time_dur = input("\nWhat time duration to monitor (seconds)\n>   ")
time_freq = input("\nWhat time to wait in between checking posts\nNOTE: Reddit likes bots that wait 30 seconds\n>   ")
monitor_and_post(cur_sub, cur_key, cur_comment, cur_quan, time_dur, time_freq)
