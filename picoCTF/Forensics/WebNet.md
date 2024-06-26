In these challenges, we've been given a pcap file and a private key. If we open the pcap file using wireshark, we can see that all the tcp streams are encrypted.

Thus, we use ssldump,

    ssldump -r capture.pcap -k picopico.key -d | grep picoCTF{

This will decrypt the pcap message using the private key and search for the flag
