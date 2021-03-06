"""import pygame,sys
import moviepy.editor

video = moviepy.editor.VideoFileClip("C:/Users/Surya/Documents/PyGameProject/lore_final.mov")

pygame.init()
video.preview()

for event in pygame.event.get():
    if event.type == pygame.K_ESCAPE:
        pygame.quit()
    elif event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()"""

import cv2
import numpy as np
#ffpyplayer for playing audio
from ffpyplayer.player import MediaPlayer

video_path = "lore_final.mov"
def PlayVideo(video_path):
    video=cv2.VideoCapture(video_path)
    player = MediaPlayer(video_path)
    while True:
        grabbed, frame=video.read()
        audio_frame, val = player.get_frame()
        if cv2.waitKey(20) & 0xFF == ord("q"):
            break
        cv2.imshow("Video", frame)
        if val != 'eof' and audio_frame is not None:
            #audio
            img, t = audio_frame
    video.release()
    cv2.destroyAllWindows()
PlayVideo(video_path)

