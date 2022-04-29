from rest_framework import routers
from .views import FullCommentViewSet, PollViewSet, CommentThreeLevelViewSet

router = routers.DefaultRouter()
router.register(r'poll', PollViewSet)
router.register(r'comment', FullCommentViewSet, basename='comments')
router.register(r'comment_three_level', CommentThreeLevelViewSet, basename='comment_three_level')
urlpatterns = router.urls
