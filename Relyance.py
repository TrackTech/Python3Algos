from abc import ABC, abstractstaticmethod
from Utils import conversion_text

class Translator(ABC):

    def __init__(self,input,conversion_method):
        self.input_str = input
        self.conversion_method = conversion_method
        self.is_converted = False
        self._input_map = {}
        self._converted_map = {}
        self._input_len = -1
        self._converted_len = -1


    @property
    def input_map(self):
        if not self.is_converted:
            self.convert_input()
        return self._input_map
    
    @property
    def converted_map(self):
        if not self.is_converted:
            self.convert_input()
        return self._converted_map
    
    @property
    def input_len(self):
        if not self.is_converted:
            self.convert_input()
        return self._input_len
    
    @property
    def converted_len(self):
        if not self.is_converted:
            self.convert_input()
        return self._converted_len

    @abstractstaticmethod
    def span_translation(self,l,r):
        pass

    @abstractstaticmethod
    def span_un_translation(self,l,r):
        pass

    def convert_input(self):
        try:
            output = self.conversion_method(self.input)
        except Exception as e:
            print("Cannot convert text - {}",e)
            raise SystemError('Could not convert text using function - {}',self.conversion_method.__name__)

        converted_index = 0
        index=0
        for index in range(len(self.input)):
            while output[converted_index]!=self.input[index]:
                converted_index+=1
            self._input_map[index]=converted_index
            self._converted_map[converted_index] = index
            converted_index+=1

        self._input_len = len(self.input)
        self._converted_len = len(output)

        #We can discard the original input once it is converted
        self.input = None
        


class Relayance_Translator(Translator):
    """
        The impementation of Relayance_Translator is linked to converstion_text method
        It enables cache
    """

    def __init__(self,input,enable_cache=False):
        super.__init__(input,conversion_text)
        self.cache = {} # Relayance_Translator implements a cache mechanism  

    def span_translation(self,l,r):

        if  ('span_translation',l,r) in self.cache:
            return self.cache[('span_translation',l,r)]

        # validate input
        if r<l or r==l:
            raise ValueError('r<l')
        if l<0 or r<0:
            raise ValueError('input less than 0')
        
        if r>self.input_len:
            raise ValueError('input out of bounds')
        
        self.cache[('span_translation',l,r)] = (self.input_map[l],self.input_map[r-1]+1)
        
        return self.cache[('span_translation',l,r)]


    def span_un_translation(self,l,r):
        if  ('span_un_translation',l,r) in self.cache:
            return self.cache[('span_un_translation',l,r)]

        # validate input
        if r<l or r==l:
            raise ValueError('r<l')
        if l<0 or r<0:
            raise ValueError('argument less than 0')
        
        if r>self.converted_len:
            raise ValueError('arguments out of bounds')
        self.cache[('span_un_translation',l,r)] = (self.converted_map[l],self.converted_map[r-1]+1)
        
        return self.cache[('span_un_translation',l,r)]


        


        


    

    


