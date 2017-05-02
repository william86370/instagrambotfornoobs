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
               login="william86370",
               password="password",
               like_per_day=0,
               comments_per_day=0,
               tag_list=['newbygains', 'fitness', '24hourfitness','gym','gains','armday','eatclean','healthylife','legday','chestday'],
               tag_blacklist=['nigger', 'pony'],
               user_blacklist={},
               max_like_for_one_tag=1,
               follow_per_day=0,
               follow_time=61 ,
               unfollow_per_day=500,
               unfollow_break_min=15,
               unfollow_break_max=30,
               log_mod=0,
               proxy='',
               # Use unwanted_username_list to block usernames containing a string
               ## Will do partial matches; i.e. 'mozart' will block 'legend_mozart'
               ### 'free_followers' will be blocked because it contains 'free'
               unwanted_username_list=['pony'],
               unfollow_whitelist=['example_user_1', 'william86370'])
bot.new_auto_mod()
