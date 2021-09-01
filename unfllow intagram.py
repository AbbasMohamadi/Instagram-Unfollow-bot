import time
from InstagramAPI import InstagramAPI
import random
from colored import fg, bg, attr


def getTotalFollowers(api, user_id):
    """
    Returns the list of followers of the user.
    It should be equivalent of calling api.getTotalFollowers from InstagramAPI
    """

    followers = []
    next_max_id = True
    while next_max_id:
        # first iteration hack
        if next_max_id is True:
            next_max_id = ''

        _ = api.getUserFollowers(user_id, maxid=next_max_id)
        followers.extend(api.LastJson.get('users', []))
        next_max_id = api.LastJson.get('next_max_id', '')
    return followers


def getTotalFollowings(api, user_id):
    """
    Returns the list of followers of the user.
    It should be equivalent of calling api.getTotalFollowers from InstagramAPI
    """

    followers = []
    next_max_id = True
    while next_max_id:
        # first iteration hack
        if next_max_id is True:
            next_max_id = ''

        _ = api.getUserFollowings(user_id, maxid=next_max_id)
        followers.extend(api.LastJson.get('users', []))
        next_max_id = api.LastJson.get('next_max_id', '')
    return followers


def nonFollowers(followers, followings):
    nonFollowers = {}
    dictFollowers = {}
    for follower in followers:
        dictFollowers[follower['username']] = follower['pk']

    for followedUser in followings:
        if followedUser['username'] not in dictFollowers:
            nonFollowers[followedUser['username']] = followedUser['pk']

    return nonFollowers



def unFollow(number: int):
    nu = 1

    #here you should replace your instagram username and password to get to work
    #remember that your 2nd step verification should be off if you want this code is working

    api = InstagramAPI('your instagram username', 'your instagram password')

    api.login()
    user_id = api.username_id
    followers = getTotalFollowers(api, user_id)
    following = getTotalFollowings(api, user_id)
    nonFollow = nonFollowers(followers, following)
    totalNonFollowers = len(nonFollow)
    print('Number of followers:', len(followers))
    print('Number of followings:', len(following))
    print('Number of nonFollowers:', len(nonFollow))

    for i in range(number):
        if i >= totalNonFollowers:
            break
        #user = list(nonFollow.keys())[len(nonFollow) - 1]
        user = random.choice(list(nonFollow.keys()))


        api.unfollow(nonFollow[user])
        nonFollow.pop(user)
        color = fg("white")
        print(str(color) + user)

        color = fg("green")
        reset = attr('reset')
        print(str(color) + "succsessful " + str(nu))
        nu = nu + 1

        color = fg("red")
        print(color + 'Number of nonFollowers:', str(len(nonFollow)))

        time_dirucation = random.uniform(10, 60)

        color = fg("blue")
        print(color + "next unfollow in "+str(time_dirucation)+" seconds \n")
        time.sleep(time_dirucation)




if __name__ == "__main__":

    # waits 15 seconds and run the code AAaaagaaain !! (monica refrence in friends)

    unFollow(15)