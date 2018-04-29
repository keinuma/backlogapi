"""
Model Backlog Space information
"""


class Space:
    """
    Representing a Backlog space.
    """
    def __init__(self, client, space_key, name):
        super().__init__()
        self.client = client
        self.id = space_key
        self.name = name

    def __repr__(self):
        return f'<Space: {self.id}>'

    @classmethod
    def from_json(cls, client, response):
        """
        Create the Space Object by json response
        :param BacklogClient client:
        :param dict response: Space json object
        :return Space space: self
        """
        space = cls(client=client, space_key=response['spaceKey'], name=response['name'])
        space.owner_id = response['ownerId']
        space.lang = response['lang']
        space.timezone = response['timezone']
        space.report_send_time = response['reportSendTime']
        space.text_formatting_rule = response['textFormattingRule']
        space.created = response['created']
        space.updated = response['updated']
        return space

    def disk_usage(self):
        """
        Representing Backlog disk usage for space
        """
        return self.client.fetch_json(uri_path='space/diskUsage')

