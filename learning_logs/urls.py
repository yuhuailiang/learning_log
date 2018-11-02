"""定义learning_logs的URL模式"""

from django.urls import path
from . import views


app_name = 'learning_logs'
urlpatterns = [
    # 主页
    path('', views.index, name='index'),

    # 显示所有的主题
    path('topics/', views.topics, name='topics'),

    # 显示特定主题
    path('topics/<topic_id>/', views.topic, name='topic'),

    # 创建新主题
    path('new_topic/', views.new_topic, name='new_topic'),

    # 创建新条目
    path('new_entry/<topic_id>/', views.new_entry, name='new_entry'),

    # 编辑既有条目
    path('edit_entry/<entry_id>', views.edit_entry, name='edit_entry'),

]
