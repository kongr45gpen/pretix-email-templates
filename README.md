# Pretix Email Templates

This is a plugin for Pretix that creates a simple custom template for emails.

It is directly based on the NETWAYS implementation at https://github.com/NETWAYS/pretix-email-net/.

## Installation:

Install the plugin with ``pip install pretix-net-mail``.

Then reconfigure Pretix with the commands ``python -m pretix rebuild && python migrate``.

Then restart the server with ``systemctl restart pretix-web pretix-worker`` (depending on the installation)


