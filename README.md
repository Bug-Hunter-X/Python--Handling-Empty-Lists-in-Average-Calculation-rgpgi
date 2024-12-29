# Python: Handling Empty Lists in Average Calculation
This repository demonstrates a common coding error in Python related to handling empty lists when calculating the average of numbers.  The initial code has a bug where it silently returns 0 when given an empty list. The improved solution includes more robust error handling.

## Bug
The original code attempts to calculate the average of a list of numbers.  However, it fails to correctly handle the case where the input list is empty. The solution handles this edge case by explicitly checking if the list is empty and returning a more meaningful result or raising an exception instead of returning 0 silently.