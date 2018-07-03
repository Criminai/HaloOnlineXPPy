# HaloOnlineXPPy

Returns what Rank in halo online you would be from the value of `xp`

The math is as follows:
```
ceil(√(12100+440*max(xp-280))-110)/220)
```

This returns a int ranging from 0 to 41
