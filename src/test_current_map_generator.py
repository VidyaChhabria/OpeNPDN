import pytest
import numpy as np
import current_map_generator
#@pytest.fixture

def test_read_power_report():
    pwr_rpt = current_map_generator.read_power_report("test/test_pwr_rpt.txt")
    assert 'fifo' in pwr_rpt , "Instance fifo not found in test report"
    if 'fifo' in pwr_rpt :
        assert pwr_rpt['fifo']['cell'] == "NAND2"
        assert pwr_rpt['fifo']['lib']  == "lib_file.lib"
        assert np.isclose(pwr_rpt['fifo']['internal_power'] ,2.765e-8) 
        assert np.isclose(pwr_rpt['fifo']['switching_power'],3.674e-8)
        assert np.isclose(pwr_rpt['fifo']['leakage_power']  ,0.000e-8)
        assert np.isclose(pwr_rpt['fifo']['total_power']    ,6.440e-8)

#TODO dependency on template definition json
#def test_read_def():
#    def_data = current_map_generator.read_def("test/test.def")
#    def_data['design'] == "pqrst"
#    def_data['units_per_micron'] == 100
    
def test_read_lef():
    lef_files = ['test/test1_lef.txt','test/test2_lef.txt']
    lef_data = current_map_generator.read_lef(lef_files);
    assert 'NAND2' in lef_data
    if 'NAND2' in lef_data:
        assert lef_data['NAND2']['cell'  ] == 'NAND2'
        assert lef_data['NAND2']['width' ] ==  0.345
        assert lef_data['NAND2']['height'] ==  0.567
    assert 'OR2' in lef_data
    if 'OR2' in lef_data:
        assert lef_data['OR2']['cell'  ] == 'OR2'
        assert lef_data['OR2']['width' ] ==  0.456
        assert lef_data['OR2']['height'] ==  0.678

