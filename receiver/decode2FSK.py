#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Decode2Fsk
# Generated: Sun Dec 30 01:35:16 2018
##################################################

from gnuradio import analog
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import math


class decode2FSK(gr.top_block):

    def __init__(self, fileIN="", fileOUT=""):
        gr.top_block.__init__(self, "Decode2Fsk")

        ##################################################
        # Parameters
        ##################################################
        self.fileIN = fileIN
        self.fileOUT = fileOUT

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 1.2e6
        self.deviation_hz = deviation_hz = 10e3
        self.deci = deci = 1
        self.baud_rate = baud_rate = 5e3
        self.samp_per_sym = samp_per_sym = samp_rate/(baud_rate*deci)
        self.modulation_index = modulation_index = deviation_hz/(baud_rate/2)
        self.bandwidth = bandwidth = 25e3
        self.gain_fsk = gain_fsk = samp_per_sym/(math.pi*modulation_index)
        self.freq = freq = 2e3
        self.firdes_filter = firdes_filter = firdes.low_pass(1,samp_rate,bandwidth,bandwidth/4)

        ##################################################
        # Blocks
        ##################################################
        self.freq_xlating_fir_filter_xxx_0 = filter.freq_xlating_fir_filter_ccc(deci, (firdes_filter), freq, samp_rate)
        self.digital_clock_recovery_mm_xx_0 = digital.clock_recovery_mm_ff(samp_per_sym*(1+0.0), 0.25*0.175*0.175, 0.5, 0.175, 0.020)
        self.digital_binary_slicer_fb_1 = digital.binary_slicer_fb()
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_gr_complex*1, fileIN, False)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_char*1, fileOUT, False)
        self.blocks_file_sink_0.set_unbuffered(False)
        self.analog_quadrature_demod_cf_0 = analog.quadrature_demod_cf(gain_fsk)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_quadrature_demod_cf_0, 0), (self.digital_clock_recovery_mm_xx_0, 0))    
        self.connect((self.blocks_file_source_0, 0), (self.blocks_throttle_0, 0))    
        self.connect((self.blocks_throttle_0, 0), (self.freq_xlating_fir_filter_xxx_0, 0))    
        self.connect((self.digital_binary_slicer_fb_1, 0), (self.blocks_file_sink_0, 0))    
        self.connect((self.digital_clock_recovery_mm_xx_0, 0), (self.digital_binary_slicer_fb_1, 0))    
        self.connect((self.freq_xlating_fir_filter_xxx_0, 0), (self.analog_quadrature_demod_cf_0, 0))    

    def get_fileIN(self):
        return self.fileIN

    def set_fileIN(self, fileIN):
        self.fileIN = fileIN
        self.blocks_file_source_0.open(self.fileIN, False)

    def get_fileOUT(self):
        return self.fileOUT

    def set_fileOUT(self, fileOUT):
        self.fileOUT = fileOUT
        self.blocks_file_sink_0.open(self.fileOUT)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_firdes_filter(firdes.low_pass(1,self.samp_rate,self.bandwidth,self.bandwidth/4))
        self.set_samp_per_sym(self.samp_rate/(self.baud_rate*self.deci))
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)

    def get_deviation_hz(self):
        return self.deviation_hz

    def set_deviation_hz(self, deviation_hz):
        self.deviation_hz = deviation_hz
        self.set_modulation_index(self.deviation_hz/(self.baud_rate/2))

    def get_deci(self):
        return self.deci

    def set_deci(self, deci):
        self.deci = deci
        self.set_samp_per_sym(self.samp_rate/(self.baud_rate*self.deci))

    def get_baud_rate(self):
        return self.baud_rate

    def set_baud_rate(self, baud_rate):
        self.baud_rate = baud_rate
        self.set_modulation_index(self.deviation_hz/(self.baud_rate/2))
        self.set_samp_per_sym(self.samp_rate/(self.baud_rate*self.deci))

    def get_samp_per_sym(self):
        return self.samp_per_sym

    def set_samp_per_sym(self, samp_per_sym):
        self.samp_per_sym = samp_per_sym
        self.set_gain_fsk(self.samp_per_sym/(math.pi*self.modulation_index))
        self.digital_clock_recovery_mm_xx_0.set_omega(self.samp_per_sym*(1+0.0))

    def get_modulation_index(self):
        return self.modulation_index

    def set_modulation_index(self, modulation_index):
        self.modulation_index = modulation_index
        self.set_gain_fsk(self.samp_per_sym/(math.pi*self.modulation_index))

    def get_bandwidth(self):
        return self.bandwidth

    def set_bandwidth(self, bandwidth):
        self.bandwidth = bandwidth
        self.set_firdes_filter(firdes.low_pass(1,self.samp_rate,self.bandwidth,self.bandwidth/4))

    def get_gain_fsk(self):
        return self.gain_fsk

    def set_gain_fsk(self, gain_fsk):
        self.gain_fsk = gain_fsk
        self.analog_quadrature_demod_cf_0.set_gain(self.gain_fsk)

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self.freq_xlating_fir_filter_xxx_0.set_center_freq(self.freq)

    def get_firdes_filter(self):
        return self.firdes_filter

    def set_firdes_filter(self, firdes_filter):
        self.firdes_filter = firdes_filter
        self.freq_xlating_fir_filter_xxx_0.set_taps((self.firdes_filter))


def argument_parser():
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    parser.add_option(
        "", "--fileIN", dest="fileIN", type="string", default="",
        help="Set fileIN [default=%default]")
    parser.add_option(
        "", "--fileOUT", dest="fileOUT", type="string", default="",
        help="Set fileOUT [default=%default]")
    return parser


def main(top_block_cls=decode2FSK, options=None):
    if options is None:
        options, _ = argument_parser().parse_args()

    tb = top_block_cls(fileIN=options.fileIN, fileOUT=options.fileOUT)
    tb.start()
    tb.wait()


if __name__ == '__main__':
    main()
