# Pretix Email Templates

This is a plugin for Pretix that creates a simple custom template for emails.

It is directly based on the NETWAYS implementation at https://github.com/NETWAYS/pretix-email-net/.

## Installation:

Run the following commands to install the plugin:
```bash
cd /pretalx/src
git clone https://github.com/kongr45gpen/pretix-email-templates.git
cd pretix-email-templates

# For production
pip install -e .

# For development
python setup.py develop

python -m pretix rebuild
systemctl restart pretix-web pretix-worker # depending on the installation
```
