# Fuck Replace

Inspired by [thefuck](https://github.com/nvbn/thefuck)

examples:

```bash
➜ apt-get install vim
E: Could not open lock file /var/lib/dpkg/lock - open (13: Permission denied)
E: Unable to lock the administration directory (/var/lib/dpkg/), are you root?

➜ fuck apt 'sudo apt'
sudo apt-get install vim
[sudo] password:
Reading package lists... Done
...
```

```bash
➜ python not_exist.py
E: python: can't open file 'not_exist.py': [Errno 2] No such file or directory

➜ fuck not_exist somedir/somefile
python somedir/somefile.py
...
```

```bash
➜ mang it
E: zsh: command not found: mang

➜ fuck 'g ' ' g'
man git
...
```

## Installation

ln -s fuck_r/fuck_r/main.py /usr/local/bin/fuck_r

Add to `.bashrc` or `.zshrc`:

```bash
function fuck { $(fuck_r "$1" "$2" $(fc -ln -1)); }
export -f fuck
```

## License

MIT
