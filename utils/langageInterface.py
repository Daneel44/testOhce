from .expressions import Expressions


class langageInterface:
  
  def __init__ (self, langage=None):
    langage = str(langage).lower()
    if (langage in ["svenska", "suédois", "suedois", "swedish"]):
      self.sentences = Expressions().Svenska()
    elif (langage in ["english", "engelska", "anglais"]):
      self.sentences = Expressions().English()
    else:
      self.sentences = Expressions().French()
  
    