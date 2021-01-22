import pytest


if __name__=='__main__':
    # pytest.main(['-m','P0'])
    # pytest.main(['-m','P0','--alluredir',"./report"])


    pytest.main(['-s','-q','--alluredir','report','test_01.py'])