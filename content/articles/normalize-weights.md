Title: Normalizing Weights
Category: Blog
Date: 2016-11-04
Tags: Code, Maya

From Ryan Porter

```
import sys

approximately = lambda lhs, rhs: abs(lhs - rhs) <= sys.float_info.epsilon

def normalizeValues(*values):
    result = [v for v in values]

    s = sum(result)

    if not approximately(s, 1.0):
        result = [pow(v, 2.0) for v in values]

        s = pow(sum(result), 0.50)

        result = [pow(v / s, 2.0) for v in values]

    return result
```
