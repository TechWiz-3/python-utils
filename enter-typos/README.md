# Enter typos

Often when hitting enter, I accidentally hit a key next to it. Often the resulting input can end up looking like this.

```py
characters = ["/", "'" "\" "]"]
input = "<regular input> <random-character><enter>"
```

This library is designed to remove trailing special characters from strings and integers and return what the user actually mean to enter.

