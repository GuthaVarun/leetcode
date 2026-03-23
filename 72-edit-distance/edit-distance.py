class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        if m < n: return self.minDistance(word2, word1)
        
        # 1. Initialize the Boundary Potential (The 'Dose' baseline)
        # We only need O(min(m,n)) space to store the current flux level.
        previous_flux = list(range(n + 1))
        
        # 2. Integrate the Signal
        for i, char1 in enumerate(word1):
            # The 'Potential' at the start of each row
            current_flux = [i + 1]
            for j, char2 in enumerate(word2):
                # Calculate the 'Substitution Cost' (The Diagonal Move)
                # Cost is 0 if characters align (Perfect Signal), 1 if they don't (Noise)
                sub_cost = previous_flux[j] + (0 if char1 == char2 else 1)
                
                # Calculate the 'Insertion/Deletion Cost' (The Orthogonal Moves)
                # We take the minimum 'Energy' of the three possible paths
                current_flux.append(min(sub_cost, 
                                        current_flux[-1] + 1, 
                                        previous_flux[j + 1] + 1))
            previous_flux = current_flux
            
        return previous_flux[-1]        