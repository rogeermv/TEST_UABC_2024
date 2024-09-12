# SPDX-FileCopyrightText: © 2024 Tiny Tapeout
# SPDX-License-Identifier: Apache-2.0

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles


@cocotb.test()
async def test_seg7(dut):
    dut._log.info("Start test for seg7")

    clock = Clock(dut.clk, 1, units="ms")
    cocotb.start_soon(clock.start())

    # Resetear
    dut._log.info("Reset")
    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 1000)
    dut.rst_n.value = 1

    dut._log.info("Begin testing digit-to-segment mapping")

    # Lista de casos de prueba (digito, valor esperado del segmento)
    test_cases = [
        (0, 0b0111111),  # A
        (1, 0b0000110),  # b
        (2, 0b1011011),  # C
        (3, 0b1001111),  # d
        (4, 0b1100110),  # E
        (5, 0b1101101),  # F
        (6, 0b1111101),  # G
        (7, 0b0000111),  # H
        (8, 0b1111111),  # I
        (9, 0b1101111),  # J
        (10, 0b1011110), # K
        (11, 0b0111001), # L
        (12, 0b1110110), # M
        (13, 0b1011110), # N
        (14, 0b1111011), # O
        (15, 0b1111110), # P
    ]

    for digit, expected in test_cases:
        dut.digit.value = digit
        await ClockCycles(dut.clk, 1000)
        assert dut.segments.value == expected, f"Test failed for digit {digit}: expected {bin(expected)}, got {bin(dut.segments.value)}"

    dut._log.info("All tests passed!")
