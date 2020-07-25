#!/usr/bin/env python3
import mackee

#===========================================
# callback to report images for the video
#===========================================
def findImages(video):
	images = video.get('images')
	if(images):
		poster = images.get('poster')
		thumb  = images.get('thumbnail')

		line = video.get('id')+','
		line += (poster.get('src')+',') if poster else ','
		line += (thumb.get('src')) if thumb else ''

		print(line)

#===========================================
# only run code if it's not imported
#===========================================
if __name__ == '__main__':
	mackee.main(findImages)