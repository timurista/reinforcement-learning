from moviepy.editor import VideoFileClip, CompositeVideoClip, TextClip, vfx
# from moviepy.config import change_settings
# change_settings({"IMAGEMAGICK_BINARY": "/usr/local/bin/convert"})
# from moviepy.editor import imageio
import imageio_ffmpeg

# imageio.plugins.ffmpeg.download()
import os
# /Users/turista/projects/reinforcement-learning/player
# FFMPEG_BINARY = os.getenv('FFMPEG_BINARY', '.venv/lib/python3.8/site-packages/imageio_ffmpeg/binaries/ffmpeg-osx64-v4.2.2')
# FFMPEG_BINARY = os.getenv('FFMPEG_BINARY', '.venv/lib/python3.8/site-packages/imageio_ffmpeg/binaries/ffmpeg-osx64-v4.2.2')

# IMAGEMAGICK_BINARY = os.getenv('IMAGEMAGICK_BINARY', '.venv/lib/python3.8/site-packages/imageio_ffmpeg/binaries/ffmpeg-osx64-v4.2.2')
def main():
    path = '/tmp/'
    files = []
    for i in os.listdir(path):
        if os.path.isfile(os.path.join(path,i)) and 'video_mario' in i:
            files.append(i)
    print("mario files")
    print(files)
    vidPath="/private/tmp/video_mario_1614183995850.mp4"
    outPath="/private/tmp/video_mario_1614183995850_edited.mp4"


    video = VideoFileClip(vidPath).subclip(2,50).fx(vfx.crop, y2=500).fx(vfx.accel_decel)

    # Make the text. Many more options are available.
    txt_clip = ( TextClip("Mario Fail test",fontsize=70,color='white')
                .set_position('bottom')
                .set_duration(5) )

    speed_up = video.fx( vfx.speedx, 5)
    result = CompositeVideoClip([speed_up, txt_clip]) # Overlay text on video
    result.write_videofile(outPath,fps=60) # Many options..

if __name__ == "__main__":
    main()
