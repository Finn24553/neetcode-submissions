from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapa = defaultdict(list)
        
        for palabra in strs:
            # Las palabras anagramas comparten la misma clave ordenada
            clave = "".join(sorted(palabra))
            mapa[clave].append(palabra)
            
        return list(mapa.values())