from pytube import YouTube
from moviepy.editor import *

def download_video(url, output_path):
    try:
        yt = YouTube(url)
        stream = yt.streams.filter(only_audio=True).first()
        if stream:
            stream.download(output_path, filename="audio")
            print("Video đã được tải xuống thành công!")
        else:
            print("Không tìm thấy định dạng audio phù hợp.")
    except Exception as e:
        print("Đã xảy ra lỗi khi tải xuống video:", str(e))

def convert_to_mp3(input_path, output_path):
    try:
        video = AudioFileClip(input_path)
        video.write_audiofile(output_path)
        print("Đã chuyển đổi video sang MP3 thành công!")
    except Exception as e:
        print("Đã xảy ra lỗi khi chuyển đổi video sang MP3:", str(e))

if __name__ == "__main__":
    video_url = input("Nhập URL của video YouTube: ")
    output_path = input("Nhập đường dẫn để lưu file MP3 (ví dụ: '/path/to/save/audio.mp3'): ")

    download_video(video_url, ".")
    convert_to_mp3("audio.mp4", output_path)
