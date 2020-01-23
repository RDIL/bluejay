import sentry_sdk


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
        sentry_sdk.capture_exception(event)
