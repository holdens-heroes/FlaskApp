class BaseTest(object):
	pass

class TestClass(BaseTest):
	def __init__(self, testcase):
		self.test_case = testcase
	
	def run_test(self, test_name="default test"):
		print "Running %s for %s" % (test_name, self.test_case)
		