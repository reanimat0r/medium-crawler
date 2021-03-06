#!/usr/bin/env python3


import json
import os
import re
import textwrap

def create_dir(dirname, username):
    path = os.path.join(dirname, username)
    if not os.path.exists(path):
        os.makedirs(path)

def save_post_as_text(username, post, dir="data"):
    fname = os.path.join(dir, username, post['timestamp'] + '-' + re.sub(r'\s+', '-', post['title']))
    print("Filename :: {}".format(fname))
    with open(fname, 'w') as f:
        f.write(textwrap.fill(post['content'], 140))

def save_post_as_json(username, post, dir="data"):
    fname = os.path.join(dir, username, re.sub(r'\s+', '-', post['title']) + ".json")
    print("Filename :: {}".format(fname))
    with open(fname, 'w') as f:
        json.dump(post, f, indent=4)

def save_json_single(posts, dir="data"):
    fname = os.path.join(dir, "dump.json")
    with open(fname, 'w') as f:
        json.dump(posts, f, indent=4)

def save_posts(posts, dir="data", dump_type='text'):
    print("Dumping all the shit...")
    print("Total number of posts :: {}".format(len(posts)))
    func = save_post_as_text if dump_type=='text' else save_post_as_json
    for post in posts:
        func(post, dir)


def main():
    pass

if __name__ == "__main__":
    main()

