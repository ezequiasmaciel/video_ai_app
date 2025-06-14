from moviepy.editor import *

def compose_video(imgs, audio_path, subs):
    clips = []
    for img in imgs:
        clips.append(ImageClip(img).set_duration(5))
    video = concatenate_videoclips(clips)
    video = video.set_audio(AudioFileClip(audio_path))
    output = "output/video_final.mp4"
    video.write_videofile(output, fps=24)
    return output
