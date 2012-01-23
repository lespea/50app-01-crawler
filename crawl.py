'''
Created on 2012-01-22

@author: Adam Lesperance
'''

import re
import lxml.html
from urllib.parse import urlparse


default_base_url = "http://www.cnn.com"
default_max_level = 2
default_search_string = re.compile(r"(?i)sopa")
default_stay_local = True

DEBUG = True


def parse(
          target=default_base_url,
          level=1,
          max_level=default_max_level,
          stay_local=default_stay_local,
          search_string=default_search_string,
          parsed_links={}):
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
                parse(href, level + 1, max_level, stay_local,
                      search_string, parsed_links)
    except Exception as e:
        print("Couldn't parse the target {}: {!s}".format(target, e))

    return parsed_links


if __name__ == '__main__':
    links = parse()
    print(("Found {:d} links; ".format(len(links)) +
           "the following URLs contained the search string {!s}")
          .format(default_search_string))
    for (key, value) in links.items:
        if (value):
            print("\t%s" % key)
