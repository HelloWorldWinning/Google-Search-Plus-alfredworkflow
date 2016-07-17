# -*- coding: utf-8 -*-
# 
# Copyright © 2016 ethan-funny (http://funhacks.net)
#
# MIT Licence. See http://opensource.org/licenses/MIT
#
# Created on 2016-06-18
#

import alfred
from google import google


def process(query):
    """ Entry point
    :param query: query string
    :return:
    """
    if query:
        results = alfred_items_for_query(query)
        xml = alfred.xml(results)
        alfred.write(xml)


def alfred_items_for_query(query):
    alfred_results = []
    with open('port', 'r') as infile:
        port = int(infile.read())

    search_results = google.search(query, port)
    for result in search_results:
        title = result.get('title', '') #.decode('utf-8')
        href = result.get('href', '') #.decode('utf-8')

        # output href & set title variable
        attr = {}
        attr['arg'] = "{\"alfredworkflow\": {\"arg\": \"" + href + "\", \"variables\": {\"title\": \"" + title + "\"}}}"
        alfred_results.append(alfred.Item(
            title=title,
            subtitle=href,
            attributes=attr,
            icon='icon.png',
        ))

    return alfred_results


if __name__ == '__main__':
    try:
        query_str = alfred.args()[0]
    except IndexError:
        query_str = None

    process(query_str)
