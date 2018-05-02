"""
Model for Backlog Space
"""

from .base import BacklogBase
from .. import utilities


class Space(BacklogBase):
    """
    Representing a Backlog space.
    """
    def __init__(self, client):
        super().__init__(client)
        self._attr = (
            ('id', 'spaceKey'),
            ('space_key', 'spaceKey'),
            ('name', 'name'),
            ('owner_id', 'ownerId'),
            ('lang', 'lang'),
            ('timezone', 'timezone'),
            ('report_send_time', 'reportSendTime'),
            ('text_formatting_rule', 'textFormattingRule'),
            ('created', 'created'),
            ('updated', 'updated'),
        )

    def activities(self, **params):
        """
        Get Backlog activities
        :param params: Optional parameters used for getting activities
        """
        return self.client.fetch_json(uri_path='space/activities', query_params=params)

    def icon(self):
        """
        Get space icon image file
        """
        return self.client.fetch_json(uri_path='space/image')

    def notification(self):
        """
        Get space notification
        """
        return self.client.fetch_json(uri_path='space/notification')

    @utilities.protect((1,))
    def disk_usage(self):
        """
        Representing Backlog disk usage for space
        """
        return self.client.fetch_json(uri_path='space/diskUsage')

    @utilities.protect((1, 2, 3, 4))
    def post_attachment(self, files):
        """
        Post attachment file to space
        :param file files: file objects
        """
        return self.client.fetch_json(uri_path='space/attachment', method='POST', files=files)


