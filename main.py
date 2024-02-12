


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


# Import the necessary libraries
# import requests
# from bs4 import BeautifulSoup
# import os
#
# # Set up the URL of the website to download from
# url = "https://www.example.com/audio"
#
# # Send a GET request to the website and get the HTML response
# response = requests.get(url)
#
# # Parse the HTML content using BeautifulSoup
# soup = BeautifulSoup(response.content, 'html.parser')
#
# # Find the audio file on the page
# audio_file = soup.find("audio")
#
# # Download the audio file
# audio_file.streaming("download")
#
# # Save the audio file to a location on your computer
# os.makedirs(os.path.dirname(audio_file.name), exist_ok=True)
# with open(audio_file.name, "wb") as f:
#     f.write(audio_file.getvalue())
# ```
# This script uses the `requests` library to send a GET request to the
# website and get the HTML response. It then uses the `BeautifulSoup`
# library to parse the HTML content and find the audio file on the page. The
# script then uses the `streaming()` method of the `BeautifulSoup` object to
# download the audio file. Finally, it saves the audio file to a location on
# your computer using the `os` and `open` functions.
#
# You can modify this code to suit your needs, such as changing the URL of
# the website, the location where the audio file is saved, or the format of
# the audio file.
#
# Keep in mind that downloading audio files from a website without
# permission may violate the website's terms of service and copyright laws.
# Be sure to only use this script for legal and ethical purposes.
