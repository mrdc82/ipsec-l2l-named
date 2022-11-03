# ipsec-l2l-named
Output file where site-to-site tunnel ip's are associated with a name

So i know this script is pretty rudimental in that it does alot of outputting and formatting, but, it works.

The script will log into your firewall that shows your site-to-site vpn tunnels, unfortunately the output alone does not show the business name.

What this script does then is, it takes the output of the show command, and it goes through the config file of the firewall device and does a bunch of formatting and outputting until you get your desired result.

Again, its rudimental, but works efficiently enough for my needs.

Hope this helps someone out there.

Cheers,
Dino
