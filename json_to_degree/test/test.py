from nose.tools import with_setup
import os
import json_to_degree as js2deg
import subprocess
import json


class TestClass:

  @classmethod
  def setup_class(cls):
    cls.here = os.path.dirname(__file__)
    cls.data =  cls.here + '/data'

  def test_1(self):
      '''Test 1: Check that json_to_degree works when imported'''
      with open(self.data + "/json_test_in.json") as config_file:
        config_dict = json.load(config_file)

      gen_str = js2deg.dict_to_dat(config_dict)

      with open(self.data + "/json_test_out.txt") as verif_file:
          test_str = verif_file.read()

      assert(test_str == gen_str)
      pass      


  def test_2(self):
      '''Test 2: Check command line execution'''
      cmd = os.path.abspath(self.here + '/../../bin/js2degree')
      print(cmd)
      subprocess.call([cmd, self.data + "/json_test_in.json", "-o=test2.txt", "-s"])
      with open("test2.txt") as file:
          gen_str = file.read()
      with open(self.data + "/json_test_out.txt") as file:
          test_str = file.read()

      assert(test_str == gen_str)
      os.remove("test2.txt")
      pass
