class Solution:

    def encode(self, strs: List[str]) -> str:
        send=""
        for x in strs:
            size=len(x)
            send += f"{len(x)}.{x}"
            #send += str(size)+"."+ x
        return send

    def decode(self, s: str) -> List[str]:
        final = []
        i = 0
        while i < len(s):
            # 1. Encontrar el delimitador '.' a partir del índice actual i
            j = s.find('.', i)
            
            # 2. Extraer la longitud
            length = int(s[i:j])
            
            # 3. Extraer la palabra exacta usando rebanado
            word = s[j + 1 : j + 1 + length]
            final.append(word)
            
            # 4. Saltar el puntero al inicio de la siguiente palabra
            i = j + 1 + length
            
        return final