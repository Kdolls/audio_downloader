import pytube
import os

def downloader():
    """
    Takes user's video url input, extracts audio and downloads to main file.
    -user_input(str)
    """
    user_input = input(f'enter url: ')

    while True:
        try:
            if user_input:
                video_url = pytube.YouTube(user_input)
                audio_url = video_url.streams.filter(only_audio=True).first()

                # download folder
                audio_file = audio_url.download('audio stuff')
                print('download successful!!')
                break
        except ValueError:
            print('download failed...')


if __name__ == '__main__':
    downloader()
