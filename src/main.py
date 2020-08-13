import generated.person_pb2
import generated.person_info_pb2
import os

if __name__ == "__main__":
    # fill proto object
    ############
    # define a person that acts as a friend
    #############
    friend_info = person_info_pb2.PersonInfo()
    friend_info.age = 40
    friend_info.sex = person_info_pb2.Sex.M
    friend_info.height = 165
    friend_person = person_pb2.Person()
    friend_person.info.CopyFrom(friend_info)
    friend_person.friends.extend([])  # no friends :-(
    #######
    # define friendship characteristics
    ########
    friendship = person_pb2.Friend()
    friendship.friendship_duration = 365.1
    friendship.shared_hobbies.extend(["books", "daydreaming", "unicorns"])
    friendship.person.CopyFrom(friend_person)
    #######
    # assign the friend to a person
    #########
    person_info = person_info_pb2.PersonInfo()
    person_info.age = 30
    person_info.sex = person_info_pb2.Sex.M
    person_info.height = 184
    person = person_pb2.Person()
    person.info.CopyFrom(person_info)
    person.friends.extend([friendship])  # person with a single friendproto_friend
    ####
    # store serialized proto
    ####
    out_dir = "proto_dump"
    with open(os.path.join(out_dir, "person.protobuf"), "w") as f:
        # human-readable output
        f.write(str(person))
    with open(os.path.join(out_dir, "person.pb"), "wb") as f:
        # binary output
        f.write(person.SerializeToString())

