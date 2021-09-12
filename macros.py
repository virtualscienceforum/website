from datetime import datetime, timezone
from markdown.extensions.toc import slugify_unicode

def define_env(env):
    env.macro((lambda: datetime.now(tz=timezone.utc)), "now")
    env.filter((lambda text: slugify_unicode(text, "-")), "a")
    return env