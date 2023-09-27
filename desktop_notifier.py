from plyer import notification
import time
import argparse
import vlc
 

App = "Desktop Notifyer"
Icon = "clock.ico"
Title = "Take a Break!!!"
ring = "alarm.mp3"


#taking arguments
parser = argparse.ArgumentParser()
parser.add_argument("delay",type = float,help="Time to display next notification in minutes")
parser.add_argument("-name","--appName",type=str,help="App name to display",default=App)
parser.add_argument("-icon","--icon",type=str,help="Path to icon to display",default=Icon)
parser.add_argument("-title","--title",type=str,help="Purpose of notification",default=Title)
parser.add_argument("-desc","--msg",type=str,help="To give long description of notifying",default=None)
parser.add_argument("-t","--timeout",type= float,help="How much long a notification have to stay",default=10)
parser.add_argument("-r","--repeats",type= float,help="How much time you want to repeat this notification",default=None)
parser.add_argument("-ring","--ringtone",type=str,help="Path to eingtone ",default=ring)
args = parser.parse_args()

#assigning default title to notification
if args.msg is None:
   args.msg = f"You are working more than {int(args.delay)} minutes"

i = 1
while i <= args.repeats :
    print(f"\nBreak number {i}")
    time.sleep(0.5)
    player = vlc.MediaPlayer(ring)
    player.set_time(0)
    player.play()
    notification.notify(app_name=args.appName,app_icon=args.icon,title=args.title,message=args.msg,timeout=args.timeout)
    sec = args.delay*60
    time.sleep(sec)
    i = i + 1