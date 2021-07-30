from moviepy.editor import *

class VideoCreation():
    def __init__(self, vidPath, audPath, finalVidPath):
        super().__init__()
        self.vidPath = vidPath
        self.audPath = audPath
        self.finalVidpath = finalVidPath
        self.counter = 1


    def generateVideo(self):
        # Getting the main clip and his duration
        vidExtension = self.getFileExtension(self.vidPath)
        print(vidExtension)
        if (vidExtension != "mp4"):
            self.vidPath = self.convertVideo(self.vidPath)
        print(self.vidPath)
        clip = VideoFileClip(self.vidPath)
        vidDuration = clip.duration

        # Getting the audio and his duration
        audio = AudioFileClip(self.audPath)
        audDuration = audio.duration

        # Calculating times the video will repeat
        timesVid = audDuration / vidDuration

        # Initializing the clipList
        clipsList = [clip]

        # Populating the clipList
        while (self.counter < timesVid):
            clipsList.append(clip)
            self.counter += 1

        # Concatenating all clips 
        video = concatenate_videoclips(clipsList, method='compose')

        # Trim the final Video to match the audio duration
        videoFinal = video.set_end(audDuration)

        # Set the audio
        videoFinal = videoFinal.set_audio(audio)

        # Rendering the video
        videoFinal.write_videofile(self.finalVidpath)

    def getFileExtension(self, string: str) -> str : 
        dotIndex = string.index(".") + 1
        return string[dotIndex:]

    def convertVideo(self, video: str) -> str:
        originalVideo = VideoFileClip(video)
        originalVideo.write_videofile("./cache/vidConverted.mp4")
        return "./cache/vidConverted.mp4"