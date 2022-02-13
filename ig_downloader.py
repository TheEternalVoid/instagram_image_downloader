from instaloader import Instaloader, Profile
import yaml
from pathlib import Path

#getting username + password from yaml file stored seperately
def get_settings():
    full_file_path = Path(__file__).parent.joinpath('settings.yaml')
    with open(full_file_path) as settings:
        settings_data = yaml.load(settings, Loader=yaml.Loader)
    username = (settings_data['credentials']['username'])
    password = (settings_data['credentials']['password'])
    return [username, password]

#call the function to get user + pass
user_info = get_settings()

#parse username
user_username = user_info[0]

#parse password
user_pw_not_format = user_info[1]

#yaml is adding an additional \ so we slice the string for pass
user_pw = user_pw_not_format[1:]

#start Instaloader
ig = Instaloader()

#get user input for instaname to scrape
dp = input("Enter Insta username : ")

#login to ig (required) with given username and password
ig.login(user_username, user_pw)


profile = Profile.from_username(ig.context, dp)

#sort posts and store as list
posts_sorted_by_likes = sorted(profile.get_posts(), key = lambda post: post.likes, reverse=True)

#download each post
for post in posts_sorted_by_likes:
    ig.download_post(post, dp)

