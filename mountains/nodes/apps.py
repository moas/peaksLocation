from django.apps import AppConfig
from django.db.models import signals

from .receivers import (
    slugify_name, normalize_coordinates
)


class NodesConfig(AppConfig):
    name = 'mountains.nodes'

    def ready(self):
        signals.pre_save.connect(
            sender="nodes.Peak",
            receiver=slugify_name
        )

        signals.pre_save.connect(
            sender="nodes.Peak",
            receiver=normalize_coordinates
        )
