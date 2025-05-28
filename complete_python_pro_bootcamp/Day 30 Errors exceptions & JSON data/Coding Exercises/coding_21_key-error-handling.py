# KeyError Handling
# We've got some buggy code, try running the code. The code will crash and give you a KeyError.

# This is because some of the posts in the facebook_posts don't have any "Likes".

# Objective
# Use what you've learnt about exception handling to prevent the program from crashing.

# ✅ SOLUTION
facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]


def count_likes(posts):
    total_likes = 0
    for post in posts:
        try:
            # This line can raise KeyError
            total_likes = total_likes + post['Likes']
            # Catch the specific exception when 'Likes' key doesn't exist
        except KeyError:
            # Skip posts without 'Likes' key (treat as 0 likes)
            pass
    return total_likes


count_likes(facebook_posts)