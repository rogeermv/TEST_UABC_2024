# SPDX-FileCopyrightText: © 2024 Tiny Tapeout
# SPDX-License-Identifier: Apache-2.0

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles, FallingEdge, Timer, ClockCycles

segments = [ 63, 6, 91, 79, 102, 109, 125, 7, 127, 111, 94, 57, 118, 94, 123, 126]

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

    for i in range(15):
        dut._log.info("check segment {}".format(i))
        await ClockCycles(dut.clk, 1000)
        assert int(dut.segments.value) == segments[i]

        # all bidirectionals are set to output
        assert dut.uio_oe == 0xFF

    # reset
    dut.rst_n.value = 0
    # set a different compare value
    dut.ui_in.value = 3
    await ClockCycles(dut.clk, 10)
    dut.rst_n.value = 1
    
    # check all segments and roll over
    for i in range(15):
        dut._log.info("check segment {}".format(i))
        await ClockCycles(dut.clk, 1000)
        assert int(dut.segments.value) == segments[i]
