class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        
        seq = []  # seq[k] = k-th number in the additive sequence

        def backtracking(i: int, j: int):
            """
            i = index in the string num that we are currently processing
            j = index of the number in seq that we are currently building
            """

            # If we consumed all digits, check if we formed a valid sequence
            if i >= len(num):
                return (
                    len(seq) >= 3 and
                    seq[-1] == seq[-2] + seq[-3]
                )

            x = int(num[i])  # current digit

            # ----------------------------------------------------------
            # Case 1: CREATE a NEW number seq[j]
            # ----------------------------------------------------------
            if len(seq) <= j:

                # create the new number using this digit
                seq.append(x)

                # Option A: continue extending this number
                # (only allowed if the number does not start with 0)
                if x != 0:
                    if backtracking(i + 1, j):
                        seq.pop()   # undo before returning
                        return True

                # Option B: finish this number and move to next number
                # allowed only if additive rule is satisfied 
                # or we are dealing with the first two numbers in seq
                if (j < 2) or (seq[j-2] + seq[j-1] == seq[j]):
                    if backtracking(i + 1, j + 1):
                        seq.pop()  # undo before returning
                        return True

                # backtrack: remove the number we created
                seq.pop()
                return False

            # ----------------------------------------------------------
            # Case 2: EXTEND an existing number seq[j]
            # ----------------------------------------------------------
            else:

                # append digit x to the current number
                seq[j] = seq[j] * 10 + x

                # Option A: keep extending this number
                if backtracking(i + 1, j):
                    seq[j] //= 10      # undo modification
                    return True

                # Option B: finish this number and move to next number
                # only if additive condition holds
                # or we are dealing with the first two numbers in seq
                if (j < 2) or (seq[j-2] + seq[j-1] == seq[j]):
                    if backtracking(i + 1, j + 1):
                        seq[j] //= 10  # undo modification
                        return True

                seq[j] //= 10  # undo modification
                return False

        return backtracking(0, 0)