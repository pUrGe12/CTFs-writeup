I used strings on the file to extract all the relevant ASCII characters:

    strings dump.pcap

The ouput looked like the following:

    Flying on Ethernet secret: Is this the flag
    Flying on Ethernet secret: Is this the flag
    Flying on Ethernet secret: Is this the flag
    Flying on Ethernet secret: Is this the flag
    Flying on Ethernet secret: Is this the flag
    Flying on Ethernet secret: Is this the flag
    Flying on Ethernet secret: Is this the flag
    Flying on Ethernet secret: Is this the flag
    Flying on Ethernet secret: Is this the flag
    _googlecast
    _tcp
    local
    _googlecast
    _tcp
    local
    _googlecast
    _tcp
    local
    _googlecast
    _tcp
    local
    +Chromecast-18e2a8da30459b730aec93a71af19988
    _googlecast
    _tcp
    local
    _googlecast
    _tcp
    local
    _googlecast
    _tcp
    local
    _googlecast
    _tcp
    local
    +Chromecast-18e2a8da30459b730aec93a71af19988
    _googlecast
    _tcp
    local
    .+Chromecast-18e2a8da30459b730aec93a71af19988
    #id=18e2a8da30459b730aec93a71af19988#cd=EB3B62CAFB4F51F0114CFB58C4FE2C2F
    rm=B8B7BA5A0CEB76E5
    ve=05
    md=Chromecast
    ic=/setup/icon.png
    fn=Living Room TV	ca=465413
    st=0
    bs=FA8FCA54567B
    nf=2
    I$18e2a8da-3045-9b73-0aec-93a71af19988
    _googlecast
    _tcp
    local
    .+Chromecast-18e2a8da30459b730aec93a71af19988
    #id=18e2a8da30459b730aec93a71af19988#cd=EB3B62CAFB4F51F0114CFB58C4FE2C2F
    rm=B8B7BA5A0CEB76E5
    ve=05
    md=Chromecast
    ic=/setup/icon.png
    fn=Living Room TV	ca=465413
    st=0
    bs=FA8FCA54567B
    nf=2
    I$18e2a8da-3045-9b73-0aec-93a71af19988
    _googlecast
    _tcp
    local
    .+Chromecast-18e2a8da30459b730aec93a71af19988
    #id=18e2a8da30459b730aec93a71af19988#cd=EB3B62CAFB4F51F0114CFB58C4FE2C2F
    rm=B8B7BA5A0CEB76E5
    ve=05
    md=Chromecast
    ic=/setup/icon.png
    fn=Living Room TV	ca=465413
    st=0
    bs=FA8FCA54567B
    nf=2
    I$18e2a8da-3045-9b73-0aec-93a71af19988
    _googlecast
    _tcp
    local
    .+Chromecast-18e2a8da30459b730aec93a71af19988
    #id=18e2a8da30459b730aec93a71af19988#cd=EB3B62CAFB4F51F0114CFB58C4FE2C2F
    rm=B8B7BA5A0CEB76E5
    ve=05
    md=Chromecast
    ic=/setup/icon.png
    fn=Living Room TV	ca=465413
    st=0
    bs=FA8FCA54567B
    nf=2
    I$18e2a8da-3045-9b73-0aec-93a71af19988
    +Chromecast-18e2a8da30459b730aec93a71af19988
    _googlecast
    _tcp
    local
    #id=18e2a8da30459b730aec93a71af19988#cd=EB3B62CAFB4F51F0114CFB58C4FE2C2F
    rm=B8B7BA5A0CEB76E5
    ve=05
    md=Chromecast
    ic=/setup/icon.png
    fn=Living Room TV	ca=465413
    st=0
    bs=FA8FCA54567B
    nf=2
    ScTo
    iBwaWNvQ1RGe1Could the flag have been splitted?
    iBwaWNvQ1RGe1Could the flag have been splitted?
    iBwaWNvQ1RGe1Could the flag have been splitted?
    iBwaWNvQ1RGe1Could the flag have been splitted?
    iBwaWNvQ1RGe1Could the flag have been splitted?
    iBwaWNvQ1RGe1Could the flag have been splitted?
    iBwaWNvQ1RGe1Could the flag have been splitted?
    iBwaWNvQ1RGe1Could the flag have been splitted?
    iBwaWNvQ1RGe1Could the flag have been splitted?
    iBwaWNvQ1RGe1Could the flag have been splitted?
    iBwaWNvQ1RGe1Could the flag have been splitted?
    iBwaWNvQ1RGe1Could the flag have been splitted?
    iBwaWNvQ1RGe1Could the flag have been splitted?
    iBwaWNvQ1RGe1Could the flag have been splitted?
    iBwaWNvQ1RGe1Could the flag have been splitted?
    iBwaWNvQ1RGe1Could the flag have been splitted?
    iBwaWNvQ1RGe1Could the flag have been splitted?
    iBwaWNvQ1RGe1Could the flag have been splitted?
    iBwaWNvQ1RGe1Could the flag have been splitted?
    iBwaWNvQ1RGe1Could the flag have been splitted?
    iBwaWNvQ1RGe1Could the flag have been splitted?
    iBwaWNvQ1RGe1Could the flag have been splitted?
    iBwaWNvQ1RGe1Could the flag have been splitted?
    iBwaWNvQ1RGe1Could the flag have been splitted?
    iBwaWNvQ1RGe1Could the flag have been splitted?
    AABBHHPJGTFRLKVGhpcyBpcyB0aGUgc2VjcmV0OiBwaWNvQ1RGe1IzNERJTkdfTE9LZF8=
    PBwaWUvQ1RGesabababkjaASKBKSBACVVAVSDDSSSSDSKJBJS
    PBwaWUvQ1RGesabababkjaASKBKSBACVVAVSDDSSSSDSKJBJS
    PBwaWUvQ1RGesabababkjaASKBKSBACVVAVSDDSSSSDSKJBJS
    PBwaWUvQ1RGesabababkjaASKBKSBACVVAVSDDSSSSDSKJBJS
    PBwaWUvQ1RGesabababkjaASKBKSBACVVAVSDDSSSSDSKJBJS
    PBwaWUvQ1RGesabababkjaASKBKSBACVVAVSDDSSSSDSKJBJS
    PBwaWUvQ1RGesabababkjaASKBKSBACVVAVSDDSSSSDSKJBJS
    PBwaWUvQ1RGesabababkjaASKBKSBACVVAVSDDSSSSDSKJBJS
    PBwaWUvQ1RGesabababkjaASKBKSBACVVAVSDDSSSSDSKJBJS
    PBwaWUvQ1RGe1Maybe try checking the other file
    PBwaWUvQ1RGe1Maybe try checking the other file
    PBwaWUvQ1RGe1Maybe try checking the other file
    PBwaWUvQ1RGe1Maybe try checking the other file
    PBwaWUvQ1RGe1Maybe try checking the other file
    PBwaWUvQ1RGe1Maybe try checking the other file
    PBwaWUvQ1RGe1Maybe try checking the other file
    PBwaWUvQ1RGe1Maybe try checking the other file
    _googlecast
    _tcp
    local
    +Chromecast-18e2a8da30459b730aec93a71af19988
    _googlecast
    _tcp
    local
    +Chromecast-18e2a8da30459b730aec93a71af19988
    _googlecast
    _tcp
    local
    .+Chromecast-18e2a8da30459b730aec93a71af19988
    #id=18e2a8da30459b730aec93a71af19988#cd=EB3B62CAFB4F51F0114CFB58C4FE2C2F
    rm=B8B7BA5A0CEB76E5
    ve=05
    md=Chromecast
    ic=/setup/icon.png
    fn=Living Room TV	ca=465413
    st=0
    bs=FA8FCA54567B
    nf=2
    I$18e2a8da-3045-9b73-0aec-93a71af19988
    +Chromecast-18e2a8da30459b730aec93a71af19988
    _googlecast
    _tcp
    local
    #id=18e2a8da30459b730aec93a71af19988#cd=EB3B62CAFB4F51F0114CFB58C4FE2C2F
    rm=B8B7BA5A0CEB76E5
    ve=05
    md=Chromecast
    ic=/setup/icon.png
    fn=Living Room TV	ca=465413
    st=0
    bs=FA8FCA54567B
    nf=2

From here it was evident that the flag has been splitted. The random bits of characters preceeding the messages seem to be `base64` encoded. Combining them all:
    
    iBwaWNvQ1RGe1PBwaWUvQ1RGesabababkjaASKBKSBACVVAVSDDSSSSDSKJBJSAABBHHPJGTFRLKVGhpcyBpcyB0aGUgc2VjcmV0OiBwaWNvQ1RGe1IzNERJTkdfTE9LZF8=
putting this string in a base64 decoder we get this message:

`This is the secret: picoCTF{R34DING_LOKd_`

Since this is not the complete flag and the messages in the dump.pcap also ask us to check the other file (supposedly the zip file), this must be the password.

using `picoCTF{R34DING_LOKd_` as the password, we can unzip the file to get the flag

    picoCTF{R34DING_LOKd_fil56_succ3ss_cbf2ebf6}
