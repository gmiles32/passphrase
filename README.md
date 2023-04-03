# Passphrase
Passphrase is a lightweight python application meant to generate a specified number of words/values for a passphrase. __These are not meant to be used as a standalone passphrase__. You should instead use them in tandem with a capitalization scheme, and add some other alphanumeric characters.

## Example
Lets say passphrase returns the following values: jibe, ardent, llll

Note that these are not all words. That's okay! Just use what is returned to you. You can then combine these with other characters (lets say alternating # and 9 every 4 letters for this example) and a capitaliztion scheme (alternating between the 2nd and 4th character) to get the following passphrase: _jIbe#ardE9nTll#ll_

Not bad! Now, obviously this style of password would be very difficult to remember, but it's 2023 - use a password manager. By default, Passphrase will return 3 values, but you can request any number of values for your password. I recommend 3 for normal use, and 4-5 for something needing extra security like a master password for a password manager. 

If you want additional security, feel free to use the [included PDF](dicewarewordlist.pdf) and actual dice. This eliminates any possibility of anyone knowing anything about your password.

# Installation

For now, just pull this repo and install manually (on Linux only):
```
git clone github.com/gmiles32/passphrase
chmod +x passphrase.py
export PATH="$HOME/passphrase/:$PATH"
```

Other installation methods will be coming in the future.

# Usage

```
# Get the default 3 values
$ passphrase    # or `python3 passphrase.py if not added to path

# Get n values
$ passphrase n  # or `python3 passphrase.py n if not added to path
```

Passphrase will then return the desired number of values.

# Future work
There are a couple of changes that will be made in the future:
- Easier installing process with `pip` (adding to PyPi)
- Addition of a WebUI (for fun)
- Dockerization (also for fun)

Look out for updates, and stay safe out there!