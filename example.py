#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import time

sys.path.append(os.path.join(sys.path[0], 'src'))

from check_status import check_status
from feed_scanner import feed_scanner
from follow_protocol import follow_protocol
from instabot import InstaBot
from unfollow_protocol import unfollow_protocol

bot = InstaBot(
    login="username",
               #instagram username
    password="password",
               #instagram password
    like_per_day=1000,
               #total amount of likes the bot will do per day
    comments_per_day=0,
               #amount of comments the bot will post per day
    tag_list=['follow4follow', 'f4f', 'cute'],
               #hashtasgs that the bot will usde to like,follow accounts
    tag_blacklist=['rain', 'thunderstorm'],
               # will not like the posts with these tags
    user_blacklist={},
    max_like_for_one_tag=50,
               #the amount of likes the bot will do per hashtag
    follow_per_day=300,
               #total amount of accounts the bot will follow per day
    follow_time=1 * 60,
               #the amout of time the bot will follow an account in seconds ex 60*1 is 1 min
    unfollow_per_day=300,
               #the amount of accounts the bot will unfollow per day
    unfollow_break_min=15,
    unfollow_break_max=30,
               #how long the bot will wait boefore doing rounds of unfollowing
    log_mod=0,
               #log 0 is for concel, log 1 is for file
    proxy='',
    # Use unwanted_username_list to block usernames containing a string
    ## Will do partial matches; i.e. 'mozart' will block 'legend_mozart'
    ### 'free_followers' will be blocked because it contains 'free'
    unwanted_username_list=[
        'second', 'stuff', 'art', 'project', 'love', 'life', 'food', 'blog',
        'free', 'keren', 'photo', 'graphy', 'indo', 'travel', 'art', 'shop',
        'store', 'sex', 'toko', 'jual', 'online', 'murah', 'jam', 'kaos',
        'case', 'baju', 'fashion', 'corp', 'tas', 'butik', 'grosir', 'karpet',
        'sosis', 'salon', 'skin', 'care', 'cloth', 'tech', 'rental', 'kamera',
        'beauty', 'express', 'kredit', 'collection', 'impor', 'preloved',
        'follow', 'follower', 'gain', '.id', '_id', 'bags'
    ],
    unfollow_whitelist=['example_user_1', 'example_user_2'])
    mode = 0
    
    bot.new_auto_mod()
