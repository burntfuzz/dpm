<h2>Overview</h2>

dpm is a deterministic password manager written in Python.

It doesn't store passwords anywhere, but generates them using a hashing algorithm. You can generate high-entropy passwords by supplying a master password and a service, then retrieve them by supplying the same service and master password.

For example, "passW0rd1" and "gmail" will always produce the same result. So if you need your gmail password, you supply "gmail" as an argument and then type your master password to retrieve it.

<h2>Usage</h2>

```
$ ./dpm.py gmail
Password: 
N2YNG%WT5*xU!yOO$s
```
<h2>Disclaimer</h2>

This is made for educational purposes. Deterministic password managers can be useful for some niche applications, but the disadvantages of using one generally outweigh the benefits. Just use KeePass or something.

Actually, exploiting the flaws of one of these might be fun to put into a CTF machine...