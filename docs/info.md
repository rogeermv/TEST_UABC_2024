  <!---

This file is used to generate your project datasheet. Please fill in the information below and delete any unused
sections.

You can also include images in this folder and reference them in the markdown. Each image must be less than
512 kb in size, and the combined size of all images must be less than 1 MB.
-->

## How it works

Uses a set of registers to divide the clock, and then some combinational logic to convert from binary to decimal for the display.
With all the inputs set to 0, the internal 24 bit compare is set to 10,000,000. This means the counter will increment by one each second.

## How to test

After reset, the counter should increase by one every second with a 10MHz input clock. Experiment by changing the inputs to change the counting speed.

## External hardware

Display 7 segment
