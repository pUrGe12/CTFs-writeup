we've been given the following php code which has been used to encode the password,

    <?
    $encodedSecret = "3d3d516343746d4d6d6c315669563362";
    function encodeSecret($secret) {
    return bin2hex(strrev(base64_encode($secret)));
    }
    if(array_key_exists("submit", $_POST)) {
        if(encodeSecret($_POST['secret']) == $encodedSecret) {
          print "Access granted. The password for natas9 is <censored>";
        } else {
          print "Wrong secret";
      }
    }
    ?>

now its clear that we need to decode the password. The following php script will apply the revelant functions in order to decode it.

    <?php
    $encodedSecret = "3d3d516343746d4d6d6c315669563362";

    function decodeSecret($secret) {
      return base64_decode(strrev(hex2bin($secret)));
    }
    print decodeSecret($encodedSecret)
    ?>
you may use any online php compiler (like W3School) to run this. Once the secret is decoded, get the flag.
