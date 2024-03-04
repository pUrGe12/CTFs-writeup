The challenge provides 3 files. Opening the `encrypt.py` file I understood the following:
1. It searches the current directory using the 'os' library, and gathers all the files other than itself
2. It then generates a random dictionary for the alphabets
3. Then it goes through each file it found previously, reads it (that is, takes the entire content of the file as 1 string), goes over each character (using list comprhension) and tries to replace it (if it can't -- for underscores, it lets it be) with its value from the randomly generated dictionary.
4. It then opens the file again in write mode (this means the previous data is lost) and dumps this encrypted message.

They have also provided us a `study-guide.txt` file. Using 

    cat -n study-guide.txt
we can see that it has around 200,000 words, all jumbled up. This is because `encrypt.py` is encrypting this file as well.

Since, the dictionary is randomly generated, there is no way to run brute-force or frequency attacks (in fact I did try a brute-force attack, which failed horribly... )

The problem description clearly mentions that this `study-guide.txt` is actually a list of real english words.

We can try and find the number of words that have a certain length (because I wanted to find a word that was small like 3 or 4 digits) but after fooling around I found that there are only 8 words that are 25 digits long
and none greater than that.

    cat study-guide.txt | grep -E '^.{25}$'

Now, a valid 25 letter word in english is rare. Matching a few patterns (you can guess the patterns by my obvious choices in `script.py`), I was able to decode the flag upto an understandble limit.

A list of 25 letter words can be found here,

        https://www.litscape.com/words/length/25_letters/25_letter_words.html

The general idea was to leverage the fact that the words in study-guide are in english and find some words high in information (rare) and use them to get the decoding_dictionary.



    
