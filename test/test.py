# SPDX-FileCopyrightText: © 2024 Tiny Tapeout
# SPDX-License-Identifier: Apache-2.0

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles, FallingEdge, Timer, ClockCycles

segments = [ 63, 6, 91, 79, 102, 109, 125, 7, 127, 111, 94, 57, 118, 94, 123, 126]

binary = [
    '00111111',  # 63 en decimal
    '00000110',  # 6 en decimal
    '01011011',  # 91 en decimal
    '01001111',  # 79 en decimal
    '01100110',  # 102 en decimal
    '01101101',  # 109 en decimal
    '01111101',  # 125 en decimal
    '00000111',  # 7 en decimal
    '01111111',  # 127 en decimal
    '01101111',  # 111 en decimal
    '01011110',  # 94 en decimal
    '00111001',  # 57 en decimal
    '01110110',  # 118 en decimal
    '01011110',  # 94 en decimal
    '01111011',  # 123 en decimal
    '01111110',  # 126 en decimal
]


@cocotb.test()
async def test_7seg(dut):
    dut._log.info("Start")

    clock = Clock(dut.clk, 1, units="ms")
    cocotb.start_soon(clock.start())

    # Reset
    dut._log.info("Reset")
    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 1)
    dut.rst_n.value = 1

    dut._log.info("Test project behavior")

    for i in range(16):
        dut._log.info("Check segment {}".format(i))
        await ClockCycles(dut.clk, 1000)

        # Convert the binary vector to decimal
        binary_value = binary_vectors[i]
        expected_decimal = segments[i]
        converted_decimal = int(binary_value, 2)

        # Check if the segment output matches the expected value
        assert int(dut.segments.value) == converted_decimal
        
        # all bidirectionals are set to output
        assert dut.uio_oe == 0xFF


