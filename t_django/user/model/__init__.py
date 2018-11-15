class UserInfo(object):

    def __init__(self, user):
        self.id = user.id
        self.username = user.username
        self.email = user.email
        self.create_time = user.date_joined.strftime("%Y-%m-%d-%H %H:%M:%S")

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'create_time': self.create_time
        }
