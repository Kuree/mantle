module Mux2 (input [1:0] I, input  S, output  O);
wire  SB_LUT4_inst0_O;
SB_LUT4 #(.LUT_INIT(16'hCACA)) SB_LUT4_inst0 (.I0(I[0]), .I1(I[1]), .I2(S), .I3(1'b0), .O(SB_LUT4_inst0_O));
assign O = SB_LUT4_inst0_O;
endmodule

module Mux4 (input [3:0] I, input [1:0] S, output  O);
wire  Mux2_inst0_O;
wire  Mux2_inst1_O;
wire  Mux2_inst2_O;
Mux2 Mux2_inst0 (.I({I[1],I[0]}), .S(S[0]), .O(Mux2_inst0_O));
Mux2 Mux2_inst1 (.I({I[3],I[2]}), .S(S[0]), .O(Mux2_inst1_O));
Mux2 Mux2_inst2 (.I({Mux2_inst1_O,Mux2_inst0_O}), .S(S[1]), .O(Mux2_inst2_O));
assign O = Mux2_inst2_O;
endmodule

module Mux8 (input [7:0] I, input [2:0] S, output  O);
wire  Mux4_inst0_O;
wire  Mux4_inst1_O;
wire  Mux2_inst0_O;
Mux4 Mux4_inst0 (.I({I[3],I[2],I[1],I[0]}), .S({S[1],S[0]}), .O(Mux4_inst0_O));
Mux4 Mux4_inst1 (.I({I[7],I[6],I[5],I[4]}), .S({S[1],S[0]}), .O(Mux4_inst1_O));
Mux2 Mux2_inst0 (.I({Mux4_inst1_O,Mux4_inst0_O}), .S(S[2]), .O(Mux2_inst0_O));
assign O = Mux2_inst0_O;
endmodule

