###############################################################################
# Created by write_sdc
# Sun Sep  8 13:58:21 2019
###############################################################################
current_design aes_cipher_top
###############################################################################
# Timing Constraints
###############################################################################
create_clock -name clk -period 5.0000 -waveform {0.0000 2.5000} [get_ports {clk}]
###############################################################################
# Environment
###############################################################################
###############################################################################
# Design Rules
###############################################################################
