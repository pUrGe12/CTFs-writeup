going back to the list of files we found using `cd ../../../../; ls -la` we now want to navigate to the root directory. But before we do that we need to make sure 
we have the permission to view files in the root directory. 

    sudo -l
running this command we can see that we `ALL` the privileges in the system thus:

    cd /root; ls -la
notice that it won't work as we cannot change directory into the root folder. But we can view it's contents using

    sudo ls /root
and here we can see `3rd.txt` which we need to read:

    sudo less /root/3rd.txt
and we get the flag.
