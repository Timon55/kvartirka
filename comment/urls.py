from rest_framework import routers
from .views import CommentViewSet, PollViewSet

router = routers.DefaultRouter()
router.register(r'poll', PollViewSet)
router.register(r'comment', CommentViewSet)

urlpatterns = router.urls
