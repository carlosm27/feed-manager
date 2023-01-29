import feedparser
from datetime import date

class Rss_info:
    def __init__(self, link:str):
        self.link = link

        self.feed = feedparser.parse(self.link)
        self.entries = self.feed['entries']

    def author_info(self):
        info_dict = {}

        info_dict['name'] = self.entries[0]['author']
        info_dict['number_entries'] = len(self.entries)
        info_dict['link'] = self.link

        return info_dict


    def last_entry_info(self):
        last_entry_dict = {}

        last_entry_dict['last_entry_title'] = self.entries[0]['title']
        last_entry_dict['last_entry_href'] = self.entries[0]['link']
        last_entry_dict['last_entry_date'] = self.entries[0]['published']

        return last_entry_dict


    def list_links(self):

        links_dict = {}
        for entry in self.feed['entries']:
            links_dict[entry.title] = entry.links[0]['href']
        return links_dict
