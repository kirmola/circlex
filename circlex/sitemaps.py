from django.contrib.sitemaps import Sitemap
from api.models import Post, ExtendedUser


class UserSitemap(Sitemap):
    limit = 50000
    protocol = "https"

    def items(self):
        return ExtendedUser.objects.all()



class PostSitemap(Sitemap):
    limit = 50000
    protocol = "https"
    
    def items(self):
        return Post.objects.all()