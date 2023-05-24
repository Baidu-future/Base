import json

from deepdiff import DeepDiff
a=[1,2,3,8,9]
b=[1,2,3,4,7]
print(json.dumps(DeepDiff(a,b),indent=5))