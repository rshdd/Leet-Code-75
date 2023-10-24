class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        count1, count2 = 0, 0         
        merged_string = ""

        # Mientras que 0 sea menor o igual a la cantidad de letras en las palabras
        while count1 <= len(word1) or count2 <= len(word2):
            # Mientras que el contador sea menor a la lengitud de la palabra 1
            if count1 < len(word1):
                # Usamos el contador count1 como índice para añadirlo a merged_string
                merged_string = merged_string + word1[count1]

            # Mientras que el contador sea menor a la lengitud de la palabra 2
            if count2 < len(word2):
                # Usamos el contador count2 como índice para añadirlo a merged_string
                merged_string = merged_string + word2[count2]

            # Aumentar contadores de 1 en 1
            count1 += 1
            count2 += 1
        
        # Regresar la palabra cuando el while salga
        return merged_string
