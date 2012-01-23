Language
=======

Python

Problem Statement
=================

App Category
------------
Networking

DB
--
None

Simple part
===========

Create a web crawler app in python which, given a url seed, can crawl through all links on the page
and scan deep for a given level of depth. While crawling the app should be able to return the url
page containing a specific search text.

Input
=====

1. Url seed e.g. www.hackernews.com
2. Depth e.g. 5 (this means go into links on a page till 5 levels)
3. search text e.g. "python"

Output
======

The list of url that contains the specified text The Simple part is mandatory to be completed. If
you finish the simple part and are eager to take up something challenging, then here's a little
complex angle to the problem:


Complex part
============

> (Optional, if you complete simple part and want to take up something more challenging)

Write rules around the app for searching.

1. The return Url should contain a specific substring
2. Highlight in output if the url is amongst a long list of blacklisted urls (about 10000 blacklisted urls)
3. Search for multiple search strings and rank Urls as per the number of different search strings found and occurances of each search string in the page
4. Rank as per level of the Url w.r.t. seed url 
