# this file will store the default settings of our package

DEFAULT_SETTINGS = { # feel free to add, remove, adjust, etc. these as needed
    "difficulty": "medium",
    "hint_limit": 3,
    "disabled_hint_types":[]
}

# TODO: write function to allow users to optionally create a 'settings.json' file in their app to override the default settings.
#      check first if a 'settings.json' exists and return those values,
#      otherwise return the DEFAULT_SETTINGS
#      - handle cases where settings.json has an error ex. incorrect format or key
def load_settings():
    return 0

# TODO: optionally, write function to restore user's current settings.json to the default settings (to be used in the cli args, ex. user types 'pyriddles resetsettings')
def reset_settings():
    return 0
