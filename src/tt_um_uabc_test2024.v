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
    
    reg [23:0] counter;          
    reg [3:0]  display_value;    
    reg [6:0]  segment_reg;      

    always @(posedge clk or negedge rst_n) begin
        if (!rst_n) begin
            counter <= 24'd0;
            display_value <= 4'd0;
        end else if (counter == 24'd10000000) begin
            counter <= 24'd0;
            display_value <= display_value + 1'b1;
            
            if (display_value == 4'd15) begin
                display_value <= 4'd0;
            end
        end else begin
            counter <= counter + 1'b1;
        end
    end

    seg7 seg7(.digit(display_value), .segments(segment_reg));
    
  assign uo_out = segment_reg; 
  assign uio_out = 0;
  assign uio_oe  = 0;

  // List all unused inputs to prevent warnings
    wire _unused = &{ena,ui_in,uio_in};
endmodule
