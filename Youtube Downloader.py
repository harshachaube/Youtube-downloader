#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pytube
youtube_url = input("Enter the youtube url: ") # youtube url to be downloaded
yt = pytube.YouTube(youtube_url)
video = yt.streams.first()
video.download('C:/path of the folder/') # path, where to video download.

