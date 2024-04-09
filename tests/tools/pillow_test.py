from testbook import testbook

@testbook('./tools/pillow.ipynb', execute=True)
def test_notebook(nb):
   work_directory = nb.get('work_directory')
   assert work_directory == './pillow'