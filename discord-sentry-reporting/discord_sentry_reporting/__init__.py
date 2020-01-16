import sentry_sdk


def use_sentry(client, **sentry_args):
    sentry_sdk.init(sentry_args)

    @client.event
    def on_error(event, *args, **kwargs):
        sentry_sdk.capture_exception(event)
