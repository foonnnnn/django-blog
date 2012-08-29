from django.contrib.syndication.views import Feed

from blog.models import Entry


class LatestEntries(Feed):
    title = 'Hope Town Lodge Blog'
    link = '/blog/'
    description = 'Latest blog posts Hope Town Lodge'

    def items(self):
        return Entry.live.all()[:30]

    def item_pubdate(self, item):
        return item.pub_date

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.body_html