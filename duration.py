##
'''
runtime of all the videos in the first five playlists

'''
##


from googleapiclient.discovery import build

info = build('youtube', 'v3', developerKey='AIzaSyDYz-R9ERmZ2gu4PZ_xUBYHaCCSL19b6a0')


request  = info.playlists().list(part='contentDetails, snippet',channelId='UC9qkQ1s5iWY6PzYZ5BiD-tQ')

response = request.execute()




for things in response['items']:
	idnames=things['id']

	more_info = info.playlistItems().list(part='contentDetails',playlistId=idnames)
	answer = more_info.execute()
	for objects in answer['items']:
		videoID = objects['contentDetails']['videoId']
		final_request = info.videos().list(part="contentDetails",id=videoID)
		final_response = final_request.execute()
		for duration in final_response['items']:
			runningTotal = duration['contentDetails']['duration']
			print(runningTotal)
			


