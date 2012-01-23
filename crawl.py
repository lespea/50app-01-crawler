'''
Created on 2012-01-22

@author: Adam Lesperance
'''

import argparse
import re
import lxml.html
from urllib.parse import urlparse


DEBUG = False


def parse(
          target, max_level, stay_local, search_string,
          level=1, parsed_links={}):
    if (level > max_level):
        return parsed_links

    print("Parsing [level %d] - %s" % (level, target))

    try:
        hostname = urlparse(target)[1]
        tree = lxml.html.parse(target)
        root = tree.getroot()

        text = ''.join(root.itertext())
        parsed_links[target] = True if search_string.search(text) else False

        root.make_links_absolute(root.base)
        for link in root.iterlinks():
            href = link[2]
            if (stay_local and urlparse(href)[1] != hostname):
                continue
            if (href not in parsed_links):
                parse(href, max_level, stay_local, search_string,
                      level + 1, parsed_links)
    except Exception as e:
        print("Couldn't parse the target {}: {!s}".format(target, e))

    return parsed_links


def get_params():
    parser = argparse.ArgumentParser(description="Crawl a web page")
    parser.add_argument('--depth', '-d', dest="depth",
                        type=int, nargs='?', default=5,
                        help="How many levels to descend")
    parser.add_argument('--roam', '-r', dest="local",
                        action='store_false', default=True,
                        help="The crawler can go to different hostnames")
    parser.add_argument('search', help="The string to search for")
    parser.add_argument('target', help="The website to crawl")
    return parser.parse_args()


if __name__ == '__main__':
    params = get_params()
    if (DEBUG):
        print(params)

    links = parse(params.target, params.depth,
                  params.local, re.compile(params.search))

    print(("Found {:d} links; ".format(len(links)) +
           "the following URLs contained the search string {!s}")
          .format(params.search))
    for (key, value) in links.items():
        if (value):
            print("\t%s" % key)
