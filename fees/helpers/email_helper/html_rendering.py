import os

from config.settings.base import PROJECT_ROOT

with open(os.path.join(PROJECT_ROOT, "fees", "helpers", "resources", "emails", "base.html"), encoding="utf-8") as f:
    base_template = f.read()

with open(os.path.join(PROJECT_ROOT, "fees", "helpers", "resources", "emails", "invite_email.html"), encoding="utf-8") as f:
    invite_template = f.read()


