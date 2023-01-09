from ..ohce import Ohce

class OhceBuilder:      
  def default(self):
    self._langage = 'french'
    return self.Build()
  
  def english(self):
    self._langage = 'english'
    return self.Build()
  
  def svenska(self):
    self._langage = 'svenska'
    return self.Build()    
  
  
  def Build(self):
    return Ohce(self._langage)
    