# Discord.py Sentry Reporting

This is a small compatibility library that provides functionality to report errors from Discord.py to Sentry.

## Usage

```python
from discord_sentry_reporting import use_sentry

use_sentry(
    discord_client_object,  # it is typically named client or bot
    dsn="your_dsn_here"
    # put in any sentry keyword arguments (**kwargs) here
)
```
