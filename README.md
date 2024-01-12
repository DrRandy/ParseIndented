# ParseIndented

The goal is to convert this:

```
step one
decision one
    branch one-one
        step one-one-one
        step one-one-two
    branch one-two
        step one-two-one
step two
step three
decision two
    branch two-one
        step two-one-one
    branch two-two
        step two-two-one
        step two-two-two
        step two-two-three
    branch two-three
        decision two-three-one
            branch two-three-one-one
                step two-three-one
            branch two-three-one-two
                step two-three-one-two-one
                step two-three-one-two-two
                step two-three-one-two-three            
step four
```

    

To this:
```
(   "step one",
    'decision one': {
        'branch one-one': (
            "step one-one-one",
            "step one-one-two",
            ),
        'branch one-two': (
            "step one-two-one",
            ),
        },
    "step two",
    "step three",
    "decision two": {
        'branch two-one': {},
            "step two-one-one",
        'branch two-two': {},
            "step two-two-one",
            "step two-two-two",
            "step two-two-three",
        'branch two-three': (
            'decision two-three-one': {
                'branch two-three-one-one': (
                    "step two-three-one",
                    ),
                'branch two-three-one-two': (
                    "step two-three-one-two-one",
                    "step two-three-one-two-two",
                    "step two-three-one-two-three",
                    ),
                },          
            ),
        },
    step four,
)
```
