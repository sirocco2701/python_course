from getpass import getpass
import instaloader 

user= input("Username: ")
pas = getpass("Password: ")
L = instaloader.Instaloader()
L.login(user, pas)
profile = instaloader.Profile.from_username(L.context, user)

f = open("followers.txt", "r")
old = []
for line in f:
    old.append(line.strip())
f.close()

new = []
for follower in profile.get_followers():
    new.append(follower.user)

for newFollower in new:
    if newFollower not in old:
        print(newFollower)

f = open("followers.txt", "w")
for newFollower in new:
    f.write(newFollower + "\n")
f.close()