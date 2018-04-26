from channels.routing import ProtocolTypeRouter, URLRouter
from channels_test import consumers
from django.conf.urls import url

# channel_routing = [
#     route("websocket.receive", websocket_receive, path=r"^/chat/"),
# ]


app = ProtocolTypeRouter({
    "websocket": URLRouter([
        url(r"^test/$", consumers.BaseConsumer),
    ]),
})
