from django.urls import path
from nihon import views

urlpatterns = [
    path("", views.landing, name="landingpage"),
    path('download', views.download_file, name="downloadfile"),
    path('/download1', views.download_file1, name="downloadfile1"),
    path('/download2', views.download_file2, name="downloadfile2"),
    path('/download3', views.download_file3, name="downloadfile3"),
    path('/download4', views.download_file4, name="downloadfile4"),
    path('/download5', views.download_file5, name="downloadfile5"),
    path('/download6', views.download_file6, name="downloadfile6"),
    path('/download7', views.download_file7, name="downloadfile7"),
    path('/download8', views.download_file8, name="downloadfile8"),
    path("sign-out-page", views.home, name="home"),
    path("sign-in", views.plogin, name="login"),
    path("logout", views.logoutUser, name="logout"),
    path("sign-up", views.preg, name="register"),
    path("courses", views.course, name="courses"),
    path("downloadables", views.learn, name="download"),
    path("downloadables2", views.learn2, name="download2"),
    
]