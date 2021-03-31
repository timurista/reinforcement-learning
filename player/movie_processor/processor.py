from moviepy.editor import VideoFileClip, CompositeVideoClip, TextClip, vfx, ColorClip
from moviepy.video.tools.segmenting import findObjects
import moviepy.video as mvid

# from moviepy.config import change_settings
# change_settings({"IMAGEMAGICK_BINARY": "/usr/local/bin/convert"})
# from moviepy.editor import imageio

# scipy needed
import numpy as np
import imageio_ffmpeg

import os

def main():
    path = "/tmp/"
    files = []
    for i in os.listdir(path):
        if os.path.isfile(os.path.join(path, i)) and "video_mario" in i:
            files.append(i)
    print("mario files")
    print(files)
    vidPath = "/private/tmp/video_mario_1614183995850.mp4"
    outPath = "/private/tmp/video_mario_1614183995850_edited.mp4"

    # todo allow from larger clip
    # message server
    # animations

    if os.path.isfile(outPath):
        os.remove(outPath)
    ideal_width = 1080
    ideal_height = 1920
    margin_x = 40
    box_width = ideal_width - margin_x
    video = (
        VideoFileClip(vidPath)
        .subclip(2, 50)
        .fx(vfx.crop, y2=540, x2=800)
        .resize(width=box_width)
    )
    # 1080 px by 1920 px
    # resize 1.1
    # video = video.resize(width=1080,height=1920)
    m_y = ideal_height - video.size[1]
    mtop = (m_y // 4)
    mbottom = m_y - mtop
    print(mbottom)
    print(video.size[0])
    video = video.margin(
        top=mtop,
        bottom=mbottom,
        left=margin_x // 2,
        right=margin_x // 2,
    )

    # video.display()
    # video = video.fx(fx.all.margin(bottom=1920),color="black")

    # r = findObjects(video)

    # r.
    # print("region video", r)
    size = video.size
    print(size)

    # size_args = np.array([size[0], 50]).astype(np.uint8)
    # Make the text. Many more options are available.

    messages = [
        (2,"mario tries randomly"),
        (3,"mario fails"),
        (5, "mario dies")
    ]
    clips = []
    for msg_idx in range(len(messages)):
        msg = messages[msg_idx]
        start_time = 0 if msg_idx == 0 else msg_idx - 1
        txt_clip = (
            TextClip(
                msg[1],
                font="Keep-Calm-Medium",
                fontsize=50,
                color="white",
                bg_color="red",
                size=(video.size[0], (mbottom*.8)//1),
            )
            .set_start(t=start_time)
            .set_position("bottom")
            .set_duration(msg[0])
        )
        clips.append(txt_clip)
    
    
    title_clip = (
        TextClip(
            "Mario AI - Development",
            font="Keep-Calm-Medium",
            fontsize=72,
            color="white",
            bg_color="black",
            size=(video.size[0], mtop),
        )
        .set_position("top")
        .set_duration(10)
    )
        

    # size_args = np.array([120, 100]).astype(np.uint8)
    # using np as hack for broadcasting issue
    # color_clip = ColorClip(size=size_args,color="red").set_duration(10).set_pos("center")
    speed_up = video.fx(vfx.speedx, 5)
    result = CompositeVideoClip(
        [
            speed_up,
            title_clip,
        ] + clips,
    )  # Overlay text on video
    result.write_videofile(outPath, fps=60)  # Many options..


if __name__ == "__main__":
    main()
