/*
 * Copyright (c) 2024 Your Name
 * SPDX-License-Identifier: Apache-2.0
 */

`default_nettype none

module tt_um_uabc_test2024 (
    input  wire [7:0] ui_in,    // Dedicated inputs
    output wire [7:0] uo_out,   // Dedicated outputs
    input  wire [7:0] uio_in,   // IOs: Input path
    output wire [7:0] uio_out,  // IOs: Output path
    output wire [7:0] uio_oe,   // IOs: Enable path (active high: 0=input, 1=output)
    input  wire       ena,      // always 1 when the design is powered, so you can ignore it
    input  wire       clk,      // clock
    input  wire       rst_n     // reset_n - low to reset
);
    
    reg [23:0] counter;          // 25-bit counter to create 1-second delay
    reg [3:0]  display_value;    // Value to display
    reg [6:0]  segment_reg;      // Register to store the current segment value

  // Counter for 1-second delay
    always @(posedge clk or negedge rst_n) begin
        // if reset, set counter to 0
        if (!rst_n) begin
            counter <= 24'd0;
            display_value <= 4'd0;
        end else begin
            if (counter == 24'd10000000) begin
                // reset
                counter <= 24'd0;

                // increment digit
                display_value <= display_value + 1'b1;

                // only count from 0 to 15
                if (display_value == 4'd15)
                    display_value <= 4'd0;

            end else
                // increment counter
                counter <= counter + 1'b1;
        end
    end

  // Assign letters and numbers in binary to uo_out
    always @(*) begin
        case (display_value)
            4'd0: segment_reg = 7'b0111111; // A
            4'd1: segment_reg = 7'b0000110; // b
            4'd2: segment_reg = 7'b1011011; // C
            4'd3: segment_reg = 7'b1001111; // d
            4'd4: segment_reg = 7'b1100110; // E
            4'd5: segment_reg = 7'b1101101; // F
            4'd6: segment_reg = 7'b1111101; // G
            4'd7: segment_reg = 7'b0000111; // H
            4'd8: segment_reg = 7'b1111111; // I
            4'd9: segment_reg = 7'b1101111; // J
            4'd10: segment_reg = 7'b1011110; // K
            4'd11: segment_reg = 7'b0111001; // L
            4'd12: segment_reg = 7'b1110110; // M
            4'd13: segment_reg = 7'b1011110; // N
            4'd14: segment_reg = 7'b1111011; // O
            4'd15: segment_reg = 7'b1111110; // P
        default: segment_reg = 7'b0000000; // Blank (off)
    endcase
  end

  assign uo_out = segment_reg; // Output segment data to display
  assign uio_out = 0; // Ensure that unused IO outputs are zero
  assign uio_oe = 8'hFF; // Enable all IOs for output

  // List all unused inputs to prevent warnings
  //wire _unused = &{ena, clk, rst_n, 1'b0};

endmodule
