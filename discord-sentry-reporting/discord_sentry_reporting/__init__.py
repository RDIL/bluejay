import sentry_sdk
from discord import ClientException


def use_sentry(client, **sentry_args):
    """
    Use this compatibility library as a bridge between Discord and Sentry.

    Arguments:
        client: the Discord client object (e.g. `discord.AutoShardedClient`)
        sentry_args: keyword arguments to pass to the Sentry SDK
    """
    sentry_sdk.init(sentry_args)

    @client.event
    async def on_error(event, *args, **kwargs):
        """
        Yes, this will throw a ValueError. THIS IS ON PURPOSE,
        because otherwise, it just raises 'ExceptionName: coro'
        (coro is the name of the coroutine the exception was
        thrown on), and *doesn't give us an actual stacktrace*!
        """
        sentry_sdk.capture_exception(event)
