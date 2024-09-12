
/*
      -- 1 --
     |       |
     6       2
     |       |
      -- 7 --
     |       |
     5       3
     |       |
      -- 4 --
*/

module seg7 (
      input wire [3:0] digit,
      output reg [6:0] segments
);

      always @(*) begin
            case (digit)
            4'd0: segments = 7'b0111111; // A
            4'd1: segments = 7'b0000110; // b
            4'd2: segments = 7'b1011011; // C
            4'd3: segments = 7'b1001111; // d
            4'd4: segments = 7'b1100110; // E
            4'd5: segments = 7'b1101101; // F
            4'd6: segments = 7'b1111101; // G
            4'd7: segments = 7'b0000111; // H
            4'd8: segments = 7'b1111111; // I
            4'd9: segments = 7'b1101111; // J
            4'd10: segments = 7'b1011110; // K
            4'd11: segments = 7'b0111001; // L
            4'd12: segments = 7'b1110110; // M
            4'd13: segments = 7'b1011110; // N
            4'd14: segments = 7'b1111011; // O
            4'd15: segments = 7'b1111110; // P
            default: segments = 7'b0000000; // Blank (off)
            endcase
        end
endmodule

