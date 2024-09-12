
# SPDX-FileCopyrightText: © 2024 Tiny Tapeout
# SPDX-License-Identifier: Apache-2.0

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles, FallingEdge, Timer, ClockCycles

segments = [ 63, 91, 91, 79, 102, 109, 125, 7, 127, 111, 94, 57, 118, 94, 123, 126]

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

    for i in range(16):  # Itera de 0 a 15, 16 valores en total
        # Establece la entrada para mostrar el segmento correcto
        dut.ui_in.value = i

        # Espera un tiempo suficiente para que el DUT procese la entrada
        await ClockCycles(dut.clk, 10)  # Ajusta el número de ciclos según sea necesario

        # Compara el valor de salida del segmento con el valor esperado
        expected_output = segments[i]
        actual_output = dut.segment_output.value  # Asegúrate de que este sea el nombre correcto del bus de salida en tu DUT
        
        dut._log.info("Checking segment {}: expected={}, got={}".format(i, expected_output, actual_output))
        assert actual_output == expected_output, f"Segment {i} output mismatch: expected {expected_output}, got {actual_output}"

    dut._log.info("Test completed")
