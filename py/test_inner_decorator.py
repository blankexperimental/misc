
class Rabbit(object):
  def __init__(self, name):
    self._name = name

  @staticmethod
  def NewRabbit(name):
    return Rabbit(name)

  @classmethod
  def NewRabbit2(cls):
    return Rabbit('rabbit2')

  @property
  def name(self):
    return self._name

rbt1 = Rabbit.NewRabbit('rabbit1')
print rbt1
print rbt1.name
rbt2 = Rabbit.NewRabbit2()
print rbt2
print rbt2.name