# -*- coding: utf-8 -*-

from youtube import YouTube


def main():

    first_message = int(input('\n\nHello!\nI will help you find the right videos on the Youtube platform. At the moment, this program has the following functions:\n\n1 - Search for videos by name\n2 - Search for videos on a given channel\n3 - Find the videos that are on the "Trending" tab.\n\nEnter the number of the desired function:\n\n'))
    start = YouTube()

    if first_message == 1:
        user_text = str(input("\nSearch:\n\n"))
        print("\nStarting the search...")
        result = start.search_videos(user_text=user_text)
        print("\nInformation received:")
        print(f"{result[0]}\n{result[1]}\n{result[2]}\n{result[3]}\n{result[4]}\n{result[5]}\n{result[6]}\n{result[7]}\n{result[8]}\n{result[9]}\n\n")

    elif first_message == 2:
        try:
            user_url = str(input("\nEnter the link to the channel:\n\n"))
            name_channel = start.search_name_channel(user_url=user_url)
            print(
                f'\n\nStarting the search videos from channel - "{name_channel}"\n\n')
            result = start.search_videos_from_channel(user_url=user_url)
            print("\nInformation received:")
            print(
                f"{result[0]}\n{result[1]}\n{result[2]}\n{result[3]}\n{result[4]}\n{result[5]}\n{result[6]}\n{result[7]}\n{result[8]}\n{result[9]}\n\n")
        except:
            print("Error! Invalid link to the channel.")

    else:
        result = start.search_youtube_trends()
        print("\nInformation received:")
        print(f"{result[0]}\n{result[1]}\n{result[2]}\n{result[3]}\n{result[4]}\n{result[5]}\n{result[6]}\n{result[7]}\n{result[8]}\n{result[9]}\n\n")


if __name__ == "__main__":
    main()
