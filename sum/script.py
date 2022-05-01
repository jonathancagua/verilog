from os import system
veri_file = 'sum1b'
veri_file_tb = veri_file+'_tb'
line_vhdl = veri_file+'.v ' + veri_file_tb+'.v'


system("iverilog -o "+veri_file+' '+line_vhdl)
system("vvp "+veri_file)
system("open /Applications/gtkwave.app "+ veri_file_tb+".vcd")