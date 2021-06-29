from . import views
from django.urls import path

urlpatterns = [
    path('',views.add,name='add'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/', views.update, name='update'),
    path('cbvhome', views.mylistview.as_view(), name='cbvhome'),
    path('cbvdetail/<int:pk>/',views.mydetailview.as_view(),name='cbvdetail'),
    path('cbvupdate/<int:pk>/', views.myupdateview.as_view(), name='cbvupdate'),
    path('cbvdelete/<int:pk>/', views.mydeleteview.as_view(), name='cbvdelete')

]