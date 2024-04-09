from testbook import testbook

@testbook('./tools/pydantic.ipynb', execute=True)
def test_notebook(nb):
   nb_completion = nb.get('nb_completion')
   ret = nb_completion()
   assert isinstance(ret, int)
   assert ret > 0 and ret <= 10