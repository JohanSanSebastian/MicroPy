import os

# All the various functions that call the AHK files

def startMeetAHK(): # For Google Meet
    os.startfile(
        "AHK files\\meet.ahk")


def startTeamsAHK(): # For Teams
    os.startfile(
        "AHK files\\teams.ahk")


def startZoomAHK(): # For Zoom
    os.startfile(
        "AHK files\\zoom.ahk")


def startDiscordAHK(): # For Discord
    os.startfile(
        "AHK files\\discord.ahk")
