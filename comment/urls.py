from rest_framework import routers
from .views import CommentViewSet, PollViewSet, CommentThreeLevelViewSet

router = routers.DefaultRouter()
router.register(r'poll', PollViewSet)
router.register(r'comment', CommentViewSet)
router.register(r'comment_three_level', CommentThreeLevelViewSet)
urlpatterns = router.urls
