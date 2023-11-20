# ymd
Youtube vide download as mp3

## License
Apache License 2.0
Copyright 2023 Q0tzly

## How to install
Run it
```bash
cd
git clone https://github.com/Q0tzly/ymd.git
chmod +x ~/ymd/src/ymd.py
```

And add it to .zshrc or .bashrc (Mac)
```zshrc
export PATH="$PATH:/Users/[user]/ymd/src/"
```

Run it or Restart shell
```bash
source .zshrc
```

## How to uninstall
Only run it
```bash
cd
rm -rf ~/ymd
```

## How to use
### First
Write link list to download music to links file.

download.txt
```txt
https://www.youtube.com/○○○
https://www.youtube.com/△△△
```

### Second
```bash
ymd.py [filepath of links]
```
