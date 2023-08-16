<H1>Overview</H1>
<h2>Output file where site-to-site tunnel ip's are associated with a name, and categorises the security type into sections. See below for snippet of output</h2>

<p>So i know this script is pretty rudimental in that it does alot of outputting and formatting, but, it works.
The script will log into your firewall that shows your site-to-site vpn tunnels, unfortunately the output alone does not show the business name.
What this script does then is, it takes the output of the show command, and it goes through the config file of the firewall device and does a bunch of formatting and outputting until you get your desired result.</p>

Again, its rudimental, but works efficiently enough for my needs.

Hope this helps someone out there.

Cheers,
Dino

-------------------------------------------------------------------------------------------------------------------------------------
IKEv1
-----------------

Session Type: LAN-to-LAN

Connection   : SOME-CUSTOMER-NAME
Index        : 87570                  IP Addr      : 196.X.X.X
Protocol     : IKEv1 IPsec
Encryption   : IKEv1: (1)AES256  IPsec: (2)AES128
Hashing      : IKEv1: (1)SHA1  IPsec: (2)SHA1
Bytes Tx     : 161012989              Bytes Rx     : 321043987
Login Time   : 02:34:34 SAST Wed Aug 2 2023
Duration     : 14d 7h:25m:33s

Connection   : SOME-CUSTOMER-NAME2
Index        : 94383                  IP Addr      : 196.X.X.X
Protocol     : IKEv1 IPsec
Encryption   : IKEv1: (1)AES256  IPsec: (2)AES128
Hashing      : IKEv1: (1)SHA1  IPsec: (2)SHA1
Bytes Tx     : 121383479              Bytes Rx     : 235976077
Login Time   : 11:27:41 SAST Fri Aug 4 2023
Duration     : 11d 22h:32m:26s

-------------------

3DES
-----------------

Session Type: LAN-to-LAN

Connection   : SOME-CUSTOMER-NAME
Index        : 119602                 IP Addr      : 199.X.X.X
Protocol     : IKEv1 IPsec
Encryption   : IKEv1: (1)3DES  IPsec: (2)AES256
Hashing      : IKEv1: (1)SHA1  IPsec: (2)SHA1
Bytes Tx     : 218209401              Bytes Rx     : 3767527117
Login Time   : 12:15:39 SAST Sat Aug 12 2023
Duration     : 3d 21h:44m:35s

-------------------

AES128
-----------------

Session Type: LAN-to-LAN

Connection   : SOME-CUSTOMER-NAME
Index        : 87570                  IP Addr      : 196.X.X.X
Protocol     : IKEv1 IPsec
Encryption   : IKEv1: (1)AES256  IPsec: (2)AES128
Hashing      : IKEv1: (1)SHA1  IPsec: (2)SHA1
Bytes Tx     : 161015427              Bytes Rx     : 321048198
Login Time   : 02:34:34 SAST Wed Aug 2 2023
Duration     : 14d 7h:25m:47s

