class Connector(object):
    """
    Connector class
    Provides an universal API connector for VK and Twitter social networks
    Takes an initialized instance of known social network class defined in social_networks.py
    """

    def __init__(self, social_network):
        self.social_network = social_network

    def get_user_profile(self, user_id=None):
        return self.social_network.get_user_profile(user_id)

    def get_user_friends(self, user_id=None):
        return self.social_network.get_user_friends(user_id)

    def get_user_posts(self, user_id=None):
        return self.social_network.get_user_posts(user_id)

